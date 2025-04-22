'''
    api.py
    Divya Nandalall
    April 21, 202r5

    Uses Flask to show a list of all the countries and their flag's main hue in a 
    given continent which is specificed by the 'continent' string, case insentiviely

    Resources used: flask_sample.py by Jeff Ondich
                    help.html by Jeff Ondich
'''

import sys
import argparse
import flask
import json
import csv

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome! Let\'s learn about flags!'

@app.route('/help')
def get_help():
    return flask.render_template('help.html')

@app.route('/mainhue/<continent>')
def get_mainhue(continent):
    mainhue_dictionary = {}
    continent = continent.lower()
    with open('../data/flags.csv') as f:
        reader = csv.reader(f, delimiter=';') #sets the delimiter to ';'
        for country_data in reader: 
            #if the continent requested matches the continent in the country's data, the country name and its flag's main hue is printed
            # each continent has an associated number: 1=N.America, 2=S.America, 3=Europe, 4=Africa, 4=Asia, 6=Oceania
            if (continent == 'north_america') and country_data[2] == '1':
                mainhue_dictionary[country_data[0]] = country_data[18]
            elif (continent == 'south_america') and country_data[2] == '2':
                mainhue_dictionary[country_data[0]] = country_data[18]
            elif (continent == 'europe') and country_data[2] == '3':
                mainhue_dictionary[country_data[0]] = country_data[18]
            elif (continent == 'africa') and country_data[2] == '4':
                mainhue_dictionary[country_data[0]] = country_data[18]
            elif (continent == 'asia') and country_data[2] == '5':
                mainhue_dictionary[country_data[0]] = country_data[18]
            elif (continent == 'oceania') and country_data[2] == '6':
                mainhue_dictionary[country_data[0]] = country_data[18]
    return json.dumps(mainhue_dictionary)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
