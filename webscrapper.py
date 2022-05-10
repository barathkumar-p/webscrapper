''' python code to scrap google for pdf with specific title'''

from bs4 import BeautifulSoup
import requests,urllib.request
import lxml
headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

params = {
  "q": "S.K.GOYAL OBJECTIVE MATHEMATICS:pdf"
}

def get_pdfs():
    html = requests.get('https://www.google.com/search', headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'lxml')

    for index, result in enumerate(soup.select('.tF2Cxc')):

    
      if result.select_one('.ZGwO7'):
        pdf_file = result.select_one('.yuRUbf a')['href']
        
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36')]
        urllib.request.install_opener(opener)

        # save PDF
        urllib.request.urlretrieve(pdf_file, f"bs4_pdfs/pdf_file_{index}.pdf")

        print(f'Saving PDF №{index}..')
      else: pass


#barathkumar
