import numpy as np
import pickle
import streamlit as st

# Load the model
loaded_model = pickle.load(open("finalized_model.sav", 'rb'))

def loan(input):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'Loan not approved'
    else:
        return 'Loan approved'

def main():

    # Giving the title
    st.title("Loan Status Prediction")

    # getting input data from user
    Gender_options = ['Male', 'Female']
    Gender = st.selectbox('Choose Gender', Gender_options)
    def map_Gender_options(Gender):
        if Gender == 'Male':
            return 1
        else:
            return 0
    
    Married_options = ['Yes', 'No']
    Married = st.selectbox('Choose maritial status', Married_options)
    def map_married_options(Married):
        if Married == 'Yes':
            return 1
        else:
            return 0

    Dependents_options = ['0', '1', '2', '3']   
    Dependents = st.selectbox('Choose dependents', Dependents_options)

    Education_options = ['Yes', 'No']
    Education = st.selectbox('Select your graduation status', Education_options)
    def map_education_options(Education):
        if Education == 'No':
            return 1
        else:
            return 0

    Self_Employed_options = ['Yes', 'No']
    Self_Employed = st.selectbox('Select your employment status', Self_Employed_options)
    def map_Self_Employed_options(Self_Employed):
        if Self_Employed == 'yes':
            return 1
        else:
            return 0
        
    Applicant_Income = st.text_input('your Income')

    Coapplicant_Income = st.text_input('Coapplicant Income')

    Loan_amount = st.text_input('Loan amount')

    Loan_Amount_Term = st.text_input('Loan amount term')

    Credit_History_options = ['0', '1']
    Credit_History = st.selectbox('Choose credit history', Credit_History_options)

    Property_Area_options = ['Rural', 'Urban', 'Semi-urban']
    Property_Area = st.selectbox('Choose property area', Property_Area_options)
    def map_Property_Area_options(Property_Area):
        if Property_Area == 'Semi-urban':
            return 1
        if Property_Area == 'Rural':
            return 0
        else:
            return 2

    
    # code for prediction
    prediction = ''

    # creating a button for prediction
    if st.button('Loan Status Result'):
        prediction = loan([map_Gender_options(Gender), map_married_options(Married), Dependents, map_education_options(Education), map_Self_Employed_options(Self_Employed), Applicant_Income, Coapplicant_Income, Loan_amount, Loan_Amount_Term, Credit_History, map_Property_Area_options(Property_Area)])

    st.success(prediction)


if __name__ == '__main__':
    main()