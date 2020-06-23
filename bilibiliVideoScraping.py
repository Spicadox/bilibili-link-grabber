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

# def make_soup(url): 
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     return soup

# def scrape_url():
#     for video in soup.find_all('a', class_='img-anchor'):
#         link = video['href'].replace('//','https://')
#         csv_writer.writerow([link])

# with open("videoLinks.csv", 'w') as csv_file:
#         csv_writer = writer(csv_file)

#         url = 'https://search.bilibili.com/all?keyword=%E3%82%A2%E3%83%8B%E3%82%B2%E3%83%A9%EF%BC%81%E3%83%87%E3%82%A3%E3%83%89%E3%82%A5%E3%83%BC%E3%83%BC%E3%83%B3'
#         soup = make_soup(url)

#         lastButton = soup.find_all(class_='page-item last')
#         lastPage = lastButton[0].text
#         lastPage = int(lastPage)
#         print(lastPage)

#         page = 1
#         pageExtension = ''

#         scrape_url()

#         while page < lastPage:
#             page = page + 1
#             if page == 1:
#                 pageExtension = ''
#             else:
#                 pageExtension = '&page='+str(page)
#             print(url+pageExtension)
#             fullUrl = url+pageExtension
#             soup = make_soup(fullUrl)
#             scrape_url()
    


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#Text File version 
# def make_soup(url): 
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     return soup

# def scrape_url():
#     for video in soup.find_all('a', class_='img-anchor'):
#         link = video['href'].replace('//','')
#         text_file.write("https://"+link+'\n')

# with open("videoLinks.txt", 'w') as text_file:
#         #csv_writer = writer(text_file)

#         url = 'https://search.bilibili.com/all?keyword=%E3%82%A2%E3%83%8B%E3%82%B2%E3%83%A9%EF%BC%81%E3%83%87%E3%82%A3%E3%83%89%E3%82%A5%E3%83%BC%E3%83%BC%E3%83%B3'
#         soup = make_soup(url)

#         lastButton = soup.find_all(class_='page-item last')
#         lastPage = lastButton[0].text
#         lastPage = int(lastPage)
#         print(lastPage)

#         page = 1
#         pageExtension = ''

#         scrape_url()

#         while page < lastPage:
#             page = page + 1
#             if page == 1:
#                 pageExtension = ''
#             else:
#                 pageExtension = '&page='+str(page)
#             print(url+pageExtension)
#             fullUrl = url+pageExtension
#             soup = make_soup(fullUrl)
#             scrape_url()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#Version 2
# def make_driver(url):
#     DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"
#     driver = webdriver.Chrome(DRIVER_PATH)
#     driver.get(url)
#     return driver

# def make_soup(url): 
#     response = requests.get(url)
#     soup = BeautifulSoup(make_driver(url).page_source, 'html.parser')
#     return soup

# def scrape_url():
#     try:

#         videoList = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "img-anchor"))
        

#         for video in soup.find_all('a', class_='img-anchor'):
#             link = video['href'].replace('//','https://')
#             csv_writer.writerow([link])
#     except Exception:
#         print("URL can't be obtained via img-anchor class")
#         driver.
        
#         try: 
#             for video in soup.find_all('a', class_='cover cover-normal'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#         except Exception:
#             print("URL can't be obtained via cover cover-normal class")

#             try: 
#                 for video in soup.find_all('a', class_='cover'):
#                     link = video['href'].replace('//','https://')
#                     csv_writer.writerow([link])
#             except Exception:
#                 print("URL can't be obtained via cover cover-normal class")
#                 raise Exception

# def find_last_page(url):
#     try:
#         lastButton = soup.find_all(class_='pagination-btn')
#         lastPage = lastButton[0].text
#         lastPage = int(lastPage)
#         return lastPage
#     except Exception:
#         print("Can't find last page due to class not being 'pagination-btn'")

#         try: 
#             lastButton = soup.find_all(class_='be-pager-total')
#             lastPage = lastButton[0].text
#             totalPage = []
#             finalPage = 0
#             for word in lastPage.split():
#                 if word.isdigit():
#                     totalPage.append(int(word))
#                     finalPage = totalPage[0]
#             return finalPage
#         except Exception:
#             print("Can't find last page due to class not being 'be-pager-total'")

#             # Find the total number of pages
#             try:
#                 lastButton = soup.find_all(class_='')
#                 lastPage = lastButton[0].text

#                 lastPage = int(lastPage)
#                 return lastPage
#             except Exception:
#                 print("Can't find last page due to class not being 'page-item last'")

#                 #Find the total pages by accessing 2nd to last button in pages class
#                 try:
#                     lastButton = soup.find_all(class_='pages')
#                     length = len(lastButton)
#                     lastPage = lastButton[length - 2].text
#                     lastPage = int(lastPage)
#                     return lastPage
#                 except Exception:
#                     print("Can't find last page due to class not being 'pages'")

#                     #Find the total pages by accessing the 3rd to last button in be-pager class
#                     try:
#                         lastButton = soup.find_all(class_='be-pager')
#                         length = len(lastButton)
#                         lastPage = lastButton[length - 3].text
#                         lastPage = int(lastPage)
#                         return lastPage
#                     except Exception:
#                         print("Can't find last page due to class not being 'page-item last'")

#                         #Only one page so ignore buttons
#                         try:
#                             return None
#                         except Exception:
#                             print("Error")

# def page_extension(lastPage):
#     pageExtension = ''
#     if page == 1 or lastPage == None:
#         return pageExtension
#     else:
#         pageExtension = '&page='+str(page)
#         return pageExtension



# with open("videoLinks.csv", 'w') as csv_file:
#         csv_writer = writer(csv_file)

#         #url = 'https://space.bilibili.com/654295/video?tid=0&page=1&keyword=&order=pubdate'
#         url = input("URL: ")
        
#         soup = make_soup(url)

        

#         page = 1
#         pageExtension = ''

#         scrape_url()
#         lastPage = find_last_page(url)
#         print(lastPage)
#         while page < lastPage:
#             page = page + 1
#             if page == 1:
#                 pageExtension = ''
#             else:
#                 pageExtension = page_extension(lastPage)
#             print(url+pageExtension)
#             fullUrl = url+pageExtension
#             soup = make_soup(fullUrl)
#             scrape_url()        




###TO DO###
# 1. create a class that: finds last page
#     a. Possibly by going up the children tree or accessing 2nd to last of button class
#     b. If possible locate final page class and extract that number
#     c. Else error or if there's just one page(i.e. can't find class that button belongs to)


#-------------------------------------------------------------------------------------------------#
#Testing
# def make_driver(url):
#     DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"
#     driver = webdriver.Chrome(DRIVER_PATH)
#     driver.get(url)
#     return driver

# def make_soup(url): 
#     #response = requests.get(url)
#     soup = BeautifulSoup(make_driver(url).page_source, 'html.parser')
#     return soup

# def scrape_url():
#     for video in soup.find_all('a', class_='cover'):
#         link = video['href'].replace('//','https://')
#         csv_writer.writerow([link])

# def page_extension(lastPage):
#     pageExtension = ''
#     if page == 1 or lastPage == None:
#         return pageExtension
#     else:
#         pageExtension = '&page='+str(page)
#         return pageExtension

            
# with open("videoLinks.csv", 'w') as csv_file:
#         csv_writer = writer(csv_file)

#         url = 'https://space.bilibili.com/654295/video?tid=0&page=1&keyword=&order=pubdate'
#         #url = input("URL: ")
        
#         soup = make_soup(url)

#         page = 1
#         pageExtension = ''


#         #Find last page
#         lastButton = soup.find_all(class_='be-pager-item')
#         print(len(lastButton))
#         lastPage = lastButton[len(lastButton)].text
#         print(lastPage)
        


#         scrape_url()
#         while page < lastPage:
#             page = page + 1
#             if page == 1:
#                 pageExtension = ''
#             else:
#                 pageExtension = page_extension(lastPage)
#             print(url+pageExtension)
#             fullUrl = url+pageExtension
#             soup = make_soup(fullUrl)
#             scrape_url()   
 

 #-------------------------------------------------------------------------------------------------#
 # Test2 
 # Works still need more testing
# def make_driver(url):
#     DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"
#     driver = webdriver.Chrome(DRIVER_PATH)
#     driver.get(url)
#     return driver

# def make_soup(url): 
#     #response = requests.get(url)
#     soup = BeautifulSoup(make_driver(url).page_source, 'html.parser')
#     return soup

# def scrape_url(url):
#     i = 1
#     driver = make_driver(url)
    
#     try:
#         videoList = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "cover"))
#     )
#     except:
#         driver.quit()
#         return driver.quit()

#     videos = soup.find(class_='clearfix cube-list')
#     for videoLinks in videos.find_all('a', class_='cover'):
#         link = videoLinks['href'].replace('//','https://')
#         csv_writer.writerow([link])
#         print(i,'.',link)
#         i = i + 1

# def find_last_page(url):
#     try:
#         lastButton = soup.find_all(class_='pagination-btn')
#         lastPage = lastButton[0].text
#         lastPage = int(lastPage)
#         return lastPage
#     except Exception:
#         print("Can't find last page due to class not being 'pagination-btn'")

#         try: 
#             lastButton = soup.find_all(class_='be-pager-total')
#             lastPage = lastButton[0].text
#             words = lastPage.split()
#             lastPage = int(words[1])
#             print(lastPage)
#         except Exception:
#             print("Can't find last page due to class not being 'be-pager-total'")

#             # Find the total number of pages
#             try:
#                 lastButton = soup.find_all(class_='')
#                 lastPage = lastButton[0].text

#                 lastPage = int(lastPage)
#                 return lastPage
#             except Exception:
#                 print("Can't find last page due to class not being 'page-item last'")

#                 #Find the total pages by accessing 2nd to last button in pages class
#                 try:
#                     lastButton = soup.find_all(class_='pages')
#                     length = len(lastButton)
#                     lastPage = lastButton[length - 2].text
#                     lastPage = int(lastPage)
#                     return lastPage
#                 except Exception:
#                     print("Can't find last page due to class not being 'pages'")

#                     #Find the total pages by accessing the 3rd to last button in be-pager class
#                     try:
#                         lastButton = soup.find_all(class_='be-pager')
#                         length = len(lastButton)
#                         lastPage = lastButton[length - 3].text
#                         lastPage = int(lastPage)
#                         return lastPage
#                     except Exception:
#                         print("Can't find last page due to class not being 'page-item last'")

#                         #Only one page so ignore buttons
#                         try:
#                             return None
#                         except Exception:
#                             print("Error")

# with open("videoLinks.csv", 'w') as csv_file:
#         csv_writer = writer(csv_file)

#         url = 'https://space.bilibili.com/654295/video'
#         soup = make_soup(url)

        
#         lastButton = soup.find_all(class_='be-pager-total')
#         lastPage = lastButton[0].text
#         words = lastPage.split()
#         lastPage = int(words[1])
#         print(lastPage)
        
#         page = 1
#         pageExtension = ''

#         scrape_url(url)

#         while page < lastPage:
#             page = page + 1
            
#             pageExtension = '?page='+str(page)
#             print(url+pageExtension)
#             fullUrl = url+pageExtension
#             soup = make_soup(fullUrl)
#             scrape_url(fullUrl)
#         #driver.quit()

 #-------------------------------------------------------------------------------------------------#
 #Testing 3 for 2
# def make_driver(url):
#     DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"
#     driver = webdriver.Chrome(DRIVER_PATH)
#     driver.get(url)
#     return driver

# def make_soup(url): 
#     #response = requests.get(url)
#     soup = BeautifulSoup(make_driver(url).page_source, 'html.parser')
#     return soup

# def scrape_url(url):
#     i = 1
#     driver = make_driver(url)
    
#     try:
#         videoList = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "cover"))
#     )

#         videos = soup.find(class_='clearfix cube-list')
#         for videoLinks in videos.find_all('a', class_='cover'):
#             link = videoLinks['href'].replace('//','https://')
#             csv_writer.writerow([link])
#             print(i,'.',link)
#             i = i + 1

#     except:
#         driver.quit()

    
#         try :
#             videoList = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "img-anchor"))
#             )
#             for video in soup.find_all('a', class_='img-anchor'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#         except:
#             driver.quit()

# def find_last_page(url):
#     try:
#         lastButton = soup.find_all(class_='pagination-btn')
#         lastPage = lastButton[0].text
#         lastPage = int(lastPage)
#         return lastPage
#     except Exception:
#         print("Can't find last page due to class not being 'pagination-btn'")

#         try: 
#             lastButton = soup.find_all(class_='be-pager-total')
#             lastPage = lastButton[0].text
#             words = lastPage.split()
#             lastPage = int(words[1])
#             print(lastPage)
#         except Exception:
#             print("Can't find last page due to class not being 'be-pager-total'")

#             # Find the total number of pages
#             try:
#                 lastButton = soup.find_all(class_='')
#                 lastPage = lastButton[0].text

#                 lastPage = int(lastPage)
#                 return lastPage
#             except Exception:
#                 print("Can't find last page due to class not being 'page-item last'")

#                 #Find the total pages by accessing 2nd to last button in pages class
#                 try:
#                     lastButton = soup.find_all(class_='pages')
#                     length = len(lastButton)
#                     lastPage = lastButton[length - 2].text
#                     lastPage = int(lastPage)
#                     return lastPage
#                 except Exception:
#                     print("Can't find last page due to class not being 'pages'")

#                     #Find the total pages by accessing the 3rd to last button in be-pager class
#                     try:
#                         lastButton = soup.find_all(class_='be-pager')
#                         length = len(lastButton)
#                         lastPage = lastButton[length - 3].text
#                         lastPage = int(lastPage)
#                         return lastPage
#                     except Exception:
#                         print("Can't find last page due to class not being 'page-item last'")

#                         #Only one page so ignore buttons
#                         try:
#                             return None
#                         except Exception:
#                             print("Error")

# with open("videoLinks.csv", 'w') as csv_file:
#         csv_writer = writer(csv_file)

#         url = 'https://search.bilibili.com/all?keyword=%E3%82%A2%E3%83%8B%E3%82%B2%E3%83%A9%EF%BC%81%E3%83%87%E3%82%A3%E3%83%89%E3%82%A5%E3%83%BC%E3%83%BC%E3%83%B3&from_source=nav_search_new'
#         soup = make_soup(url)

        
#         lastButton = soup.find_all(class_='page-item last')
#         lastPage = int(lastButton[0].text)
#         print(lastPage)
        
#         page = 1
#         pageExtension = ''

#         scrape_url(url)

#         while page < lastPage:
#             page = page + 1
            
#             pageExtension = '?page='+str(page)
#             print(url+pageExtension)
#             fullUrl = url+pageExtension
#             soup = make_soup(fullUrl)
#             scrape_url(fullUrl)
#         #driver.quit()

#---------------------------------------------------------------------------------------------------------#

# Test 4

# def make_driver(url):
#     DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"
#     driver = webdriver.Chrome(DRIVER_PATH)
#     driver.get(url)
#     return driver

# def make_soup(url): 
#     #response = requests.get(url)
#     soup = BeautifulSoup(make_driver(url).page_source, 'html.parser')
#     return soup

# def scrape_url(url):
#     i = 1
#     driver = make_driver(url)
    
#     try:
#         videoList = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "cover"))
#     )
#         videos = soup.find(class_='clearfix cube-list')
#         for videoLinks in videos.find_all('a', class_='cover'):
#             link = videoLinks['href'].replace('//','https://')
#             csv_writer.writerow([link])
#             print(i,'.',link)
#             i = i + 1
#     except:
#         driver.quit()

#         try:
#             videoList = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "img-anchor"))
#             )
#             for video in soup.find_all('a', class_='img-anchor'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(i,'.',link)
#                 i = i + 1
#         except:
#             driver.quit()
    

# def find_last_page(url):
#     try:
#         lastButton = soup.find_all(class_='pagination-btn')
#         lastPage = lastButton[0].text
#         lastPage = int(lastPage)
#         return lastPage
#     except Exception:
#         print("Can't find last page due to class not being 'pagination-btn'")

#         try: 
#             lastButton = soup.find_all(class_='be-pager-total')
#             lastPage = lastButton[0].text
#             words = lastPage.split()
#             lastPage = int(words[1])
#             print(lastPage)
#         except Exception:
#             print("Can't find last page due to class not being 'be-pager-total'")

#             # Find the total number of pages
#             try:
#                 lastButton = soup.find_all(class_='')
#                 lastPage = lastButton[0].text

#                 lastPage = int(lastPage)
#                 return lastPage
#             except Exception:
#                 print("Can't find last page due to class not being 'page-item last'")

#                 #Find the total pages by accessing 2nd to last button in pages class
#                 try:
#                     buttonList = soup.find(class_='pages')
#                     lastButton = buttonList.find_all('li')
#                     length = len(lastButton)
#                     lastPage = int(lastButton[length - 2].text)
#                     return lastPage
#                 except Exception:
#                     print("Can't find last page due to class not being 'pages'")

#                     #Find the total pages by accessing the 3rd to last button in be-pager class
#                     try:
#                         lastButton = soup.find_all(class_='be-pager')
#                         length = len(lastButton)
#                         lastPage = lastButton[length - 3].text
#                         lastPage = int(lastPage)
#                         return lastPage
#                     except Exception:
#                         print("Can't find last page due to class not being 'page-item last'")

#                         #Only one page so ignore buttons
#                         try:
#                             return None
#                         except Exception:
#                             print("Error")

# with open("videoLinks.csv", 'w') as csv_file:
#         csv_writer = writer(csv_file)

#         url = 'https://search.bilibili.com/all?keyword=%E9%8A%80%E9%AD%82%E6%96%87%E5%AD%97%E8%B5%B7%E3%81%93%E3%81%97'
#         #url = input("URL: ")

#         soup = make_soup(url)
#         #driver = make_driver(url)
        

        
#         buttonList = soup.find(class_='pages')
#         lastButton = buttonList.find_all('li')
#         length = len(lastButton)
#         print(len(lastButton))
#         lastPage = int(lastButton[length - 2].text)
        
        
#         #lastPage = find_last_page(url)

#         print(lastPage)

#         page = 1
#         pageExtension = ''

#         scrape_url(url)

#         while page < lastPage:
#             page = page + 1
            
#             pageExtension = '&page='+str(page)
#             print(url+pageExtension)
#             fullUrl = url+pageExtension
#             soup = make_soup(fullUrl)
#             scrape_url(fullUrl)
#         #driver.quit()

#---------------------------------------------------------------------------------------------------------#
# ### Rewrite scrape and finding total page function


# # def make_driver(url):
# #     DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"
# #     driver = webdriver.Chrome(DRIVER_PATH)
# #     driver.get(url)
# #     return driver


# def make_soup(driver): 
#     #response = requests.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     return soup


# # TODO: Checking whether I need more or less driver.quit()
# def scrape_url(driver):
#     i = 1

#     try:
#         if soup.find_all('a', class_='img-anchor') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "img-anchor"))
#                 )
#             except:
#                 driver.quit()
            
#             for video in soup.find_all('a', class_='img-anchor'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1
        
#         elif soup.find_all('a', class_='cover cover-normal') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "cover cover-normal"))
#                 )
#             except:
#                 driver.quit()  

#             for video in soup.find_all('a', class_='cover cover-normal'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1

#         elif soup.find_all('a', class_='cover') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "cover"))
#                 )
#             except:
#                 driver.quit()

#             for video in soup.find_all('a', class_='cover'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1
#         else:
#             print("Error finding video urls")

#     except:
#         driver.quit()
#         print("Error finding video urls")
#         raise Exception


# #TODO: Reformat if and the try and except also google raise Exception
# def find_last_page(driver):
#     try:
        
#         if soup.find_all(class_='be-pager-total') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "be-pager-total"))
#                 )
#             except:
#                 driver.quit()  

#             lastButton = soup.find_all(class_='be-pager-total')
#             lastPage = lastButton[0].text
#             words = lastPage.split()
#             lastPage = int(words[1])
#             return lastPage

#         elif soup.find_all(class_='pages') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "pages"))
#                 )
#             except:
#                 driver.quit()

#             buttonList = soup.find(class_='pages')
#             lastButton = buttonList.find_all('li')
#             length = len(lastButton)
#             lastPage = int(lastButton[length - 2].text)
#             return lastPage

#         #TODO: Take a look over this one and make sure class search is right
#         elif soup.find_all("page-item last") != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "page-item last"))
#                 )
#             except:
#                 driver.quit()

#             lastButton = soup.find_all(class_='page-item last')
#             lastPage = lastButton[0].text
#             lastPage = int(lastPage)
#             return lastPage

#         elif soup.find_all("be-pager") != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "be-pager"))
#                 )
#             except:
#                 driver.quit()

#             lastButton = soup.find_all(class_='be-pager')
#             length = len(lastButton)
#             lastPage = lastButton[length - 3].text
#             lastPage = int(lastPage)
#             return lastPage

#         elif soup.find_all(class_='pagination-btn') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "pagination-btn"))
#                 )
#             except:
#                 driver.quit()
            
#             lastButton = soup.find_all(class_='pagination-btn')
#             lastPage = lastButton[0].text
#             lastPage = int(lastPage)
#             return lastPage

#         else:
#             print("Error finding video urls")

#     except:
#         print("Error: Can't get the last page")
#         raise Exception



# # TODO
# fileName = input("File Name: ")
# with open(fileName + ".csv", 'w') as csv_file:
#         csv_writer = writer(csv_file)

#         #url = 'https://search.bilibili.com/all?keyword=%E9%8A%80%E9%AD%82%E6%96%87%E5%AD%97%E8%B5%B7%E3%81%93%E3%81%97'
#         url = input("URL: ")
#         driver = make_driver(url)
#         soup = make_soup(driver)
        
        

        
#         # buttonList = soup.find(class_='pages')
#         # lastButton = buttonList.find_all('li')
#         # length = len(lastButton)
#         # print(len(lastButton))
#         # lastPage = int(lastButton[length - 2].text)
        
        
#         lastPage = find_last_page(driver)

#         print(lastPage)

#         page = 1
#         pageExtension = ''

#         scrape_url(driver)

#         while page < lastPage:
#             page = page + 1
            
#             pageExtension = '&page='+str(page)
#             print(url+pageExtension)
#             fullUrl = url+pageExtension
#             soup = make_soup(make_driver(fullUrl))
#             scrape_url(make_driver(fullUrl))

#         driver.quit()


#---------------------------------------------------------------------------------------------------------#
# # Final Version 1.0

# #TODO split user url and turn it into usable url(i.e.remove everything after '?' mark)
# #Sites with error: https://space.bilibili.com/654295/video?tid=0&page=1&keyword=&order=pubdate, https://space.bilibili.com/1726310?from=search&seid=12136548391520811086
# # Learn about try, except and raise

# def make_soup(driver): 
#     #response = requests.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     return soup


# def scrape_url(driver):
#     i = 1

#     try:
#         if soup.find_all('a', class_='img-anchor') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "img-anchor"))
#                 )
#             except:
#                 driver.quit()
            
#             for video in soup.find_all('a', class_='img-anchor'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1
        
#         #Tested with: https://space.bilibili.com/216970/channel/detail?cid=13214
#         elif soup.find_all('a', class_='cover cover-normal') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "cover cover-normal"))
#                 )
#             except:
#                 driver.quit()  

#             for video in soup.find_all('a', class_='cover cover-normal'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1

        

#         elif soup.find_all('a', class_='clearfix cube-list') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "cover"))
#                 )
#             except:
#                 driver.quit()

#             videos = soup.find(class_='clearfix cube-list')
#             for video in videos.find_all('a', class_='cover'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1

#         #Tested with: https://space.bilibili.com/1726310?from=search&seid=12136548391520811086
#         #Debate whether to also get links from 'album-top' class
#         #TODO find way to split url and remove everything after question mark
#         #TODO No longer works(link)?
#         elif soup.find_all('div', class_='small-item fakeDanmu-item') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "cover"))
#                 )
#             except:
#                 driver.quit()

#             videos = soup.find(class_='content clearfix')
#             for video in videos.find_all('a', class_='cover'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1
#         else:
#             print("Error finding video urls")

#     except:
#         driver.quit()
#         print("Error finding video urls")
#         raise Exception



# def find_last_page(driver):
#     try:
        
#         if soup.find_all(class_='be-pager-total') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "be-pager-total"))
#                 )
#             except:
#                 driver.quit()  

#             lastButton = soup.find_all(class_='be-pager-total')
#             lastPage = lastButton[0].text
#             words = lastPage.split()
#             lastPage = int(words[1])
#             return lastPage

#         elif soup.find_all(class_='pages') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "pages"))
#                 )
#             except:
#                 driver.quit()

#             buttonList = soup.find(class_='pages')
#             lastButton = buttonList.find_all('li')
#             length = len(lastButton)
#             lastPage = int(lastButton[length - 2].text)
#             return lastPage


#         elif soup.find_all("page-item last") != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "page-item last"))
#                 )
#             except:
#                 driver.quit()

#             lastButton = soup.find_all(class_='page-item last')
#             lastPage = lastButton[0].text
#             lastPage = int(lastPage)
#             return lastPage

#         #Tested with: https://space.bilibili.com/216970/channel/detail?cid=13214
#         elif soup.find_all("be-pager") != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "be-pager"))
#                 )
#             except:
#                 driver.quit()

#             lastButton = soup.find_all(class_='be-pager')
#             length = len(lastButton)
#             lastPage = lastButton[length - 3].text
#             lastPage = int(lastPage)
#             return lastPage

#         elif soup.find_all(class_='pagination-btn') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "pagination-btn"))
#                 )
#             except:
#                 driver.quit()
            
#             lastButton = soup.find_all(class_='pagination-btn')
#             lastPage = lastButton[0].text
#             lastPage = int(lastPage)
#             return lastPage

#         #Tested with: https://space.bilibili.com/1726310?from=search&seid=12136548391520811086
#         else:
#             print("Can't find total pages")
#             lastPage = 0
#             return lastPage

#     except:
#         print("Error: Can't get the last page")
#         raise Exception

# def dir_path(userPath):
#     ''.' '.join(userPath)
#     if os.path.isdir(userPath):
#         return userPath
#     else:
#         os.mkdir(userPath)
#         return userPath


# try: 
#     #TODO 
#     #try catch PermissionError 
#     #Catch invalid urls
#     #allow save location & default location

#     defaultPath = pathlib.Path().absolute()
#     print("Default Save Location:", defaultPath, "\n")
#     parser = argparse.ArgumentParser(prog='biliurls')

#     # Arguments
#     parser.add_argument('-p', '--path',
#                         type=dir_path
#                         metavar='',
#                         nargs='+',

#                         help="Absolute save path")

#     parser.add_argument('-n', '--name',
#                         type=str,
#                         metavar='',
#                         default='output',
#                         help="Name of the csv file")

#     parser.add_argument('-d', '--driver',
#                         type=str,
#                         metavar='',
#                         default=defaultPath,
#                         help="Absolute web driver path")
    
#     # parser.add_argument('-h', '--help',
#     #                     help="Absolute web driver path")

#     parser.add_argument('-l', '--link',
#                         type=str,
#                         metavar='',
#                         required=True,
#                         help="Link to extract video urls")
    
#     parser.add_argument('-v', '--verbose',
#                         action='store_true',
#                         help="Show more information as the command executes")

#     args = parser.parse_args()
#     ' '.join(args.path)
#     print(args.path)
#     if args.path is not None:
#         try:
#             os.mkdir(str(args.path))
#             print(args.path)
#         except OSError as e:
#             print("Directory exists no need to create directory\n")

#     INVALID_CHARACTERS_RE =  re.compile(r"^[^<>/{}[\]~`]*$")
#     if INVALID_CHARACTERS_RE.match(args.name):
#         defaultFile = os.path.abspath(str(args.path)+ "\\" + str(args.name)) 
#         print(defaultFile)
#     else:
#         print("Illegal characters detected in file name")
#         exit()
        


            
#     # defaultPath = pathlib.Path().absolute()
#     # print("Default Save Location:", defaultPath, "\n")
#     # userPreference = input("Would you like to set csv save location rather than using the default location?(Y/N): ")

#     # if userPreference == 'Y' or userPreference == 'y' or userPreference == 'yes' or userPreference == 'Yes':
#     #     saveLocation = input("Input absolute path: ")
#     # else:
#     #     saveLocation = ''
#     # if saveLocation.find('/') < 0:
#     #     saveLocation = os.path.abspath(saveLocation)

#     # try:
#     #     os.mkdir(saveLocation)
#     # except OSError as e:
#     #     print("Directory exists no need to create directory\n")


#     # fileName = input("File Name: ")
#     # if userPreference == 'Y' or userPreference == 'y' or userPreference == 'yes' or userPreference == 'Yes':
#     #     defaultFile = saveLocation +"\\" + fileName
#     #     print('Saving to:', defaultFile, "\n")
#     # else:
#     #     defaultFile = fileName
#     #     print('Saving to:', str(defaultPath) + "\\" + str(defaultFile), "\n")
#     print("space")
#     print(defaultPath)
#     print("space")
#     print(defaultFile)
#     with open(defaultFile + ".csv", 'w', newline='') as csv_file:
#             csv_writer = writer(csv_file)

#             #url = input("URL: ")

#             DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"
#             driver = webdriver.Chrome(DRIVER_PATH)
#             driver.get(args.link)

#             soup = make_soup(driver)

#             lastPage = find_last_page(driver)

#             print("Total Pages: " + str(lastPage))
#             page = 1
#             pageExtension = ''
#             print("\n" + 'Page:',1)
#             if args.link.find('channel') == -1 and lastPage > 1:  
#                 scrape_url(driver)
#                 while page < lastPage:
#                     page = page + 1
                    
#                     if soup.find_all(class_='h-inner') != []:
#                         pageExtension = '?page='+str(page)
#                         print(args.link+pageExtension)
#                     else:
#                         pageExtension = '&page='+str(page)
#                         print(args.link+pageExtension)
                    
#                     # pageExtension = '?page='+str(page)

#                     fullUrl = args.link+pageExtension
#                     driver.get(fullUrl)
#                     soup = make_soup(driver)
#                     scrape_url(driver)

#             # In the event that the webpage is a single page application
#             else:     
#                 try:
#                     i = 1
#                     h = 1 
#                     print("\n" + 'Page:',1)
#                     # Loops through all video urls through all pages    
#                     while i <= lastPage:                                 
#                         for video in soup.find_all('a', class_='cover cover-normal'):    
#                             link = video['href'].replace('//','https://')
#                             csv_writer.writerow([link])
#                             print(str(h)+'.' + link)
#                             h = h + 1
#                         if i < lastPage:
#                             driver.find_element_by_class_name('be-pager-next').click()
#                             print("\n" + 'Page:',i + 1)
#                             #TODO Find a better way than using sleep
#                             time.sleep(2)
#                         i = i + 1
#                         soup = make_soup(driver)
#                     print("\n" + 'Extracted:',h-1 ,'URLS')           
#                 except:
#                     raise Exception

#             # Close all windows
#             driver.quit()
# except KeyboardInterrupt as ke:
#     print('User cancelled the operation')


#---------------------------------------------------------------------------------------------------------------------------#

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



#---------------------------------------------------------------------------------------------------------------------------#

# Final Version 2.5

#TODO split user url and turn it into usable url(i.e.remove everything after '?' mark)
#Sites with error: https://space.bilibili.com/654295/video?tid=0&page=1&keyword=&order=pubdate, https://space.bilibili.com/1726310?from=search&seid=12136548391520811086
# Learn about try, except and raise
# chrome driver needs to be on PATH, therefore test if setting PATH to parent folder affects child

# def make_soup(driver): 
#     #response = requests.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     return soup


# def scrape_url(driver):
#     i = 1

#     try:
#         if soup.find_all('a', class_='img-anchor') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "img-anchor"))
#                 )
#             except:
#                 driver.quit()
            
#             for video in soup.find_all('a', class_='img-anchor'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1
        
#         #Tested with: https://space.bilibili.com/216970/channel/detail?cid=13214
#         elif soup.find_all('a', class_='cover cover-normal') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "cover cover-normal"))
#                 )
#             except:
#                 driver.quit()  

#             for video in soup.find_all('a', class_='cover cover-normal'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1

        

#         elif soup.find_all('a', class_='clearfix cube-list') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "cover"))
#                 )
#             except:
#                 driver.quit()

#             videos = soup.find(class_='clearfix cube-list')
#             for video in videos.find_all('a', class_='cover'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1

#         #Tested with: https://space.bilibili.com/1726310?from=search&seid=12136548391520811086
#         #Debate whether to also get links from 'album-top' class
#         #TODO find way to split url and remove everything after question mark
#         #TODO No longer works(link)?
#         elif soup.find_all('div', class_='small-item fakeDanmu-item') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "cover"))
#                 )
#             except:
#                 driver.quit()

#             videos = soup.find(class_='content clearfix')
#             for video in videos.find_all('a', class_='cover'):
#                 link = video['href'].replace('//','https://')
#                 csv_writer.writerow([link])
#                 print(str(i)+'.' + link)
#                 i = i + 1
#         else:
#             print("Error finding video urls")

#     except:
#         driver.quit()
#         print("Error finding video urls")
#         raise Exception



# def find_last_page(driver):
#     try:
        
#         if soup.find_all(class_='be-pager-total') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "be-pager-total"))
#                 )
#             except:
#                 driver.quit()  

#             lastButton = soup.find_all(class_='be-pager-total')
#             lastPage = lastButton[0].text
#             words = lastPage.split()
#             lastPage = int(words[1])
#             return lastPage

#         elif soup.find_all(class_='pages') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "pages"))
#                 )
#             except:
#                 driver.quit()

#             buttonList = soup.find(class_='pages')
#             lastButton = buttonList.find_all('li')
#             length = len(lastButton)
#             lastPage = int(lastButton[length - 2].text)
#             return lastPage


#         elif soup.find_all("page-item last") != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "page-item last"))
#                 )
#             except:
#                 driver.quit()

#             lastButton = soup.find_all(class_='page-item last')
#             lastPage = lastButton[0].text
#             lastPage = int(lastPage)
#             return lastPage

#         #Tested with: https://space.bilibili.com/216970/channel/detail?cid=13214
#         elif soup.find_all("be-pager") != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "be-pager"))
#                 )
#             except:
#                 driver.quit()

#             lastButton = soup.find_all(class_='be-pager')
#             length = len(lastButton)
#             lastPage = lastButton[length - 3].text
#             lastPage = int(lastPage)
#             return lastPage

#         elif soup.find_all(class_='pagination-btn') != []:
#             try: 
#                 videoList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "pagination-btn"))
#                 )
#             except:
#                 driver.quit()
            
#             lastButton = soup.find_all(class_='pagination-btn')
#             lastPage = lastButton[0].text
#             lastPage = int(lastPage)
#             return lastPage

#         #Tested with: https://space.bilibili.com/1726310?from=search&seid=12136548391520811086
#         else:
#             print("Can't find total pages")
#             lastPage = 0
#             return lastPage

#     except:
#         print("Error: Can't get the last page")
#         raise Exception


# try: 
#     #TODO 
#     #try catch PermissionError 
#     #Catch invalid urls
#     #allow save location & default location

#     defaultPath = pathlib.Path().absolute()
#     print("Default Save Location:", defaultPath, "\n")
#     parser = argparse.ArgumentParser(prog='biliurls')

#     # Arguments
#     parser.add_argument('-n', '--name',
#                         type=str,
#                         metavar='',
#                         default='output',
#                         help="Name of the csv file")

#     parser.add_argument('-l', '--link',
#                         type=str,
#                         metavar='',
#                         required=True,
#                         help="Link to extract video urls")

#     parser.add_argument('-w', '--wait',
#                         type=int,
#                         metavar='',
#                         help="The amount of second to stop and wait for browser to load. Recommended for use only if browser is taking longer than 2 seconds to load. Prevent links from being extracted on same page as the next page has yet to load.")                    
    
#     parser.add_argument('-v', '--verbose',
#                         action='store_true',
#                         help="Show more information as the command executes")

#     args = parser.parse_args()
    

#     INVALID_CHARACTERS_RE =  re.compile(r"^[^<>/{}[\]~`]*$")
#     if INVALID_CHARACTERS_RE.match(args.name):
#         defaultFile = os.path.abspath(str(defaultPath) + "\\" + str(args.name)) 
#         print(defaultFile)
#     else:
#         print("Illegal characters detected in file name")
#         exit()
        


            
#     # defaultPath = pathlib.Path().absolute()
#     # print("Default Save Location:", defaultPath, "\n")
#     # userPreference = input("Would you like to set csv save location rather than using the default location?(Y/N): ")

#     # if userPreference == 'Y' or userPreference == 'y' or userPreference == 'yes' or userPreference == 'Yes':
#     #     saveLocation = input("Input absolute path: ")
#     # else:
#     #     saveLocation = ''
#     # if saveLocation.find('/') < 0:
#     #     saveLocation = os.path.abspath(saveLocation)

#     # try:
#     #     os.mkdir(saveLocation)
#     # except OSError as e:
#     #     print("Directory exists no need to create directory\n")


#     # fileName = input("File Name: ")
#     # if userPreference == 'Y' or userPreference == 'y' or userPreference == 'yes' or userPreference == 'Yes':
#     #     defaultFile = saveLocation +"\\" + fileName
#     #     print('Saving to:', defaultFile, "\n")
#     # else:
#     #     defaultFile = fileName
#     #     print('Saving to:', str(defaultPath) + "\\" + str(defaultFile), "\n")
#     with open(defaultFile + ".csv", 'w', newline='') as csv_file:
#             csv_writer = writer(csv_file)

#             #url = input("URL: ")

#             DRIVER_PATH = r"C:\Users\samph\AppData\Local\Programs\Python\Python37-32\Python Files\WebScraping\chromedriver.exe"
#             print(os.path.abspath(str(defaultPath) + "\\chromedriver.exe"))
#             driver = webdriver.Chrome(os.path.abspath(str(defaultPath) + r"\\WebScraping\chromedriver.exe"))
#             driver.get(args.link)

#             soup = make_soup(driver)

#             lastPage = find_last_page(driver)

#             print("Total Pages: " + str(lastPage))
#             page = 1
#             pageExtension = ''
#             print("\n" + 'Page:',1)
#             if args.link.find('channel') == -1 and lastPage > 1:  
#                 scrape_url(driver)
#                 while page < lastPage:
#                     page = page + 1
                    
#                     if soup.find_all(class_='h-inner') != []:
#                         pageExtension = '?page='+str(page)
#                         print(args.link+pageExtension)
#                     else:
#                         pageExtension = '&page='+str(page)
#                         print(args.link+pageExtension)
                    
#                     # pageExtension = '?page='+str(page)

#                     fullUrl = args.link+pageExtension
#                     driver.get(fullUrl)
#                     soup = make_soup(driver)
#                     scrape_url(driver)

#             # In the event that the webpage is a single page application
#             else:     
#                 try:
#                     i = 1
#                     h = 1 
#                     print("\n" + 'Page:',1)
#                     # Loops through all video urls through all pages    
#                     while i <= lastPage:
#                         try: 
#                             videoList = WebDriverWait(driver, 10).until(
#                             EC.presence_of_element_located((By.CLASS_NAME, "cover cover-normal"))
#                             )
#                             for video in soup.find_all('a', class_='cover cover-normal'):    
#                                 link = video['href'].replace('//','https://')
#                                 csv_writer.writerow([link])
#                                 print(str(h)+'.' + link)
#                             h = h + 1
#                             if i < lastPage:
#                                 driver.find_element_by_class_name('be-pager-next').click()
#                                 print("\n" + 'Page:',i + 1)
#                                 #TODO Find a better way than using sleep
#                                 #time.sleep(args.wait)
#                         except:
#                             driver.quit()                                 
                        
#                         i = i + 1
#                         soup = make_soup(driver)
#                     print("\n" + 'Extracted:',h-1 ,'URLS')           
#                 except:
#                     raise Exception

#             # Close all windows
#             driver.quit()
# except KeyboardInterrupt as ke:
#     print('User cancelled the operation')

