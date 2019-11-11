from selenium import webdriver
import pandas as pd
import time

##9:24
WAIT_CONST = 2;
#open up firefox emulator.
driver = webdriver.Firefox()


targURL = "https://studentorg.ucsd.edu"
driver.get(targURL)
time.sleep(WAIT_CONST)


items = len(driver.find_elements_by_tag_name("tr"))
total = []
urls = []
first = True
print(items)
entries = driver.find_elements_by_tag_name("tr")
for entry in entries:
	if first:
		first = False
	else:
		wrapper = entry.find_element_by_tag_name('td')
		dataEntry = wrapper.find_element_by_tag_name('a')
		name = dataEntry.text
		href =  dataEntry.get_attribute('href')
		new = ((name,href))
		total.append(new)
		urls.append(href)
df = pd.DataFrame(total,columns=['clubName','pageID'])
df.to_csv('clubInformationScraped.csv')
for url in urls:
	print("href: "+url)
	driver.get(url)
	time.sleep(WAIT_CONST)
	items = len(driver.find_elements_by_tag_name("tr"))
	totals = []
	firstDescr = True
	secondDescr = True
	descriptions = driver.find_elements_by_tag_name("dd")
	for description in descriptions:
		if firstDescr:
			firstDescr = False
		elif secondDescr:
			purpose = description.text
			new = (purpose)
			totals.append(new)
			secondDescr = False
			print(purpose)
df = pd.DataFrame(totals,columns=['clubPurpose'])
df.to_csv('clubPurposeScraped.csv')
driver.close();
"""

entries = driver.find_elements_by_class_name("tr")
for entry in entries:
    entry_name = quote.find_element_by_class_name('a').text
    href = quote.find_element_by_class_name('a').href
    new = ((entry_name,author))
    total.append(new)
    items+=1
df = pd.DataFrame(total,columns=['clubName','pageID'])
df.to_csv('clubInformationScraped.csv')
print(items)
"""