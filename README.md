#### Excel-Project-through-Python-Scripting
# School & College Contact Data Scraper (Delhi, Gurgaon, Noida)

## 📌 Project Overview
This project is a **Python-based web scraping automation tool** designed to collect publicly available contact information of **schools and colleges** located in **Delhi, Gurgaon, and Noida**.

The script extracts:
- Institution name
- City
- Official website
- Email IDs available on the website
- Contact phone numbers

All collected data is **automatically structured and exported into an Excel file**, making it easy for further analysis or reporting.

---

## 🎯 Problem Statement
Manually collecting contact details for **300+ educational institutions** is time-consuming and error-prone.  
To solve this, Python scripting is used to **automate data collection**, ensuring:
- Faster execution
- Consistent formatting
- Reduced human error
- Easy scalability

---

## 🛠️ Technologies & Libraries Used
- **Python 3**
- `requests` – for fetching website content
- `BeautifulSoup (bs4)` – for parsing HTML
- `re` – for extracting email IDs and phone numbers using regular expressions
- `pandas` – for structuring data
- `openpyxl` – for exporting data to Excel

---

## 📂 Project Structure
```
├── schools.csv # Input file containing institution names & cities
├── scraper.py # Main Python script
├── School_Contacts.xlsx # Output Excel file (generated)
├── README.md # Project documentation
```

---

## 📥 Input Format (`schools.csv`)
The input file should contain the list of schools/colleges.

Example:
```csv
name,city,website,email id, contact no
Delhi Public School RK Puram,Delhi,https://dpsrkp.net
Amity International School,Noida,https://www.amity.edu
```
If the website is unavailable, it can be left blank and marked as “Not Available” in the output.

---
# ⚙️ How the Script Works

1.Reads institution details from schools.csv

2. Sends HTTP requests to official websites

3. Parses webpage content using BeautifulSoup

4. Extracts:
Email IDs using regex patterns
Contact numbers using regex patterns

5. Stores extracted data in a structured table
6.Exports the final dataset to an Excel file
---

## ⚠️ Important Notes

Only publicly available information is collected
Some websites may block automated requests
Missing data is marked as "Not Available"
A delay between requests can be added to avoid server overload

---
## 🚀 Future Improvements

Automatic website discovery

CAPTCHA handling

Multi-page scraping (Contact / About pages)

College and school category separation

Data validation & duplicate removal

##  Author

### Samta Sakha
Python | Data Science | Automation
