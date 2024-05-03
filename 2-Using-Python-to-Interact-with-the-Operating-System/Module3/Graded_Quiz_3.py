# You are reading an article that contains website urls in the format https://www.website-domain.com. You’d like to extract the complete urls from the text automatically, instead of copying and pasting them by hand. 

# Complete the function find_url to extract all encrypted websites that begin with https:// and end with any top level domain, such as .org, .com, or .co from the text.

import re

def find_url(website):
 pattern = r"https://[\w.-]+" #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result


print(find_url("Go to the website https://www.coursera.com find more information about Google Certificate Programs. Then, visit https://www.python.org/ to learn more about Python. ")) # Should return ['https://www.coursera.com', 'https://www.python.org']
print(find_url("You can find anything on https://www.google.com!")) # Should return ['https://www.google.com']
print(find_url("You can find anything on http://www.google.com!")) # Should return []
print(find_url("Check out python.org!")) # Should return []
