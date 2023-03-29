import Packages.utils
import Packages.read_csv
import Packages.charts


def first_chart():
    
    data = Packages.read_csv.read_csv('./world_population.csv')
    country = input('Type Country => ')
    keys, values = Packages.utils.population_by_country(data, country)

    if len(keys) > 0: 
        choice = int(input('Choose a function: 1: Bar Chart 2: Pie Chart : '))
        if choice == 1:
            barchar = Packages.charts.generate_bar_char(keys, values)
            print(barchar)
        elif choice == 2:
            piehart = Packages.charts.gen_pie_chart(keys, values)
            print(piehart)
        else:
            print('Invlaid choice')

def second_chart():
    data = Packages.read_csv.read_csv('./world_population.csv')
    continent = input('Type Continent => ')
    countries, ratios = Packages.utils.population_percentage_by_continent(data, continent)

    if len(countries) > 0:
        choice = int(input('Choose a function: 1: Bar Chart 2: Pie Chart : '))
        if choice == 1:
            barchar = Packages.charts.generate_bar_char(countries, ratios)
            print(barchar)
        elif choice == 2:
            piehart = Packages.charts.gen_pie_chart(countries, ratios)
            print(piehart)
        else:
            print('Invlaid choice') 

def run():

  first_chart()
  cont = input('Do you want to continue?(y/n): ')
  if cont == 'y':
    second_chart()
  elif cont == 'n':
     print ('Thanks for using this code')
  else:
     print('Wrong answer')  

if __name__ == '__main__':
  run()

