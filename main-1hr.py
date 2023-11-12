from bs4 import BeautifulSoup

# opening a file and access it with a variable name as html_file
with open('D:\\HTML\\udemy learning\\bootstrap learning\\forms.html', 'r') as html_file:
  content = html_file.read()
  

soup = BeautifulSoup(content,'lxml')
 # print(soup.prettify())
  # find used for 1 iteration,whereas findall returns all iterations
#card_title_tags= soup.find_all('div',class_='form-control') 
#print(card_title_tags)

#for card in card_title_tags:
 # print(card.text)

input_fields=soup.find_all('div',class_='form-control')
for inputs in input_fields:
  input_details = inputs.label.text
  print(input_details)