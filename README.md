# bilibili-link-grabber
## Testing/Work in Progress
### Overview
This is a simple script that scrapes all the video urls from certain [BiliBili](https://www.bilibili.com/) pages. Currently it is able to scrape all video links from search result pages, user's 投稿(submissions) pages, and user's 频道 (channel) pages. Rather than right clicking each video in order to obtain its url, this script is designed to allow users to obtain all the video urls from each page and writing all of that into a csv file. The csv file can be used by [annie](https://github.com/iawia002/annie) or [youtube-dl](https://github.com/ytdl-org/youtube-dl)(not recommended as youtube-dl doesn't download all parts of the video) to download every single video with the given url in the csv file.

---
### Installation
Requires/recommended [Python](https://www.python.org/downloads/) version 3.7+

This script requires non-standard modules: [requests](https://pypi.org/project/requests/), [BeautifulSoup](https://pypi.org/project/beautifulsoup4/), and [Selenium](https://pypi.org/project/selenium/). [ChromeDriver](https://chromedriver.chromium.org/) is also required to work with Selenium, and ensure you're downloading the version that matches your Chrome build. A requirements text file will be included and the command `pip3 install -r requirements.txt` (or `pip`)can be used to install the required modules. Note it is recommended that pip is installed and/or up to date. It is also recommended that the ChromeDriver is installed and placed in the same folder as this script as there would be no need to specify the driver path later on. It should be noted that the default ouput for the csv file will be in the same folder as this script.

The executable file in the repository is a basic demo version of the current link scraper script. This executable file does not involve command line arugments, thus making it easier to use. The file is temporary and will probably be removed after a little more progress on the link scraper script.

 ---
 
### Options and Usages
TBD
```
python bilibiliVideoScraping.pu [OPTIONS] -l [URL]

python bilibiliVideoScraping.py -h

  -h, --help         show this help message and exit
  -n, --name         Name of the csv file
  -d, --driver       Absolute web driver path
  -p, --path         The user's chosen absolute path for the csv file 
  -l, --link         Link to extract video urls
  -w, --wait         The amount of second to stop and wait for browser to load. Recommended for use only if browser
                        is taking longer than 2 seconds to load. Prevent links from being extracted on same page as
                        the next page has yet to load.
  -q, --quiet       Limit the information printed onto the console as the script executes
 ```
 Example:`python bilibiliVideoScraping.py -l <Bilibili Link>`
 
 ---
 ### This script is intended to be used on the following BiliBili pages: 
 
 BiliBili search pages
 <p align="left">
  <kbd>
   <img src= "https://github.com/AnimeSam/bilibili-link-grabber/blob/master/images/search_page.png" width="800" height="1000">
  </kbd>
 </p>
 
 
 User's 投稿(submissions) pages and with the 全部(all) filter
 <p align="left">
  <kbd>
   <img src= "https://github.com/AnimeSam/bilibili-link-grabber/blob/master/images/submission_section.png" width="900" height="750" img align="right">
  </kbd>
 </p>
 
 
 User's 频道 (channel) pages which in most cases are single page application(meaning url doesn't change no matter which page you're on)
 <p align="left">
  <kbd>
   <img src= "https://github.com/AnimeSam/bilibili-link-grabber/blob/master/images/channel_section.png" width="1000" height="500" img align="right">
  </kbd>
 </p>
 
---
 
### About Me
As a data hoarder, anime enthusiast, and a self proclaim Japanophile, I needed a way to get all the video links from certain BiliBili pages in order to download it. Normally I would google a software or program that would allow me to do just that, but as a student studying in Computer Science(with a concentration in Software Engineer), I felt it was time to create and work on a project. I decided to work on the script using Python due to the fact that I wanted to practice and learn more about Python. I had fun learning about web scraping and enjoyed working on this script! Any tips or feedback on this script is much appreciated as I am sure there can be *much* improvement to be done! 
