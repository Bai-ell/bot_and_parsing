import requests
from bs4 import BeautifulSoup 
import json

data_base = []  

def breakfast():
    url = "https://www.russianfood.com/recipes/bytype/?fid=926&page="
    
    for page_number in range(1, 30):  # Обрабатываем первые 20 рецептов (по 5 на каждой странице)
        page_url = url + str(page_number)
        text_html = requests.get(page_url).text
        text = text_html   
        soup = BeautifulSoup(text, 'lxml')
        list_lap = soup.find_all('div', class_='recipe_list_new')

        for i in list_lap:
            title_text = i.find('div', class_='title').text.strip()
            description = i.find('div', class_="announce").text.strip()
            img = i.find('img')['src'] 
            recipe = i.find('span').text.strip()

        
            data_base.append({
                'title': title_text,
                'description': description,
                'image': f'{img}',
                'recipe': recipe,
            })

    with open('file_for_breakfast.json', 'w', encoding='utf-8-sig') as file:
        json.dump(data_base, file, indent=4, ensure_ascii=False)


breakfast()





def lanch():
    url = "https://www.russianfood.com/recipes/bytype/?fid=927&page="

    for page_number in range(1, 30):
        page_url = url + str(page_number)
        text_html = requests.get(page_url).text
        soup = BeautifulSoup(text_html, 'lxml')
        list_lap = soup.find_all('div', class_='recipe_list_new')

        for i in list_lap:
            title_text = i.find('div', class_='title').text.strip()
            description = i.find('div', class_="announce").text.strip()
            img = i.find('img')['src'] 
            recipe = i.find('span').text.strip()

            data_base.append({
                'title': title_text,
                'description': description,
                'image': f'{img}',
                'recipe': recipe,
            })

    with open('file_for_lunch.json', 'w', encoding='utf-8-sig') as file:
        json.dump(data_base, file, indent=4, ensure_ascii=False)

# lanch()



def dinner():
    url = "https://www.russianfood.com/recipes/bytype/?fid=928&page="

    for page_number in range(1, 30): 
        page_url = url + str(page_number)
        text_html = requests.get(page_url).text
        soup = BeautifulSoup(text_html, 'lxml')
        list_lap = soup.find_all('div', class_='recipe_list_new')

        for i in list_lap:
            title_text = i.find('div', class_='title').text.strip()
            description = i.find('div', class_="announce").text.strip()
            img = i.find('img')['src'] 
            recipe = i.find('span').text.strip()

            data_base.append({
                'title': title_text,
                'description': description,
                'image': f'{img}', 
                'recipe': recipe,
            })

    with open('file_for_dinner.json', 'w', encoding='utf-8-sig') as file:  
        json.dump(data_base, file, indent=4, ensure_ascii=False)

# dinner()
#