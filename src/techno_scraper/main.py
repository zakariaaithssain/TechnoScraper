from .modules.scraper import Scraper


def main():
    techno_scraper = Scraper()
    try:
        techno_scraper.scrape().save_data()
    except AttributeError:
        pass  # when scraping is stopped manually we get attribute error because of the chaining


if __name__ == "__main__":
    main()



