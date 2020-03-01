import os
import pdfkit #module for converting html to PDF
import requests # pulls html of web url
from bs4 import BeautifulSoup

print ('eBay item Parcer')

dirName = 'Ebay Dump'


try:
    # Create target Directory on Desktop
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') #creates ~/Desktop
    os.mkdir(desktop + '/'+ dirName) #creates folder on desktop from the dirName
    print("You're all set!" , dirName ,  "has been created on your desktop! ")
except FileExistsError:
    print("You're all set! Directory " , dirName ,  " already exists!")


item_url = ''
print ("What is the eBay item url? Press return key when done")
item_url =  input() #generates ebay item url
print ()
file_name = ''
while True:
    print ("Thanks! What would you like to name the pdf file?")
    file_name = input() #generates file name for later as PDF name
    print()
    print ("Does this look good? (write yes or no and press return)  " + file_name + '.pdf') #confirms file name
    confirmation = input() #file name to write to pdf
    if confirmation == 'yes':
        break
print ("Thanks! Saving page info now!")

options = {
    'quiet': ''  #hides text output of pdfkit
    }
pdfkit.from_url( item_url, (desktop + '/'+ dirName + '/'+ file_name + '.pdf'),options=options)
print ("Now Moving File To Proper Location!")
print ()
page = requests.get(item_url) #requests html from url entered earlier
soup = BeautifulSoup(page.text, 'html.parser') #parses html file, writes to text
#price = soup.find(id='prcIsum_bidPrice') 
price = soup.find(itemprop="price").get_text()
#current bid price, NEEDS WORK
name = soup.find("title").get_text() #listing name / page title

print ('The listing title is ' + str(name) )
print ('And the current bid is: ' + str(price) )

    


# find fix pdf write location To Ebay Dump created in beginning DONE
# find way to loop back if name is wrong DONE
#find way to loop back to beginning when task completes
#fix bid price