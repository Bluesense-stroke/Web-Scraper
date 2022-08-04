from distutils.log import info
from  bs4 import BeautifulSoup 
import requests
import time
import pandas as pd 


#unfamliar_skills = input("Enter the unfamiliar skills > ")

def scraping():


    global cp,skill,info
    cp=[]
    skill=[]
    info=[]

    for i in range(1,10):
        #extracting the html text from the target website 
        html_text = requests.get(f"https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence={1}&startPage=1").text
        #creating the instance for the beautiful soup 
        soup = BeautifulSoup(html_text,'lxml')
        #find the list of jobs in a page  
        jobs = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
        
        
        for job in jobs:
            publishdate = job.find('span',class_ = "sim-posted").span.text
            if "few" in publishdate :
                # finding the particular company name in the page of job
                company_name = job.find('h3',class_ = "joblist-comp-name").text.replace(" ",'').strip()
                #sorting the filter for the jobs 
                skills = job.find('span',class_ = "srp-skills").text.replace(" ",'').strip()
                #getting the link from the inspect
                more_info = job.header.h2.a['href']
            
                cp.append(company_name)
                skill.append(skills)
                info.append(more_info)
                    

            else:
                pass

if __name__ == '__main__':
    
    scraping()
    #print(cp)
    
    df = pd.DataFrame({"Company Name ": cp , "Skills": skill , "More info ": info})
    df.to_excel("./data.xlsx")

