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

import re
import argparse
import time


# Final Version 2

#TODO split user url and turn it into usable url(i.e.remove everything after '?' mark)
#Sites with error: https://space.bilibili.com/654295/video?tid=0&page=1&keyword=&order=pubdate, https://space.bilibili.com/1726310?from=search&seid=12136548391520811086
# Learn about try, except and raise

def make_soup(driver): 
    #response = requests.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
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
    #TODO 
    #try catch PermissionError 
    #Catch invalid urls


    defaultPath = pathlib.Path().absolute()
    print("Default Save Location:", defaultPath, "\n")
    parser = argparse.ArgumentParser(prog='biliurls')

    # Arguments
    parser.add_argument('-n', '--name',
                        type=str,
                        metavar='',
                        default='output',
                        help="Name of the csv file")

    parser.add_argument('-d', '--driver',
                        type=str,
                        metavar='',
                        nargs='+',
                        default=defaultPath,
                        help="Absolute web driver path")

    parser.add_argument('-p', '--path',
                        type=str,
                        metavar='',
                        nargs='+',
                        default=defaultPath,
                        help="The user's chosen absolute path for the csv file")
    
    parser.add_argument('-l', '--link',
                        type=str,
                        metavar='',
                        required=True,
                        help="Link to extract video urls")

    parser.add_argument('-w', '--wait',
                        type=int,
                        metavar='',
                        help="The amount of second to stop and wait for browser to load. Recommended for use only if browser is taking longer than 2 seconds to load. Prevent links from being extracted on same page as the next page has yet to load.")                    
    
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help="Show more information as the command executes")

    args = parser.parse_args()
    
    link = args.link
    if args.wait is not None:
        wait = args.wait
    else:
        wait = 2

    INVALID_CHARACTERS_RE =  re.compile(r"^[^<>/{}[\]~`]*$")
    if INVALID_CHARACTERS_RE.match(args.name):
        if args.name is not None:
            defaultFile = os.path.abspath(str(args.path) + "\\" + str(args.name)) 
            print(defaultFile)
        else:
             defaultFile = os.path.abspath(str(defaultPath) + "\\" + str(args.name)) 
             print(defaultFile)  
    else:
        print("Error: illegal characters detected in file name or save path")
        exit()
        


    print(os.path.join(str(args.driver),"\\chromedriver.exe"))
    with open(defaultFile + ".csv", 'w', newline='') as csv_file:
            csv_writer = writer(csv_file)

            #url = input("URL: ")

            #DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"

            if args.driver is not None:
                driver = webdriver.Chrome(os.path.abspath(str(args.driver) + r"\\chromedriver.exe"))
                print(os.path.abspath(str(defaultPath) + "\\chromedriver.exe"))
            else: 
                driver = webdriver.Chrome(os.path.abspath(str(defaultPath) + r"\\chromedriver.exe"))
                print(os.path.abspath(str(defaultPath) + "\\chromedriver.exe"))

            #driver = webdriver.Chrome(os.path.abspath(str(defaultPath) + r"\\WebScraping\chromedriver.exe"))

            driver.get(link)

            soup = make_soup(driver)

            lastPage = find_last_page(driver)

            print("Total Pages: " + str(lastPage))
            page = 1
            pageExtension = ''
            
            if link.find('channel') == -1 and lastPage > 1:  
                print("\n" + 'Page:',1)
                scrape_url(driver)
                while page < lastPage:
                    page = page + 1


                    if soup.find_all(class_='h-inner') != [] and link.find('space') == -1:
                        pageExtension = '&page='+str(page)
                        print(link+pageExtension)
                    else:
                        pageExtension = '?page='+str(page)
                        print(link+pageExtension)
                    
                    # pageExtension = '?page='+str(page)

                    fullUrl = link+pageExtension
                    driver.get(fullUrl)
                    soup = make_soup(driver)
                    time.sleep(2)
                    scrape_url(driver)

            # In the event that the webpage is a single page application
            else:     
                try:
                    i = 1
                    h = 1 
                    print("\n" + 'Page:',1)
                    # Loops through all video urls through all pages    
                    while i <= lastPage:
                        for video in soup.find_all('a', class_='cover cover-normal'):    
                            link = video['href'].replace('//','https://')
                            csv_writer.writerow([link])
                            print(str(h)+'.' + link)
                            h = h + 1
                        if i < lastPage:
                            driver.find_element_by_class_name('be-pager-next').click()
                            print("\n" + 'Page:',i + 1)
                            #TODO Find a better way than using sleep
                            time.sleep(wait)

                        i = i + 1
                        soup = make_soup(driver)
                    print("\n" + 'Extracted:',h-1 ,'URLS')           
                except:
                    raise Exception

            # Close all windows
            driver.quit()
except KeyboardInterrupt as ke:
    print('\nUser cancelled the operation')
    driver.quit()
