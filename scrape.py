import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# === Load symptoms list ===
with open("symptoms.txt", "r", encoding="utf-8") as f:
    symptoms = [line.strip().split("::") for line in f if "::" in line]

# === Configure headless browser ===
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

symptom_data = {}

for name, link in symptoms:
    try:
        print(f"Scraping {name} ...")
        driver.get(link)
        time.sleep(2)  # Let page load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        page_content = {}

        # === Find sections like h2: "Causes", "When to see a doctor" ===
        for header in soup.find_all(["h2", "h3"]):
            section_title = header.get_text(strip=True)
            content = []

            next_node = header.find_next_sibling()
            while next_node and next_node.name not in ["h2", "h3"]:
                if next_node.name in ["p", "ul"]:
                    content.append(next_node.get_text(strip=True))
                next_node = next_node.find_next_sibling()

            if content:
                page_content[section_title] = content

        symptom_data[name] = page_content
    except Exception as e:
        print(f"Error scraping {name}: {e}")
        continue

# === Save results ===
with open("symptom_details.json", "w", encoding="utf-8") as f:
    json.dump(symptom_data, f, indent=2, ensure_ascii=False)

print("✅ Done scraping symptom details.")
driver.quit()
import json

# Make sure symptom_data is your list of dictionaries
# Example: [{"name": "Headache", "description": "...", "causes": "..."}, {...}, ...]

with open("symptom_details.json", "w", encoding="utf-8") as f:
    json.dump(symptom_data, f, ensure_ascii=False, indent=2)

print("✅ Saved symptom details to symptom_details.json")
