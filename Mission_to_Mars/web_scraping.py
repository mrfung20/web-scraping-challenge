from splinter import Browser
from bs4 import BeautifulSoup 
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def web_scraping():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'http://redplanetscience.com/#'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_='content_title')
    summaries = soup.find_all('div', class_='article_teaser_body')

    titles_list = []
    summaries_list = []

    # Iterate through each article
    for x in range(1):
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        title = titles[x].text.strip()
        titles_list.append(title)
        
    for x in range(1):
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        summary = summaries[x].text.strip()
        summaries_list.append(summary)

    titles_and_summaries = zip(titles_list, summaries_list)

    try:
            browser.links.find_by_partial_text('next').click()
    except:
            print("Scraping Complete")

    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    tables = pd.read_html(url)

    df = tables[0]
    df.head()
    df.rename(columns={0:'',1:"Mars",2:"Earth"},inplace='True')
    df.head()
    df.loc[-1] = ['Description','','']
    df.index = df.index + 1
    df = df.sort_index()

    html_table = df.to_html()
    html_table = html_table.replace('\n', '')

    df.to_html('table.html')

    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    fancy_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
    
    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    img__links_list=[]
    img_titles_list=[]

    titles = soup.find_all('div', class_='description')
    links = soup.find_all('img', class_='thumb')

    for link in links:
        image_link = link['src']
        image_full_link = f"https://marshemispheres.com/{image_link}"
        img__links_list.append(image_full_link)
        

    for title in titles:
        a = title.find('a')
        image_title = a.find('h3').text.strip()
        img_titles_list.append(image_title)
    try:
            browser.links.find_by_partial_text('next').click()
            
    except:
            print("Scraping Complete")

    images_dict = []
    for x in range(0,4):
        images_dict.append({"title":img_titles_list[x],"img_url":img__links_list[x]})
    
    browser.quit()

  
    mars_data = {"news_title":titles_list,"news_summary":summaries_list,"featured_image":fancy_image_url,"hemi_table":images_dict}
    
    return(mars_data)

