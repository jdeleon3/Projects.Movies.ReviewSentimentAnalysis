from bs4 import BeautifulSoup
import requests
from app.models.Movie import Movie
from app.models.Review import Review

class MovieSearch:
    def __init__(self):        
        self.url = f"https://www.rottentomatoes.com/search?search="
        

    def search(self, movie_name):
        response = requests.get(self.url + movie_name)
        if response.status_code != 200:
            raise Exception(f"Error fetching data from Rotten Tomatoes: {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('search-page-media-row')
        response = []
        for result in results:
            print(result)            
            cast = result.attrs.get('cast')
            year = result.attrs.get('releaseyear')
            l = result.find('a', {'slot': 'title'})
            title = l.text.strip() if l else None
            url = l.attrs.get('href') if l else None
            if cast and title and year:
                movie = Movie(title=title, year=int(year), cast=cast, url=url)
                response.append(movie)
        
        return response
    
    def get_reviews(self, url:str):
        response = requests.get(f'{url}/reviews')
        if response.status_code != 200:
            raise Exception(f"Error fetching data from Rotten Tomatoes: {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')
        reviews = soup.find_all('p', {'class': 'review-text'})
        if not reviews:
            return []
        
        response = []
        for index, review in enumerate(reviews):
            review_text = review.text.strip()
            if not review_text:
                continue
            r = Review(id=index, content=review_text)
            response.append(r)
        
        return response

    def get_results(self):
        return self.results