# from bs4 import BeautifulSoup
import requests
#
# res = requests.get("https://www.worldometers.info/coronavirus/")
# content = res.content
#
# soup = BeautifulSoup(content, features="html.parser")
#
# links = soup.findAll("a", {"href": "country/viet-nam/"})[0]
# links = links.find_next('td')
#
# # for l in links:
# #     if l.attrs["href"] == "country/viet-nam/":
# #         print(l)
# print(links)

url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country":"All"}

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "a3dd48e29amshc8331b9f27e2938p12df0bjsn79d086cfd0f9"
    }

response = requests.get(url, headers=headers, params={"country":"All"}).json()

print(response["response"][0]['cases']["total"])
