from flask import Flask, jsonify, request, response
import json 
import psycopg2

app = Flask(__name__)

@app.route('/',methods='POST')
def home(methods):
    if methods == 'POST':
        data = request.get_json()

        first_name = data['first_name']
        last_name = data['last_name')
        email = data['email']
        password = data['password']
        
