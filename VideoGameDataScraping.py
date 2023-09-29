from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_video_games'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[1]

world_titles = table.find_all('th')

world_table_titles = [title.text.strip() for title in world_titles]

dataFrame = pd.DataFrame(columns = world_table_titles)

gameTitle = []
sales = []
series = []
platform = []
releaseDate = []
developer = []
publisher = []

rows = table.find_all('tr')
for row in rows[1:]:
    rowData = row.find_all('td')
    tableData = [data.text.strip() for data in row]
    gameTitle.append(rowData[0].text.strip())
    sales.append(rowData[1].text.strip())
    series.append(rowData[2].text.strip())
    platform.append(rowData[3].text.strip())
    releaseDate.append(rowData[4].text.strip())
    developer.append(rowData[5].text.strip())
    publisher.append(rowData[6].text.strip())

dataFrame['Title'] = gameTitle
dataFrame['Sales'] = sales
dataFrame['Series'] = series
dataFrame['Platform(s)'] = platform
dataFrame['Initial release date'] = releaseDate
dataFrame['Developer(s)[b]'] = developer
dataFrame['Publisher(s)[b]'] = publisher 

dataFrame.to_csv(r'C:\Users\docto\OneDrive\Desktop\VideoGameScraping.csv', index = False)