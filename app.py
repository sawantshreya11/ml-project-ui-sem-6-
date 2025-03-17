import streamlit as st
from streamlit_option_menu import option_menu

# Custom CSS
# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            color: #c62828;
            font-family: Arial, sans-serif;
        }
        .stButton>button, .print-button {
            background-color: #c62828;
            color: white;
            border-radius: 12px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        }
        .stButton>button:hover, .print-button:hover {
            background-color: #ff7043;
            transform: scale(1.05);
        }
        .report-container {
            background-color: #fff7f7;
            padding: 20px;
            border: 2px solid #c62828;
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        }
        .stRadio > div {
            display: flex;
            gap: 10px;
            flex-direction: row;
        }
        .yellow-alert {
            background-color: #fff3cd;
            color: #856404;
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
            border: 1px solid #ffeeba;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)


# Sidebar menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Breast Cancer Prediction'],
                           icons=['activity', 'heart', 'cast'], default_index=0)

# ✅ Print button
st.markdown("""<button class="print-button" onclick="window.print()">Print Report</button>""", unsafe_allow_html=True)

# ----------------------------- Diabetes Prediction ------------------------------
if selected == "Diabetes Prediction":
    st.title("🩺 Diabetes Prediction")

    c1, c2, c3 = st.columns(3)
    with c1:
        pregnancies = st.number_input('Pregnancies', min_value=0, step=1)
    with c2:
        glucose = st.number_input('Glucose (mg/dL)', min_value=0, step=1)
    with c3:
        blood_pressure = st.number_input('Blood Pressure (mm Hg)', min_value=0, step=1)
    with c1:
        skin_thickness = st.number_input('Skin Thickness (mm)', min_value=0, step=1)
    with c2:
        insulin = st.number_input('Insulin (IU/mL)', min_value=0, step=1)
    with c3:
        bmi = st.number_input('BMI', min_value=0.0, step=0.1)
    with c1:
        dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, step=0.01)
    with c2:
        age = st.number_input('Age (years)', min_value=0, step=1)

    if st.button('Predict', key="diabetes_predict"):
        st.info("Prediction model not yet implemented — Training in progress!")
        
        # ✅ Report Generation
        st.markdown(f"""
            <div class="report-container">
                <h4>Diabetes Report</h4>
                <p><strong>Pregnancies:</strong> {pregnancies}</p>
                <p><strong>Glucose:</strong> {glucose} mg/dL</p>
                <p><strong>Blood Pressure:</strong> {blood_pressure} mm Hg</p>
                <p><strong>Skin Thickness:</strong> {skin_thickness} mm</p>
                <p><strong>Insulin:</strong> {insulin} IU/mL</p>
                <p><strong>BMI:</strong> {bmi}</p>
                <p><strong>Diabetes Pedigree Function:</strong> {dpf}</p>
                <p><strong>Age:</strong> {age} years</p>
            </div>
        """, unsafe_allow_html=True)

# ----------------------------- Heart Disease Prediction ------------------------------
if selected == "Heart Disease Prediction":
    st.title("❤️ Heart Disease Prediction")

    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input('Age (years)', min_value=0, step=1)
    with c2:
        sex = st.radio('Sex', ['Female', 'Male'], horizontal=True)
        sex_str = 'Male' if sex == 'Male' else 'Female'
    with c3:
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, step=1)
    with c1:
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, step=1)
    with c2:
        chol = st.number_input('Cholesterol (mg/dL)', min_value=0, step=1)
    with c3:
        fbs = st.radio('Fasting Blood Sugar > 120 mg/dL', ['No', 'Yes'], horizontal=True)
        fbs_str = 'Yes' if fbs == 'Yes' else 'No'
    with c1:
        restecg = st.number_input('Resting ECG Result (0-2)', min_value=0, max_value=2, step=1)
    with c2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, step=1)
    with c3:
        exang = st.radio('Exercise-Induced Angina', ['No', 'Yes'], horizontal=True)
        exang_str = 'Yes' if exang == 'Yes' else 'No'

    if st.button('Predict', key="heart_predict"):
        st.info("Prediction model not yet implemented — Training in progress!")
        
        # ✅ Report Generation
        st.markdown(f"""
            <div class="report-container">
                <h4>Heart Disease Report</h4>
                <p><strong>Age:</strong> {age} years</p>
                <p><strong>Sex:</strong> {sex_str}</p>
                <p><strong>Chest Pain Type:</strong> {cp}</p>
                <p><strong>Resting BP:</strong> {trestbps} mm Hg</p>
                <p><strong>Cholesterol:</strong> {chol} mg/dL</p>
                <p><strong>Fasting Blood Sugar > 120 mg/dL:</strong> {fbs_str}</p>
                <p><strong>Resting ECG:</strong> {restecg}</p>
                <p><strong>Max Heart Rate:</strong> {thalach}</p>
                <p><strong>Exercise-Induced Angina:</strong> {exang_str}</p>
            </div>
        """, unsafe_allow_html=True)

# ✅ Report for Breast Cancer Prediction
if selected == "Breast Cancer Prediction":
    st.title("🎗️ Breast Cancer Prediction")

    c1, c2, c3 = st.columns(3)
    with c1:
        radius_mean = st.number_input('Radius Mean', min_value=0.0, step=0.1)
    with c2:
        texture_mean = st.number_input('Texture Mean', min_value=0.0, step=0.1)
    with c3:
        perimeter_mean = st.number_input('Perimeter Mean', min_value=0.0, step=0.1)
    with c1:
        area_mean = st.number_input('Area Mean', min_value=0.0, step=0.1)
    with c2:
        smoothness_mean = st.number_input('Smoothness Mean', min_value=0.0, step=0.01)
    with c3:
        compactness_mean = st.number_input('Compactness Mean', min_value=0.0, step=0.01)
    if st.button('Predict', key="cancer_predict"):
        st.info("Prediction model not yet implemented — Training in progress!")
        
        st.markdown(f"""
            <div class="report-container">
                <h4>Breast Cancer Report</h4>
                <p><strong>Radius Mean:</strong> {radius_mean}</p>
            </div>
        """, unsafe_allow_html=True)
