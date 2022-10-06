import time
import csv
from webbrowser import BaseBrowser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


starturl="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(starturl)
time.sleep(10)

def scrape():
     headers=["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
     planetData=[]
     for i in range(0,207):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul in soup.find_all("ul",attrs={"class","exoplanet"}):
            litags=ul.find_all("li")
            templist=[]
            for i,li in enumerate(litags):
                if  i==0:
                    templist.append(li.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(li.contents[0])
                    except:
                        templist.append("")
            planetData.append(templist)
        print(f"page {i} done")
        browser.find_element(By.XPATH,value="/html/body/div[2]/div/div[3]/section[2]/div/section[2]/div/div/article/div/div[2]/footer/div/div/div/nav/span[2]/a").click()
     with open("class127.csv","w") as Z:
        writer=csv.writer(Z)
        writer.writerow(headers)
        writer.writerows(planetData)
scrape()

