#!/usr/bin/python3

import requests

API_KEY = "YOUR_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def detect_city():
    resposta = requests.get("http://ip-api.com/json/")
    dados = resposta.json()
    cidade = dados.get("city")
    return cidade

def clima(cidade):
    params = {
        "q": cidade,
        "appid": API_KEY,
        "lang": "pt_br",
        "units": "metric" # "metric" para Celcius / "imperial" para Fahrenheit.
    }

    resposta = requests.get(BASE_URL, params=params)

    if resposta.status_code == 200:

        dados = resposta.json()
        clima = dados["weather"][0]["description"]
        temperatura = dados["main"]["temp"]
        umidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]

        print(f"Condição: {clima}")
        print(f"Temperatura: {temperatura:.1f}°C")
        print(f"Umidade: {umidade}%")
        print(f"Vento: {vento} m/s")

    if resposta.status_code == 200 and params["units"] == "imperial":
        
        dados = resposta.json()
        clima = dados["weather"][0]["description"]
        temperatura = dados["main"]["temp"]
        umidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]

        print(f"Condição: {clima}")
        print(f"Temperatura: {temperatura:.1f}°F")
        print(f"Umidade: {umidade}%")
        print(f"Vento: {vento} m/s")

def main():
    cidade = detect_city()
    if cidade:
        clima(cidade)
    
    if API_KEY == "YOUR_KEY":
        print("Adicione sua chave primeiro!")

if __name__ == "__main__":
    main()