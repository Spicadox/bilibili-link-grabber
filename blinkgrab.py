
import requests 
from bs4 import BeautifulSoup
from csv import writer 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import os
import pathlib
import sys

import re
import argparse
import time
import urllib.request




# Final Version 2

#TODO split user url and turn it into usable url(i.e.remove everything after '?' mark)
#Sites with error: https://space.bilibili.com/654295/video?tid=0&page=1&keyword=&order=pubdate, https://space.bilibili.com/1726310?from=search&seid=12136548391520811086, link is cut at & i.e."https://space.bilibili.com/1726310?from=search"
# Learn about try, except and raise
#TODO allow user to choose pages to scrape
#TODO Decide if this script will support homepage scraping
#TODO work on allow user to scrape a page with filtered settings
#TODO Work on opening and then writing rather than rewriting file
#TODO A summary of successes and failures of getting urls per page

#Tested Links:
    #a.https://space.bilibili.com/1726310/video
    #b.https://space.bilibili.com/654295/video 

    #c.https://search.bilibili.com/all?keyword=%E3%82%A2%E3%83%8B%E3%82%B2%E3%83%A9%EF%BC%81%E3%83%87%E3%82%A3%E3%83%89%E3%82%A5%E3%83%BC%E3%83%BC%E3%83%B3
    #d.https://search.bilibili.com/all?keyword=%E9%8A%80%E9%AD%82%E6%96%87%E5%AD%97%E8%B5%B7%E3%81%93%E3%81%97
    #e.https://search.bilibili.com/all?keyword=%E3%81%8A%E9%A3%9F%E4%BA%8B%E5%87%A6%E3%81%BE%E3%81%A4%E3%81%8A%E3%81%8B&from_source=nav_search_new
        # gets "'from_source' is not recognized as an internal or external command, operable program or batch file." error but everything works due to to not getting full link
    #f.https://search.bilibili.com/all?keyword=no%20radio%20no%20life&from_source=nav_search_new
        # gets "'from_source' is not recognized as an internal or external command, operable program or batch file." error but everything works


    #h.https://space.bilibili.com/216970/channel/detail?cid=13217
    #i.https://space.bilibili.com/216970/channel/detail?cid=13214

#Untested Links:
    #Home pages
    #j.https://space.bilibili.com/942021/video
    #g.https://space.bilibili.com/391100


#Works: a,b,c,d,e,f,h,i


def make_soup(driver): 
    url = driver.current_url
    response = requests.get(url)
    # headers = {}
    # headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    # response = urllib.request.Request(url, headers=headers)
    #print(response.status_code)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def scrape_url(driver):
    i = 1

    try:
        if soup.find_all('a', class_='img-anchor') != []:
            try: 
                videoList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "img-anchor"))
                )
            except:
                driver.quit()
            
            for video in soup.find_all('a', class_='img-anchor'):
                link = video['href'].replace('//','https://')
                csv_writer.writerow([link])
                print(str(i)+'.' + link)
                i = i + 1
        
        #Tested with: https://space.bilibili.com/216970/channel/detail?cid=13214
        elif soup.find_all('a', class_='cover cover-normal') != []:
            try: 
                videoList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cover cover-normal"))
                )
            except:
                driver.quit()  

            for video in soup.find_all('a', class_='cover cover-normal'):
                link = video['href'].replace('//','https://')
                csv_writer.writerow([link])
                print(str(i)+'.' + link)
                i = i + 1

        

        elif soup.find_all('ul', class_='clearfix cube-list') != []:
            try: 
                videoList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cover"))
                )
            except:
                driver.quit()

            videos = soup.find(class_='clearfix cube-list')
            for video in videos.find_all('a', class_='cover'):
                link = video['href'].replace('//','https://')
                csv_writer.writerow([link])
                print(str(i)+'.' + link)
                i = i + 1

        #Tested with: https://space.bilibili.com/1726310?from=search&seid=12136548391520811086
        #Debate whether to also get links from 'album-top' class
        #TODO find way to split url and remove everything after question mark
        #TODO No longer works(link)?
        elif soup.find_all('div', class_='small-item fakeDanmu-item') != []:
            try: 
                videoList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cover"))
                )
            except:
                driver.quit()

            videos = soup.find(class_='content clearfix')
            for video in videos.find_all('a', class_='cover'):
                link = video['href'].replace('//','https://')
                csv_writer.writerow([link])
                print(str(i)+'.' + link)
                i = i + 1
                
        else:
            print("Error finding video urls class")

    except:
        driver.quit()
        print("Error finding video urls")
        raise Exception



def find_last_page(driver):
    try:
        
        if soup.find_all(class_='be-pager-total') != []:
            try: 
                videoList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "be-pager-total"))
                )
            except:
                driver.quit()  

            lastButton = soup.find_all(class_='be-pager-total')
            lastPage = lastButton[0].text
            words = lastPage.split()
            lastPage = int(words[1])
            return lastPage

        elif soup.find_all(class_='pages') != []:
            try: 
                videoList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pages"))
                )
            except:
                driver.quit()

            buttonList = soup.find(class_='pages')
            lastButton = buttonList.find_all('li')
            length = len(lastButton)
            lastPage = int(lastButton[length - 2].text)
            return lastPage


        elif soup.find_all("page-item last") != []:
            try: 
                videoList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "page-item last"))
                )
            except:
                driver.quit()

            lastButton = soup.find_all(class_='page-item last')
            lastPage = lastButton[0].text
            lastPage = int(lastPage)
            return lastPage

        #Tested with: https://space.bilibili.com/216970/channel/detail?cid=13214
        elif soup.find_all("be-pager") != []:
            try: 
                videoList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "be-pager"))
                )
            except:
                driver.quit()

            lastButton = soup.find_all(class_='be-pager')
            length = len(lastButton)
            lastPage = lastButton[length - 3].text
            lastPage = int(lastPage)
            return lastPage

        elif soup.find_all(class_='pagination-btn') != []:
            try: 
                videoList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pagination-btn"))
                )
            except:
                driver.quit()
            
            lastButton = soup.find_all(class_='pagination-btn')
            lastPage = lastButton[0].text
            lastPage = int(lastPage)
            return lastPage

        #Tested with: https://space.bilibili.com/1726310?from=search&seid=12136548391520811086
        else:
            print("Can't find total pages")
            lastPage = 0
            return lastPage

    except:
        print("Error: Can't get the last page")
        raise Exception

try:
    try: 
        #TODO 
        #try catch PermissionError 
        #Catch invalid urls


        defaultPath = pathlib.Path().absolute()
        print("Default Save Location:", defaultPath, "\n")
        parser = argparse.ArgumentParser(prog='biliurls')

        # Arguments
        parser.add_argument('-n', '--name',
                            type=str,
                            nargs='+',
                            metavar='',
                            default='output',
                            help="Name of the csv file")

        parser.add_argument('-d', '--driver',
                            type=str,
                            nargs='+',
                            default=defaultPath,
                            help="Absolute web driver path")

        parser.add_argument('-s', '--save',
                            type=str,
                            nargs='+',
                            default=defaultPath,
                            help="The user's chosen absolute save path for the csv file")
        
        parser.add_argument('-l', '--link',
                            type=str,
                            metavar='',
                            required=True,
                            help="Link to extract video urls,it is recommended for the link to be enclosed in double quotation though not necessary")

        parser.add_argument('-w', '--wait',
                            type=int,
                            metavar='',
                            help="The amount of second to stop and wait for browser to load. Recommended for use only if browser is taking longer than 2 seconds to load. Prevent links from being extracted on same page as the next page has yet to load.")                    
        
        parser.add_argument('-q', '--quiet',
                            action='store_false',
                            help="Show more information as the command executes")

        # parser.add_argument('-p', '--page',
        #                     type=int,
        #                     nargs='+',
        #                     action='store_true',
        #                     help="Select specific page(s) to scrape")

        args = parser.parse_args()
        
        if args.driver is not None:
            DRIVER_PATH = " ".join(args.driver)
            print("DRIVER_PATH: " + DRIVER_PATH)

        if args.name is not None:
            FILE_NAME = "_".join(args.name)
            print("File Name: " + FILE_NAME)


        link = args.link
        print("Link: " + link + "\n")
        if args.wait is not None:
            wait = args.wait
        else:
            wait = 2

        # pages = args.page
        # print(pages)

        INVALID_CHARACTERS_RE =  re.compile(r"^[^<>/{}[\]~`]*$")
        if INVALID_CHARACTERS_RE.match(args.name):
            if args.name is not None:
                defaultFile = os.path.abspath(str(args.save) + "\\" + str(args.name)) 
                if args.quiet:
                    print(defaultFile)
            else:
                defaultFile = os.path.abspath(str(defaultPath) + "\\" + str(args.name)) 
                if args.quiet:
                    print(defaultFile)  
        else:
            if args.quiet:
                print("Error: illegal characters detected in file name or save path")
            exit()
            

        # create variable = open(defaultFile + ".csv", 'w', newline='') so try except, we can use variable.close()
        #f = open('/pythonwork/thefile_subset1.csv', 'w')
        #writer = csv.writer(f)
        #f.close()
        print(os.path.join(str(args.driver),"\\chromedriver.exe"))
        with open(defaultFile + ".csv", 'w', newline='') as csv_file:
                csv_writer = writer(csv_file)

                #DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"
                try:
                    if args.driver is not None:
                        driver = webdriver.Chrome(DRIVER_PATH + r"\\chromedriver.exe")
                        if args.quiet:
                            print("Chromedriver Path:" + DRIVER_PATH + "\\chromedriver.exe")
                    else: 
                        driver = webdriver.Chrome(os.path.abspath(str(defaultPath) + r"\\chromedriver.exe"))
                        if args.quiet:
                            print("Chromedriver Path:" + os.path.abspath(str(defaultPath) + "\\chromedriver.exe"))
                except: 
                    sys.exit("Error finding ChromeDriver. Please make sure path contains the ChromeDriver.")

                #driver = webdriver.Chrome(os.path.abspath(str(defaultPath) + r"\\WebScraping\chromedriver.exe"))

                driver.get(link)
                      
                soup = make_soup(driver)
               

                lastPage = find_last_page(driver)
                if args.quiet:
                    print("Total Pages: " + str(lastPage))
                page = 1
                pageExtension = ''
                
                if link.find('channel') == -1 and lastPage >= 1:  
                    if args.quiet:
                        print("\n" + 'Page:',1)
                    scrape_url(driver)
                    while page < lastPage:
                        page = page + 1


                        if soup.find_all(class_='h-inner') != [] and link.find('space') == -1 or link.find('keyword') > -1:
                            pageExtension = '&page='+str(page)
                            if args.quiet:
                                print(link+pageExtension)
                        else:
                            pageExtension = '?page='+str(page)
                            if args.quiet:
                                print(link+pageExtension)
                        
                        # pageExtension = '?page='+str(page)

                        fullUrl = link+pageExtension
                        driver.get(fullUrl)

                        #Sleep(2) allows all urls to be scraped
                        # Assume the sleep allows driver to get all of page's source code  before soup initializes
                        # since without it not everypage will get scraped 
                        if wait > 0:
                            time.sleep(wait - 1)
                        else:
                            time.sleep(wait)

                        #driver.set_page_load_timeout(10)
                        #driver.delete_all_cookies()
                        
                        soup = make_soup(driver)
                        scrape_url(driver)

                # In the event that the webpage is a single page application
                else:     
                    try:
                        i = 1
                        h = 1 
                        if args.quiet:
                            print("\n" + 'Page:',1)
                        # Loops through all video urls through all pages    
                        while i <= lastPage:
                            for video in soup.find_all('a', class_='cover cover-normal'):    
                                link = video['href'].replace('//','https://')
                                csv_writer.writerow([link])
                                if args.quiet:
                                    print(str(h)+'.' + link)
                                h = h + 1
                            if i < lastPage:
                                driver.find_element_by_class_name('be-pager-next').click()
                                if args.quiet:
                                    print("\n" + 'Page:',i + 1)
                                #TODO Find a better way than using sleep
                                time.sleep(wait)

                            i = i + 1
                            soup = make_soup(driver)
                        if args.quiet:    
                            print("\n" + 'Extracted:',h-1 ,'URLS')           
                    except:
                        raise Exception

                # Close all windows
                driver.quit()
    except KeyboardInterrupt:
        if args.quiet:
            sys.exit('\nUser cancelled the operation')
        driver.quit()
        
except Exception:
    if args.quiet:
        print("An unexpected error has occurred!")
        sys.exit("Exiting script")
    # Nothing executes past this comment
    driver.quit()


