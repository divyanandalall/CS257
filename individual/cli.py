''' 
    cli.py 
    Divya Nandalall, April 17, 2025


    NAME: cli.py - command line interface assignment
    SYNOPSIS: python3 cli.py get_mainhue continent
    DESCRIPTION: Shows a list of all the countries and their flag's main colour in a 
    given continent which is specificed by the 'continent' string, case insentiviely
'''

import csv
import sys
import argparse

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description="Report on country flag's mainhue in a given continent")
    parser.add_argument('filename', help = "The name of the file with countries' flag data")
    parser.add_argument('continent', help= 'The continent of the countries whose mainhue you seek: North_America; South_America; Europe; Africa; Asia; Oceania')
    parsed_arguments = parser.parse_args()
    return parsed_arguments


def get_mainhue(filename, continent): 
    with open(filename) as f:
        reader = csv.reader(f, delimiter=';') #sets the delimiter to ';'
        for country_data in reader: 
            #if the continent requested matches the continent in the country's data, the country name and its flag's main hue is printed
            # each continent has an associated number: 1=N.America, 2=S.America, 3=Europe, 4=Africa, 4=Asia, 6=Oceania
            if (continent == 'north_america') and country_data[2] == '1':
                print(f"{country_data[0]}:{country_data[18]}")
            elif (continent == 'south_america') and country_data[2] == '2':
                print(f"{country_data[0]}: {country_data[18]}")
            elif (continent == 'europe') and country_data[2] == '3':
                print(f"{country_data[0]}: {country_data[18]}")
            elif (continent == 'africa') and country_data[2] == '4':
                print(f"{country_data[0]}: {country_data[18]}")
            elif (continent == 'asia') and country_data[2] == '5':
                print(f"{country_data[0]}: {country_data[18]}")
            elif (continent == 'oceania') and country_data[2] == '6':
                print(f"{country_data[0]}: {country_data[18]}")

def usage_statement():
    print(f'Usage: {sys.argv[0]} csvfile continent')
    print('Do not use spaces, use _ instead')
    print('Available continents: North_America; South_America; Europe; Africa; Asia; Oceania')

def main():
    arguments = get_parsed_arguments()
    arguments.continent = arguments.continent.lower() #changes the continent to lower case
    if len(sys.argv)!=3 or (arguments.continent!='north_america' and arguments.continent!='south_america' and arguments.continent!='europe' and arguments.continent!='asia' and arguments.continent!='africa' and arguments.continent!='oceania'):
        usage_statement()
        exit()
    get_mainhue(arguments.filename, arguments.continent)


if __name__ == '__main__':
    main()
