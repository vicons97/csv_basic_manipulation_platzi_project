def population_by_country(data, country):
        result = list(filter(lambda item: item['Country/Territory'] == country, data))
        match = result[0]
        resultn = {
        '2022': int(match['2022 Population']),
        '2020': int(match['2020 Population']),
        '2015': int(match['2015 Population']),
        '2010': int(match['2010 Population']),
        '2000': int(match['2000 Population']),
        '1990': int(match['1990 Population']),
        '1980': int(match['1980 Population']),
        '1970': int(match['1970 Population'])
        }
        return resultn.keys(), resultn.values()
    

def population_percentage_by_continent(data, continent):
    result = list(filter(lambda item: item['Continent'] == continent, data))

    countries = list(map(lambda x: x['Country/Territory'], result))
    ratios = list(map(lambda x: x['World Population Percentage'], result))
    return countries, ratios
