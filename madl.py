from bs4 import BeautifulSoup
import requests
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--download", action=argparse.BooleanOptionalAction, help="Specify true if you want to download the results")
parser.add_argument("--fwtype", help="DEX,CEX,REBUG")
parser.set_defaults(download=False)
parser.set_defaults(fwtype="DEX")
args = parser.parse_args()

def get_page(category = "DEX"):

    final_url = "https://archive.midnightchannel.net/SonyPS/Firmware/index.php?cat=" + category.upper()
    r = requests.get(final_url)
    r = r.text
    return r

def parse_page(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    lines = soup.findAll('td', {'class': 'desc'})
    res = []
    for i in range(len(lines)):
     xd = BeautifulSoup(str(lines[i]), "html.parser")
     link = xd.find('a', href=True)
     res.append(link['href'])
    
    return res



page = get_page(args.fwtype)
download = args.download
if page != None and download == True:
   res = parse_page(page)
   for i in range(len(res)):
      w = requests.get("https://archive.midnightchannel.net/SonyPS/Firmware/"+ res[i])
      print("Downloading: " + res[i])
      with open(res[i].split("/")[-1], 'wb') as f:
            f.write(w.content) 
elif page != None and download == False:
    res = parse_page(page)
    for i in range(len(res)):
        print("Found: https://archive.midnightchannel.net/SonyPS/Firmware/" + res[i])
    
else:
    print("Didn't find any matching results")





