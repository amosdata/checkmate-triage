from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075")

# WAIT a bit before trying to capture the page source
time.sleep(5)  # Let the page load completely

# 💾 Save the entire HTML to a file
html = driver.page_source
with open("page_source.html", "w", encoding="utf-8") as f:
    f.write(html)

try:
    symptom_list = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.index.content-within"))
    )

except Exception as e:
    print(e)

finally:
    driver.quit()
