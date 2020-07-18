
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

import traceback


# Final Version 2

#TODO split user url and turn it into usable url(i.e.remove everything after '?' mark)
#Sites with error: https://space.bilibili.com/654295/video?tid=0&page=1&keyword=&order=pubdate, https://space.bilibili.com/1726310?from=search&seid=12136548391520811086, link is cut at & i.e."https://space.bilibili.com/1726310?from=search"
# Learn about try, except and raise
#TODO allow user to choose pages to scrape
#TODO Decide if this script will support homepage scraping
#TODO work on allow user to scrape a page with filtered settings
#TODO Work on opening and then writing rather than rewriting file
#TODO A summary of successes and failures of getting urls per page
#TODO If file name contains just periods then save location moves back one 

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
                            help="Name of the csv file")

        parser.add_argument('-d', '--driver',
                            type=str,
                            nargs='+',
                            help="Absolute web driver path")

        parser.add_argument('-s', '--save',
                            type=str,
                            nargs='+',
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

        parser.add_argument('-p', '--page',
                            type=int,
                            nargs='+',
                            help="Select specific page(s) to scrape")

        args = parser.parse_args()
        
        
        DRIVER_PATH = str(defaultPath)
        # If --driver is used then the driver path(removing all spaces) is set and printed 
        if args.driver is not None:  
            DRIVER_PATH = " ".join(args.driver)
        if args.quiet:
            print("DRIVER PATH: " + DRIVER_PATH + "\\chromedriver.exe")
       

        # If --save is used then the save path(removing all spaces) is set and printed
        SAVE_PATH = str(defaultPath)
        if args.save is not None:
            SAVE_PATH = " ".join(args.save)
        if args.quiet:
            print("SAVE PATH: " + SAVE_PATH)

        # If --name is used then the custom file name is printed else default name is printed 
        FILE_NAME = "output"
        if args.name is not None:
            FILE_NAME = "_".join(args.name)
        if args.quiet:
            print("File Name: " + FILE_NAME)
        elif args.quiet:
            print("File Name: output")

        # sets link and prints link
        link = args.link
        if args.quiet:
            print("Link: " + link + "\n")
        
        # sets wait time
        if args.wait is not None:
            wait = args.wait
        else:
            wait = 2

        # Ensure that user inputted arguments are valid numbers


        

        # Check for invalid characters in file name and append it to current path
        INVALID_CHARACTERS_RE =  re.compile(r"^[^<>/{}[\]~`]*$")
        #INVALID_CHARACTERS_RE = re.compile(r"\\*?<>:\"/\|")

        if args.name is not None:
            if INVALID_CHARACTERS_RE.match(FILE_NAME):
                filePath = os.path.abspath(SAVE_PATH + "\\" + FILE_NAME) 
                if args.quiet:
                    print("Full File Path: " + filePath + ".csv")
            else:
                if args.quiet:
                    print("Error: illegal characters detected in file name")
                sys.exit()
        else:
            filePath = os.path.abspath(SAVE_PATH + "\\" + FILE_NAME)
            if args.quiet:
                    print("Full File Path: " + filePath + ".csv")
            

        # create variable = open(defaultFile + ".csv", 'w', newline='') so try except, we can use variable.close()
        #f = open('/pythonwork/thefile_subset1.csv', 'w')
        #writer = csv.writer(f)
        #f.close()

        with open(filePath + ".csv", 'w', newline='') as csv_file:
                csv_writer = writer(csv_file)
                
                try:
                    driver = webdriver.Chrome(DRIVER_PATH + r"\\chromedriver.exe")
                except: 
                    sys.exit("Error finding ChromeDriver. Please make sure path contains the ChromeDriver.")

                # Start up browser with user's first specified page
                if args.page is not None:
                    if "/channel/detail?cid=" in link:
                        driver.get(link)

                    if "keyword" in link:
                        driver.get(link + "&page=" + str(args.page[0]))

                    # else:
                    #     driver.get(link + "?page=" + str(args.page[0]))
                else:
                    driver.get(link)
                      


                soup = make_soup(driver)
               
               # Find the last page, total pages, current page in page argument 
                if args.page is not None:
                    lastUserPage = args.page[len(args.page) - 1]
                    totalUserPage = len(args.page)
                    currentUserPage = args.page[0]


                lastPage = find_last_page(driver)
                if args.page is None:
                    if args.quiet:
                        print("Total Pages: " + str(lastPage))
                elif args.quiet:
                    print("Total User Selected Pages: " + str(totalUserPage))

                page = 1
                pageExtension = ''
                
                # If the link does not contain the word 'channel' and is not the last page 
                if link.find('channel') == -1 and lastPage >= 1:  
                    if args.page is None:
                        if args.quiet:
                            print("\n" + 'Page:',1)
                    else:
                        if args.quiet:
                            print("\n" + 'Page:',currentUserPage)

                    scrape_url(driver)
                    count = 1
                    # If the current page is not the last page
                    # or page argument is selected and the last page has not been reached
                    while (args.page is None and page < lastPage) or (args.page is not None and currentUserPage < lastUserPage):
                        page = page + 1

                        if args.page is not None:
                            currentUserPage = int(args.page[count])
                            if args.quiet:
                                print("\nPage:",currentUserPage)
                        count = count + 1
                        if soup.find_all(class_='h-inner') != [] and link.find('space') == -1 or link.find('keyword') > -1:
                            if args.page is None:
                                pageExtension = '&page='+str(page)
                                if args.quiet:
                                    print(link+pageExtension)
                            else:
                                pageExtension = '&page='+str(currentUserPage)
                                if args.quiet:
                                    print(link+pageExtension)
                        elif args.page is not None:
                            pageExtension = '?page='+str(currentUserPage)
                            if args.quiet:
                                print(link+pageExtension)
                        else:
                            pageExtension = '?page='+str(page)
                            if args.quiet:
                                print(link+pageExtension)
                        # pageExtension = '?page='+str(page)
                        if args.page is None:
                            fullUrl = link + pageExtension
                        else:
                            fullUrl = link + pageExtension
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

#--------------------------------------------------------------------------------------------------------------------------------#
                    #     # If the current page is not the last page
                #     # or page argument is selected and the last page has not been reached
                #     ## (args.page is not None and currentUserPage < lastUserPage)
                #     if args.page is None:
                #         while page < lastPage:
                #             page = page + 1


                #         if soup.find_all(class_='h-inner') != [] and link.find('space') == -1 or link.find('keyword') > -1:
                #             pageExtension = '&page='+str(page)
                #             if args.quiet:
                #                 print(link+pageExtension)
                #         else:
                #             pageExtension = '?page='+str(page)
                #             if args.quiet:
                #                 print(link+pageExtension)
                        
                #         # pageExtension = '?page='+str(page)

                #         fullUrl = link+pageExtension
                #         driver.get(fullUrl)

                #         #Sleep(2) allows all urls to be scraped
                #         # Assume the sleep allows driver to get all of page's source code  before soup initializes
                #         # since without it not everypage will get scraped 
                #         if wait > 0:
                #             time.sleep(wait - 1)
                #         else:
                #             time.sleep(wait)

                #         #driver.set_page_load_timeout(10)
                #         #driver.delete_all_cookies()
                        
                #         soup = make_soup(driver)
                #         scrape_url(driver)

                #     else:
                #         while currentUserPage < lastUserPage:
                #             count = 1                           
                #             currentUserPage = int(args.page[count])
                #             print(currentUserPage)
                #             count = count + 1
                #             if soup.find_all(class_='h-inner') != [] and link.find('space') == -1 or link.find('keyword') > -1:                        
                #                 pageExtension = '&page='+str(page)
                #             if args.quiet:
                #                 print(link+pageExtension)
                                
                #             pageExtension = '?page='+str(currentUserPage)
                #             if args.quiet:
                #                 print(link+pageExtension)
                        
                #             fullUrl = str(link) + str(currentUserPage)
                #             driver.get(fullUrl)
                #             #Sleep(2) allows all urls to be scraped
                #             # Assume the sleep allows driver to get all of page's source code  before soup initializes
                #             # since without it not everypage will get scraped 
                #             if wait > 0:
                #                 time.sleep(wait - 1)
                #             else:
                #                 time.sleep(wait)

                #             #driver.set_page_load_timeout(10)
                #             #driver.delete_all_cookies()
                #             soup = make_soup(driver)
                #             scrape_url(driver)
#--------------------------------------------------------------------------------------------------------------------------------#

                # In the event that the webpage is a single page application
                else:     
                    i = 1
                    h = 1 
                    if args.quiet and args.page is None:
                        print("\n" + 'Page:',1)
                    elif args.quiet and args.page is not None:
                        print("\n" + 'Page:',currentUserPage)
                    # Loops through all video urls through all pages
                    if args.page is None:    
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

                    else:
                        count = 1
                        h = 1
                        counter = 0
                        # originally <= 
                        while counter < totalUserPage:
                            counter = counter + 1
                            print("CurrentUserPage",currentUserPage)
                            print("lastUserPage",lastUserPage)
                            
                            # Change pages by typing page number 
                            if currentUserPage < lastUserPage:
                                currentUserPage = int(args.page[count])
                                if currentUserPage != 1:
                                    inputPageElement = driver.find_element_by_class_name('be-pager-options-elevator')
                                    inputPage = inputPageElement.find_element_by_class_name('space_input')
                                    inputPage.send_keys(currentUserPage)
                                    inputPage.send_keys(Keys.ENTER)
                            count = count + 1

                            # Scrape
                            for video in soup.find_all('a', class_='cover cover-normal'):    
                                link = video['href'].replace('//','https://')
                                csv_writer.writerow([link])
                                if args.quiet:
                                    print(str(h)+'.' + link)
                                h = h + 1
                                
                                #TODO Find a better way than using sleep
                            time.sleep(wait)

                            soup = make_soup(driver)
                    if args.quiet:    
                        print("\n" + 'Extracted:',h-1 ,'URLS')       

                # Close all windows
                driver.quit()
    except KeyboardInterrupt:
        if args.quiet:
            sys.exit('\nUser cancelled the operation')
        driver.quit()
        
except Exception as e:
    if args.quiet:
        print("An unexpected error has occurred!")
        print(e)
        traceback.print_exc()
        #sys.exit("Exiting script")
    # Nothing executes past this comment(meaning nothing executes past sys.exit())
    driver.quit()


