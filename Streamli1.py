import numpy as np 
import streamlit as st 
import joblib 

model= joblib.load('decision_tree.pkl')

def main():
    st.title('ML Model Prediction App')
    st.write('Enter the values for the following features to get a prediction:')

    REGION = st.number_input('REGION')
    TENURE = st.number_input('TENURE' , nin_value=0 , max_value= 7)
    MONTANT = st.number_input('MONTANT')
    FREQUENCE_RECH = st.number_input('FREQUENCE_RECH')
    REVENUE = st.number_input('REVENUE')
    FREQUENCE = st.number_input('FREQUENCE')
    DATA_VOLUME = st.number_input('DATA_VOLUME')
    ON_NET = st.number_input('ON_NET')
    ORANGE = st.number_input('ORANGE')
    TIGO = st.number_input('TIGO')
    ZONE1 = st.number_input('ZONE1')
    ZONE2 = st.number_input('ZONE2')
    MRG = st.number_input('MRG')
    REGULARITY = st.number_input('REGULARITY')
    TOP_PACK = st.text_input('TOP_PACK')
    FREQ_TOP_PACK = st.number_input('FREQ_TOP_PACK')

    if st.button ('PREDICT '):
        data_to_predict = np.array([[REGION , TENURE, MONTANT ,FREQUENCE_RECH ,REVENUE
                                    ,DATA_VOLUME ,ON_NET ,ORANGE , TIGO ,ZONE1 ,ZONE2, MRG ,REGULARITY, TOP_PACK, FREQ_TOP_PACK ]])
    print(data_to_predict)
    result = model.predict(data_to_predict)
    st.success(result)

if __name__ == '__main__':
    main()