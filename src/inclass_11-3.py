import pandas
import requests
from bs4 import BeautifulSoup as bs

# EX 1
# get webpage
response = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density")
soup = bs(response.content, "html.parser")

# get the table we want
table = soup.find("table", attrs={"class": "sortable wikitable"})

# create dict we will fill with data
data = {}

# parse each row of the table we found
for tr in table.find_all("tr"):
    tds = tr.find_all("td")

    # for all rows with data
    if (len(tds) > 0):

        # the second col of every data row has a flag
        if(len(tds[1].find_all("span", attrs={"class": "flagicon"})) > 0):
            # store data
            country = tds[1].text.strip() # clean white space in string
            # remove commas in nums
            area_km2 = tds[2].text.replace(',', '')
            area_mi2 = tds[3].text.replace(',', '')
            population = tds[4].text.replace(',', '')
            
            # write to dictionary
            data[country] = {'area_km2': float(area_km2),
                             'area_mi2': float(area_mi2),  
                             'population': int(population)}


# EX 2
df = pandas.DataFrame.from_dict(data, orient='index')
df

# EX 3
df.describe()

# EX 4
df.corr(method='pearson').style.background_gradient(cmap='coolwarm')

# EX 5
df.plot.scatter(x="area_km2", y="population")
