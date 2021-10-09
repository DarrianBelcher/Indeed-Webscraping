# Indeed-Webscraping

## Description
Web scraping Python project that extracts the first page of internship opportinities within 25 miles of Hampton, Virginia, that were posted in the last 24 hours. The internship descriptions including internship title, company name, job description, job location, and company Information link are then written to individual company text files.

The website link: 
<br>
```htmlText = requests.get("https://www.indeed.com/jobs?q=intern&l=hampton&fromage=1&vjk=d6866bece2cc7d55").text ``` 
<br>
can be swaped and customized using Indeed to change the parameters of the internship search (job location radius, etc)

## Requirements
* Install **Beautiful Soup** and **Requests** libraries
* Create a Folder titled "Internships" to store individual company internship descriptions 

## Sample File Output
### File Name: "TowneBank Internship.txt"


Job Title: Intern - Information Technology 
<br>
Company Name: TowneBank 
<br>
Company Information Link: https://www.indeed.com/cmp/Townebank 
<br>
Job Location: Suffolk, VA 23435 
<br>
Short Description: Some of the specific areas hosting interns are Information Security, Network Engineering and Administration, Deployment, Business Continuity Planning, User… 
