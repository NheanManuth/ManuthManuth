import requests
from bs4 import BeautifulSoup

url = "https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
pickup_lines_dict = {}

#Scrape all the titles of each pickup line.
all_titles = soup.find_all(name='li', class_='css-32630i emt9r7s3')
print("\nAll tittles of pickup lines:")
for index, title in enumerate(all_titles, start=1):
    title_text = title.find('a', class_='emt9r7s2 css-1mp8e4k e1c1bym14').text
    pickup_lines_dict[title_text] = []

#Scrape all the pickup lines under each title.

#Title1 with its pickup line
pickup_line_title1 = soup.find_all('ul', attrs={"data-node-id": "10"})
for title1 in pickup_line_title1:
    title1_text = all_titles[0].find('a', class_='emt9r7s2 css-1mp8e4k e1c1bym14').text
    for li in title1.find_all('li'):
        pickup_line = li.text.strip()
        pickup_lines_dict[title1_text].append(pickup_line)
        
#Title2 with its pickup line
pickup_line_title2 = soup.find_all('ul', attrs={"data-node-id":"16"})
for title2 in pickup_line_title2:
    title2_text = all_titles[1].find('a', class_='emt9r7s2 css-1mp8e4k e1c1bym14').text
    for li in title2.find_all('li'):
        pickup_line = li.text.strip()
        pickup_lines_dict[title2_text].append(pickup_line)
        
#Title3 with its pickup line
pickup_line_title3 = soup.find_all('ul', attrs={"data-node-id":"16"})
for title3 in pickup_line_title3:
    title3_text = all_titles[2].find('a', class_='emt9r7s2 css-1mp8e4k e1c1bym14').text
    for li in title3.find_all('li'):
        pickup_line = li.text.strip()
        pickup_lines_dict[title3_text].append(pickup_line)
        
#Title4 with its pickup line
pickup_line_title4 = soup.find_all('ul', attrs={"data-node-id":"16"})
for title4 in pickup_line_title4:
    title4_text = all_titles[3].find('a', class_='emt9r7s2 css-1mp8e4k e1c1bym14').text
    for li in title4.find_all('li'):
        pickup_line = li.text.strip()
        pickup_lines_dict[title4_text].append(pickup_line)
        
#Title5 with its pickup line
pickup_line_title5 = soup.find_all('ul', attrs={"data-node-id":"16"})
for title5 in pickup_line_title5:
    title5_text = all_titles[4].find('a', class_='emt9r7s2 css-1mp8e4k e1c1bym14').text
    for li in title5.find_all('li'):
        pickup_line = li.text.strip()
        pickup_lines_dict[title5_text].append(pickup_line)

#Title6 with its pickup line
pickup_line_title6 = soup.find_all('ul', attrs={"data-node-id":"16"})
for title6 in pickup_line_title6:
    title6_text = all_titles[5].find('a', class_='emt9r7s2 css-1mp8e4k e1c1bym14').text
    for li in title6.find_all('li'):
        pickup_line = li.text.strip()
        pickup_lines_dict[title6_text].append(pickup_line)
        
#Title7 with its pickup line
pickup_line_title7 = soup.find_all('ul', attrs={"data-node-id":"16"})
for title7 in pickup_line_title7:
    title7_text = all_titles[6].find('a', class_='emt9r7s2 css-1mp8e4k e1c1bym14').text
    for li in title7.find_all('li'):
        pickup_line = li.text.strip()
        pickup_lines_dict[title7_text].append(pickup_line)
        
print("\nDictionary of Pickup Lines:")
for title, lines in pickup_lines_dict.items():
    print(f"\nTitle: {title}")
    for line in lines:
        print(f"    • {line}")