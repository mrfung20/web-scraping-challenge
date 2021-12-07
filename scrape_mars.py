#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser


# In[2]:


executable_path = {"executable_path": "/Users/rogeralbarran/Downloads/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


# visit the NASA Mars News site and scrape headlines
nasa_url = 'https://mars.nasa.gov/news/'
browser.visit(nasa_url)
time.sleep(1)
nasa_html = browser.html
nasa_soup = BeautifulSoup(nasa_html, 'html.parser')

news_list = nasa_soup.find('ul', class_='item_list')
first_item = news_list.find('li', class_='slide')
nasa_headline = first_item.find('div', class_='content_title').text
nasa_teaser = first_item.find('div', class_='article_teaser_body').text
print(nasa_headline)


# In[4]:


# visit the JPL website and scrape the featured image
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)
time.sleep(1)
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(1)
expand = browser.find_by_css('a.fancybox-expand')
expand.click()
time.sleep(1)

jpl_html = browser.html
jpl_soup = BeautifulSoup(jpl_html, 'html.parser')

img_relative = jpl_soup.find('img', class_='fancybox-image')['src']
image_path = f'https://www.jpl.nasa.gov{img_relative}'
print(image_path)


# In[5]:


# visit the mars weather report twitter and scrape the latest tweet
mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(mars_weather_url)
time.sleep(1)
mars_weather_html = browser.html
mars_weather_soup = BeautifulSoup(mars_weather_html, 'html.parser')

tweets = mars_weather_soup.find('ol', class_='stream-items')
mars_weather = tweets.find('p', class_="tweet-text").text
print(mars_weather)


# In[13]:


# Visit Mars facts url 
facts_url = 'http://space-facts.com/mars/'

# Use Panda's `read_html` to parse the url
mars_facts = pd.read_html(facts_url)

# Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
mars_df = mars_facts[0]

# Assign the columns `['Description','Value']`
mars_df.columns = ['Description','Value']

# Save html code to folder Assets
mars_df.to_html()

data = mars_df.to_dict(orient='records')  # Here's our added param..

# Display mars_df
mars_df


# In[14]:


# scrape images of Mars' hemispheres from the USGS site
mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
hemi_dicts = []

for i in range(1,9,2):
    hemi_dict = {}
    
    browser.visit(mars_hemisphere_url)
    time.sleep(1)
    hemispheres_html = browser.html
    hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')
    hemi_name_links = hemispheres_soup.find_all('a', class_='product-item')
    hemi_name = hemi_name_links[i].text.strip('Enhanced')
    
    detail_links = browser.find_by_css('a.product-item')
    detail_links[i].click()
    time.sleep(1)
    browser.find_link_by_text('Sample').first.click()
    time.sleep(1)
    browser.windows.current = browser.windows[-1]
    hemi_img_html = browser.html
    browser.windows.current = browser.windows[0]
    browser.windows[-1].close()
    
    hemi_img_soup = BeautifulSoup(hemi_img_html, 'html.parser')
    hemi_img_path = hemi_img_soup.find('img')['src']

    print(hemi_name)
    hemi_dict['title'] = hemi_name.strip()
    
    print(hemi_img_path)
    hemi_dict['img_url'] = hemi_img_path

    hemi_dicts.append(hemi_dict)


# In[ ]:




