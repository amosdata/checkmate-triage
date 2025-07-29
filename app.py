import streamlit as st
import json

# Load JSON data
def load_json(file):
    with open(file, 'r') as f:
        return json.load(f)

symptom_data = load_json('symptom_data.json')
symptom_details = load_json('symptom_details.json')

# Streamlit App UI
st.title("🩺 CheckMate Triage: Symptom Checker")
st.markdown("Enter your symptoms to view possible conditions and what to do next.")

# Multi-select symptoms
selected_symptoms = st.multiselect("Select your symptoms:", list(symptom_data.keys()))

if selected_symptoms:
    possible_conditions = set()
    
    for symptom in selected_symptoms:
        conditions = symptom_data.get(symptom, [])
        possible_conditions.update(conditions)

    st.subheader("🧾 Possible Conditions")
    
    for condition in sorted(possible_conditions):
        details = symptom_details.get(condition, {})
        st.markdown(f"### 🩹 {condition.title()}")
        st.write(f"**Description:** {details.get('description', 'No description available.')}")
        st.write(f"**Severity:** {details.get('severity', 'Unknown')}")
        st.write(f"**Suggested Action:** {details.get('suggested_action', 'No recommendation available.')}")
        st.markdown("---")
else:
    st.info("Please select one or more symptoms to get started.")
