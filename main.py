import streamlit as st

def calculate_curb65(confusion, urea, respiratory_rate, blood_pressure, age):
    score = 0
    score += (confusion == 'Yes')
    score += (urea > 7)  # Urea level > 7 mmol/L
    score += (respiratory_rate >= 30)  # Respiratory rate >= 30 breaths/min
    score += (blood_pressure < 90 or diastolic <= 60)  # Systolic < 90 mm Hg or Diastolic ≤ 60 mm Hg
    score += (age >= 65)
    return score

def main():
    st.title("CURB-65 Score Calculator for Pneumonia Severity")
    
    st.write("""
    The CURB-65 score is a clinical prediction rule that has been validated for predicting mortality in community-acquired pneumonia. The score is used to guide decisions about the intensity of treatment in patients diagnosed with pneumonia.
    """)
    
    confusion = st.selectbox('Is the patient confused?', ('No', 'Yes'))
    urea = st.number_input('Enter blood urea nitrogen level (mmol/L):', min_value=0.0, step=0.1)
    respiratory_rate = st.number_input('Enter respiratory rate (breaths per minute):', min_value=0, step=1)
    systolic_bp = st.number_input('Enter systolic blood pressure (mm Hg):', min_value=0, step=1)
    diastolic_bp = st.number_input('Enter diastolic blood pressure (mm Hg):', min_value=0, step=1)
    age = st.number_input('Enter age:', min_value=0, step=1)
    
    if st.button('Calculate CURB-65 Score'):
        score = calculate_curb65(
            confusion=confusion,
            urea=urea,
            respiratory_rate=respiratory_rate,
            blood_pressure=(systolic_bp, diastolic_bp),
            age=age
        )
        st.subheader(f"The CURB-65 Score is: {score}")
        if score >= 3:
            st.error("High risk of mortality. Consider hospital admission and possible intensive care.")
        elif score in [1, 2]:
            st.warning("Moderate risk. Hospitalization may be needed.")
        else:
            st.success("Low risk. Consider home treatment.")

if __name__ == "__main__":
    main()
