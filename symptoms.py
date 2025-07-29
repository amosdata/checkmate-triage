from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Optional: run in headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Start driver
driver = webdriver.Chrome(options=chrome_options)

# Open the page
url = "https://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075"
driver.get(url)

# Wait for content to load
time.sleep(5)

# Grab all symptom <a> tags for adults
adult_symptoms = driver.find_elements(By.XPATH, "//a[starts-with(@id, 'main_0_maincontent_1_SympTomRepeater_AdultSymptom_')]")
child_symptoms = driver.find_elements(By.XPATH, "//a[starts-with(@id, 'main_0_maincontent_1_SymptomChildRepeater_ChildSymptom_')]")

# Extract and print names
print("Adult Symptoms:")
for a in adult_symptoms:
    print("-", a.text)

print("\nChild Symptoms:")
for a in child_symptoms:
    print("-", a.text)

driver.quit()
