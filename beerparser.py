import sys

from bs4 import BeautifulSoup


class BeerParser:
    def __init__(self, path):
        self.path = path
        self.beerlist = []
        self.soup = None

    def get_beers(self):
        self.soup = BeautifulSoup(open(self.path, encoding='utf-8'), 'html.parser')
        for beer in self.soup.find_all('div', {'class': 'beer-info '}):
            beer_dict = {'name': beer.find('a').text, 'style': beer.find('em').text}
            rating_str_class = beer.find('span', {'class': 'rating'})
            if rating_str_class is not None:
                rating_str = rating_str_class.get('class')[2].replace('r', '')
                beer_dict['rating'] = int(rating_str) / 100.0
            else:
                beer_dict['rating'] = None
            details = beer.find('div', {'class': 'beer-details'}).find('span')
            details_text = details.text

            details_numbers = details_text.replace('ABV', '').replace('%', '').replace('IBU', '').split('•')
            if len(details_numbers) > 1:
                abv = details_numbers[0].strip()
                ibu = details_numbers[1].strip()
                if abv == 'N/A':
                    beer_dict['ABV'] = None
                else:
                    beer_dict['ABV'] = float(abv)
                if ibu == 'N/A':
                    beer_dict['IBU'] = None
                else:
                    beer_dict['IBU'] = int(ibu)
            self.beerlist.append(beer_dict)
        return self.beerlist


if __name__ == "__main__":
    if len(sys.argv) < 2:
        default_path = 'my_file.html'
    else:
        default_path = sys.argv[1]
    beers = BeerParser(default_path).get_beers()
    [print(beer) for beer in beers]
