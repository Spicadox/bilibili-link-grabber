# bilibili-video-scraper
## Testing
### Overview
This is a simple script that scrapes all the video urls from certain [BiliBili](https://www.bilibili.com/) pages. Currently it is able to scrape all video links from search result pages, user's 投稿(submissions) pages, and user's 频道 (channel) pages. Rather than right clicking each video in order to obtain its url, this script is designed to allow users to obtain all the video urls from each page and writing all of that into a csv file. The csv file can be used by [annie](https://github.com/iawia002/annie) or [youtube-dl](https://github.com/ytdl-org/youtube-dl)(not recommended as youtube-dl doesn't download all parts of the video) to download every single video with the given url in the csv file.

### Installation
This script requires non-standard modules: [requests](https://pypi.org/project/requests/), [BeautifulSoup](https://pypi.org/project/beautifulsoup4/), and [Selenium](https://pypi.org/project/selenium/). [ChromeDriver](https://chromedriver.chromium.org/) is also required to work with Selenium, and ensure you're downloading the version that matches your Chrome build. A requirements text file will be included and the command `pip install -r requirements.txt` can be used to install the required modules. Note it is recommended that pip is installed and/or up to date. 

### Arguments and Usage
TBD
