# Date: 10/08/21
# Description: Web scraping project that searches indeed and extracts the first page of internship opportinities within 25 miles of Hampton, Virginia, that were posted in the last 24 hours. The internship descriptions are them written to individual company text files.  

import requests
from bs4 import BeautifulSoup

htmlText = requests.get("https://www.indeed.com/jobs?q=intern&l=hampton&fromage=1&vjk=d6866bece2cc7d55").text 

soup = BeautifulSoup(htmlText, "lxml")

jobListings = soup.find_all("div", class_="slider_item") # searches for individual indeed job cards that are divided by div tags, creates list containing each job card's HTML

for index, jobListing in enumerate(jobListings):
    jobTitleBlock = jobListing.find('h2') #there are two span tags in the block, title needed from second block

    jobTitle = jobTitleBlock.find_next("span").text #Extracts title from title block 

    companyName = jobListing.find("span",class_="companyName").text #Extracts company name from job card

    jobLocation = jobListing.find("div", class_="companyLocation").text #Extracts job location from job card

    companyInfo = "https://www.indeed.com" + jobListing.a['href'] # Extracts ending of company profile link, concatonates it to https://indeed.com to create a functional link

    descriptionSummary = jobListing.find("li").text # Extracts short job description from job card 

# Writes each job description to a unique file under a folder named "Internships" (Internships file needs to be created in the same diirectory as the pyhon file before running)
    with open(f"Internships/{companyName} Insernship.txt", "w") as f:
        f.write(f"Job Title: {jobTitle} \n")
        f.write(f"Company Name: {companyName} \n")
        f.write(f"Company Information Link: {companyInfo} \n")
        f.write(f"Job Location: {jobLocation} \n")
        f.write(f"Short Description: {descriptionSummary} \n")
