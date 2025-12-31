# Technopark Startups Scraper

## Disclaimer

- This scraper is intended for educational and non-commercial purposes only. I am not responsible for any inappropriate use.
- I reviewed robots.txt file of the website before scraping it, and made sure it doesn't forbid any type of scraping.

This project is a web scraper built with Selenium to extract all startup details from the **Technopark Morocco "Startup of the Month"** webpage: 
https://www.technopark.ma/start-ups-du-mois/


## Features

- Scrapes all Technopark startups information including:
  -  Name
  -  Sector
  -  Technologies
  -  City
  -  Description
  -  Website
  -  Emails
  -  Phones


---


## Extracted Data Format

The final data is saved as a `JSON` file inside the `data/` folder.



##  Quick Start

- Make sure you have Chrome installed. You'll need chromedriver that matches your Chrome version.
Download it from: https://sites.google.com/chromium.org/driver/ And ensure it is in your system PATH.

- Install requirements:
```
python -m pip install -r requirements.txt
```

- Run the scraper:
```
python main.py
```



## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) to avoid any inappropriate use.
You may use, share, and modify this project for non-commercial purposes only.






