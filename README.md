# bilibili-link-scraper
## Testing
### Overview
This is a simple script that scrapes all the video urls from certain [BiliBili](https://www.bilibili.com/) pages. Currently it is able to scrape all video links from search result pages, user's 投稿(submissions) pages, and user's 频道 (channel) pages. Rather than right clicking each video in order to obtain its url, this script is designed to allow users to obtain all the video urls from each page and writing all of that into a csv file. The csv file can be used by [annie](https://github.com/iawia002/annie) or [youtube-dl](https://github.com/ytdl-org/youtube-dl)(not recommended as youtube-dl doesn't download all parts of the video) to download every single video with the given url in the csv file.

### Installation
Requires/recommended [Python](https://www.python.org/downloads/) version 3.7+

This script requires non-standard modules: [requests](https://pypi.org/project/requests/), [BeautifulSoup](https://pypi.org/project/beautifulsoup4/), and [Selenium](https://pypi.org/project/selenium/). [ChromeDriver](https://chromedriver.chromium.org/) is also required to work with Selenium, and ensure you're downloading the version that matches your Chrome build. A requirements text file will be included and the command `pip3 install -r requirements.txt` (or `pip`)can be used to install the required modules. Note it is recommended that pip is installed and/or up to date. 

### Options and Usages
TBD
```
python bilibiliVideoScraping.pu [OPTIONS] -l [URL]

python bilibiliVideoScraping.py -h

  -h, --help          show this help message and exit
  -n, --name          Name of the csv file
  -d, --driver        Absolute web driver path
  -p, --path          The user's chosen absolute path for the csv file 
  -l , --link         Link to extract video urls
  -w , --wait         The amount of second to stop and wait for browser to load. Recommended for use only if browser
                        is taking longer than 2 seconds to load. Prevent links from being extracted on same page as
                        the next page has yet to load.
  -v, --verbose       Show more information as the command executes
 ```
 Example:`python bilibiliVideoScraping.py -l <Bilibili Link>`
