import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#Get all data
data_url = "https://covid-193.p.rapidapi.com/statistics"

data_headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "a3dd48e29amshc8331b9f27e2938p12df0bjsn79d086cfd0f9"
}

#Get all country name
name_url = "https://covid-193.p.rapidapi.com/countries"

name_headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "a3dd48e29amshc8331b9f27e2938p12df0bjsn79d086cfd0f9"
}

res = requests.get(name_url, headers=name_headers).json()
countries = res["response"]

#Define routes
@app.route("/")
def index():
    world_res = requests.get(data_url, headers=data_headers, params={"country":"All"}).json()
    world_cases = world_res["response"][0]['cases']["total"]
    world_deaths = world_res["response"][0]["deaths"]["total"]
    world_recovered = world_res["response"][0]["cases"]["recovered"]

    return render_template("index.html", countries=countries, world_cases=world_cases, world_deaths=world_deaths, world_recovered=world_recovered)

@app.route("/<string:country>")
def country(country):
    querystring = {"country": country}

    response = requests.get(data_url, headers=data_headers, params=querystring).json()

    cases = response["response"][0]["cases"]["total"]
    deaths = response["response"][0]["deaths"]["total"]
    recovered = response["response"][0]["cases"]["recovered"]

    return render_template("countries.html", heading=country, cases=cases, deaths=deaths, recovered=recovered, country=country)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', message="No country found!"),  404
