from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By
import requests

starturl="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("/Users/naman/Desktop/chromedriver")
browser.get(starturl)
time.sleep(10)

headers=["name",
"Distance",
"Mass",
"Radius"]
final_starts_data=[]

def scrape():
    for i in range(1,5):
        while True:
            time.sleep(2)
            soup=BeautifulSoup(browser.page_source,"html.parcel")
            for ul_tags in soup.find_all("ul",attrs={"class","brightest_stars"})
                    for j in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=j.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            
            hyperlink_litag=li_tags[0]
            temp_list.append("wiki/List_of_brightest_stars_and_other_record_stars"+hyperlink_litag.find_all("a",href=True)[0]["href"])

            planet_data.append(temp_list)
    
         browser.find_element_by_xpath('').click()


with open("final.csv","w") as f:
    data_writer=csv.writer(f)
    data_writer.writerow(headers)
    data_writer.writerows(final_stars_data)


           