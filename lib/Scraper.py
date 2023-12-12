from bs4 import BeautifulSoup
import requests
from Course import Course

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        doc = BeautifulSoup(requests.get('https://learn-co-curriculum.github.io/site-for-scraping/courses').text,
                            'html.parser')
        return doc

    def get_courses(self):
        return self.get_page().select('.post')
    
    def make_courses(self):
        for c in self.get_courses():
            title = c.select("h2")[0].text if c.select("h2") else ''
            date = c.select(".date")[0].text if c.select('.date') else ''
            description = c.select("p")[0].text if c.select('p') else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        
        return self.courses
    
    def print_courses(self):
        for c in self.make_courses():
            print(c)