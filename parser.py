from bs4 import BeautifulSoup
import pandas as pd
soup = BeautifulSoup(open("myfile.html", encoding="utf-8"), "html.parser")
bearlist = []
for bear in soup.find_all('div', {'class' : 'beer-info '}):
    beer_dict={}
    beer_dict['name'] = bear.find('a').text
    beer_dict['style'] = bear.find('em').text
    rating_str_class =  bear.find('span', {'class': 'rating'})
    if rating_str_class is not None:
            rating_str = rating_str_class.get('class')[2].replace('r','')
            beer_dict['rating'] = int(rating_str)/100.0
    else:
        beer_dict['rating'] = None
    details = bear.find('div', {'class':'beer-details'}).find('span')
    details_text = details.text

    details_numbers = details_text.replace('ABV','').replace('%','').replace('IBU','').split('•')
    if len(details_numbers)>1:
        print(details_numbers)
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

    bearlist.append(beer_dict)
    
print(bearlist)
bear_df = pd.DataFrame(bearlist)
bear_df.drop_duplicates()
print(bear_df.head())
print(bear_df.columns)
print(bear_df.describe())
print(bear_df.info())