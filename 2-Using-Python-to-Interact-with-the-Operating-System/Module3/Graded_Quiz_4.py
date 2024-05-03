# You’re working with a dataset on capital cities around the world. This dataset includes a field that contains information on both city and country. You’d like to separate this field into two fields, a city field and a country field. In the current field, city and country are separated by either a comma or a period. Complete the function parse_city_country to split city and country into two strings and return only the city.

import re

def parse_city_country(text):
  pattern = r"[.,]" #enter the regex pattern here
  result = re.split(pattern, text) #enter the re method  here
  if len(result) != 2:
    return ""
  return result[0] #return the correct capturing group

print(parse_city_country("Paris, France")) # should return Paris
print(parse_city_country("Mumbai, India")) # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil")) # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank

