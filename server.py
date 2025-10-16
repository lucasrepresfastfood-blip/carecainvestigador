# -*- coding: utf-8 -*-
import requests
from flask import Flask, render_template

app = Flask(__name__)
NASA_API_KEY = "DEMO_KEY" 
SERVER_PORT = 5000

@app.route('/')
def dashboard():
    # Mensagens sem acentos
    return "<h1>Servidor OSINT Tracker Ativo na porta 5000.</h1><p>Use o menu Satelite OSINT no app Android.</p>"

@app.route('/satellite-data')
def get_satellite_data():
    try:
        nasa_url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
        response = requests.get(nasa_url)
        response.raise_for_status()
        data = response.json()
        
        return render_template('satellite_template.html', 
                               image_url=data.get('url', ''), 
                               title=data.get('title', 'N/A'),
                               explanation=data.get('explanation', 'N/A'))
                               
    except requests.RequestException as e:
        # Mensagem de erro sem acentos
        return f"Erro ao conectar com a API da NASA: {e}", 500

if __name__ == '__main__':
    app.run(port=SERVER_PORT)
