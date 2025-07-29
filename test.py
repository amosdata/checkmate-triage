import requests
from bs4 import BeautifulSoup

url = "https://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.content, "html.parser")

print(soup.prettify()[:1500])
