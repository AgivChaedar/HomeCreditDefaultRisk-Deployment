import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

@st.cache()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, OCCUPATION_TYPE, HOUSETYPE_MODE, CREDIT_ACTIVE, CREDIT_TYPE, NAME_CONTRACT_TYPE, NAME_CONTRACT_STATUS, CNT_INSTALMENT, AGE_YEARS, AMT_INCOME_TOTAL, YEARS_ENTRY_PAYMENT, EMPLOYED_TO_AGE_RATIO, AMT_ANNUITY, NUM_INSTALMENT_NUMBER, YEARS_EMPLOYED, AMT_CREDIT, EXT_SOURCE_MEAN):
            
    # Pre-processing user input
    AGE_YEARS = AGE_YEARS

    if CODE_GENDER == 'M':
        CODE_GENDER = 0
    elif CODE_GENDER == 'F':
        CODE_GENDER = 1
    
    if FLAG_OWN_CAR == 'N':
        FLAG_OWN_CAR = 0
    elif FLAG_OWN_CAR == 'Y':
        FLAG_OWN_CAR = 1

    if FLAG_OWN_REALTY == 'N':
        FLAG_OWN_REALTY = 0
    elif FLAG_OWN_REALTY == 'Y':
        FLAG_OWN_REALTY = 1

    if NAME_INCOME_TYPE == 'Working':
        NAME_INCOME_TYPE = 0
    elif NAME_INCOME_TYPE == 'Commercial associate':
        NAME_INCOME_TYPE = 1
    elif NAME_INCOME_TYPE == 'State servant':
        NAME_INCOME_TYPE = 2

    if NAME_EDUCATION_TYPE == 'Secondary / secondary special':
        NAME_EDUCATION_TYPE = 0
    elif NAME_EDUCATION_TYPE == 'Higher education':
        NAME_EDUCATION_TYPE = 1
    elif NAME_EDUCATION_TYPE == 'Incomplete higher':
        NAME_EDUCATION_TYPE = 2
    elif NAME_EDUCATION_TYPE == 'Lower secondary':
        NAME_EDUCATION_TYPE = 3
    elif NAME_EDUCATION_TYPE == 'Academic degree':
        NAME_EDUCATION_TYPE = 4

    if NAME_FAMILY_STATUS == 'Married':
        NAME_FAMILY_STATUS = 0
    elif NAME_FAMILY_STATUS == 'Single / not married':
        NAME_FAMILY_STATUS = 1
    elif NAME_FAMILY_STATUS == 'Civil marriage':
        NAME_FAMILY_STATUS = 2
    elif NAME_FAMILY_STATUS == 'Separated':
        NAME_FAMILY_STATUS = 3
    elif NAME_FAMILY_STATUS == 'Widow':
        NAME_FAMILY_STATUS = 4

    if OCCUPATION_TYPE == 'Laborers':
        OCCUPATION_TYPE = 0
    elif OCCUPATION_TYPE == 'Sales staff':
        OCCUPATION_TYPE = 1
    elif OCCUPATION_TYPE == 'Core staff':
        OCCUPATION_TYPE = 2
    elif OCCUPATION_TYPE == 'Managers':
        OCCUPATION_TYPE = 3
    elif OCCUPATION_TYPE == 'Drivers':
        OCCUPATION_TYPE = 4
    elif OCCUPATION_TYPE == 'High skill tech staff':
        OCCUPATION_TYPE = 5
    elif OCCUPATION_TYPE == 'Accountants':
        OCCUPATION_TYPE = 6
    elif OCCUPATION_TYPE == 'Medicine staff':
        OCCUPATION_TYPE = 7
    elif OCCUPATION_TYPE == 'Security staff':
        OCCUPATION_TYPE = 8
    elif OCCUPATION_TYPE == 'Cleaning staff':
        OCCUPATION_TYPE = 9
    elif OCCUPATION_TYPE == 'Cooking staff':    
        OCCUPATION_TYPE = 10
    elif OCCUPATION_TYPE == 'Private service staff':
        OCCUPATION_TYPE = 11
    elif OCCUPATION_TYPE == 'Waiters/barmen staff':
        OCCUPATION_TYPE = 12
    elif OCCUPATION_TYPE == 'Secretaries':
        OCCUPATION_TYPE = 13
    elif OCCUPATION_TYPE == 'Low-skill Laborers':
        OCCUPATION_TYPE = 14
    elif OCCUPATION_TYPE == 'Realty agents':    
        OCCUPATION_TYPE = 15
    elif OCCUPATION_TYPE == 'HR staff':
        OCCUPATION_TYPE = 16
    elif OCCUPATION_TYPE == 'IT staff':
        OCCUPATION_TYPE = 17

    if HOUSETYPE_MODE == 'block of flats':
        HOUSETYPE_MODE = 0
    elif HOUSETYPE_MODE == 'specific housing':
        HOUSETYPE_MODE = 1
    elif HOUSETYPE_MODE == 'terraced house':
        HOUSETYPE_MODE = 2

    if CREDIT_ACTIVE == 'Closed':
        CREDIT_ACTIVE = 0
    elif CREDIT_ACTIVE == 'Sold':
        CREDIT_ACTIVE = 1

    if CREDIT_TYPE == 'Consumer credit':
        CREDIT_TYPE = 0
    elif CREDIT_TYPE == 'Credit card':
        CREDIT_TYPE = 1
    elif CREDIT_TYPE == 'Car loan':
        CREDIT_TYPE = 2
    elif CREDIT_TYPE == 'Microloan':
        CREDIT_TYPE = 3
    elif CREDIT_TYPE == 'Mortgage':
        CREDIT_TYPE = 4
    elif CREDIT_TYPE == 'Unknown type of loan':
        CREDIT_TYPE = 5

    if NAME_CONTRACT_TYPE == 'Cash loansConsumer loans':
        NAME_CONTRACT_TYPE = 0
    elif NAME_CONTRACT_TYPE == 'Cash loansCash loans':
        NAME_CONTRACT_TYPE = 1
    elif NAME_CONTRACT_TYPE == 'Revolving loansConsumer loans':
        NAME_CONTRACT_TYPE = 2

    if NAME_CONTRACT_STATUS == 'ApprovedActiveActive':
        NAME_CONTRACT_STATUS = 0
    elif NAME_CONTRACT_STATUS == 'ApprovedCompletedActive':
        NAME_CONTRACT_STATUS = 1
    elif NAME_CONTRACT_STATUS == 'ApprovedActiveCompleted':
        NAME_CONTRACT_STATUS = 2
    elif NAME_CONTRACT_STATUS == 'ApprovedSignedActive':
        NAME_CONTRACT_STATUS = 3
    elif NAME_CONTRACT_STATUS == 'ApprovedApprovedActive':
        NAME_CONTRACT_STATUS = 4
    elif NAME_CONTRACT_STATUS == 'ApprovedCompletedCompleted':
        NAME_CONTRACT_STATUS = 5
    elif NAME_CONTRACT_STATUS == 'ApprovedReturned to the storeActive':
        NAME_CONTRACT_STATUS = 6
    elif NAME_CONTRACT_STATUS == 'ApprovedActiveSigned':
        NAME_CONTRACT_STATUS = 7

    CNT_INSTALMENT = CNT_INSTALMENT

    AMT_INCOME_TOTAL = AMT_INCOME_TOTAL

    YEARS_ENTRY_PAYMENT = YEARS_ENTRY_PAYMENT

    EMPLOYED_TO_AGE_RATIO = EMPLOYED_TO_AGE_RATIO

    AMT_ANNUITY = AMT_ANNUITY 

    NUM_INSTALMENT_NUMBER = NUM_INSTALMENT_NUMBER

    YEARS_EMPLOYED = YEARS_EMPLOYED

    AMT_CREDIT = AMT_CREDIT 

    EXT_SOURCE_MEAN = EXT_SOURCE_MEAN

    # Making predictions 
    prediction = classifier.predict( 
        [[CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, OCCUPATION_TYPE, HOUSETYPE_MODE, CREDIT_ACTIVE, CREDIT_TYPE, NAME_CONTRACT_TYPE, NAME_CONTRACT_STATUS, CNT_INSTALMENT, AGE_YEARS, AMT_INCOME_TOTAL, YEARS_ENTRY_PAYMENT, EMPLOYED_TO_AGE_RATIO, AMT_ANNUITY, NUM_INSTALMENT_NUMBER, YEARS_EMPLOYED, AMT_CREDIT, EXT_SOURCE_MEAN]])

    if prediction == 0:
        pred = 'Default on repayment'
    else:
        pred = 'Repay'
    return pred


# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:white;padding:13px"> 
    <h1 style ="color:red;text-align:center;">Default Risk Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    # following lines create boxes in which user can enter data required to make prediction 
    AGE_YEARS = st.number_input("Input your Age")
    CODE_GENDER = st.selectbox('Gender',("M","F"))
    FLAG_OWN_CAR = st.selectbox('Do you have car? Yes(Y) or No(N)',('N','Y'))
    FLAG_OWN_REALTY = st.selectbox('Do you have house or flat? Yes(Y) or No(N)',('N','Y'))
    NAME_INCOME_TYPE = st.selectbox('Input your income type here:', ('Working', 'Commercial associate', 'State servant'))
    NAME_EDUCATION_TYPE = st.selectbox('Last Education:',('Secondary / secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Academic degree'))
    NAME_FAMILY_STATUS = st.selectbox('What is your Family Status?', ('Married', 'Single / not married', 'Civil marriage', 'Separated', 'Widow'))
    OCCUPATION_TYPE = st.selectbox('What kind of occupation you have?', ('Laborers', 'Sales staff', 'Managers','Core staff', 'Drivers', 'High skill tech staff', 'Security staff', 'Accountants', 'Medicine staff', 'Cooking staff', 'Cleaning staff', 'Private service staff', 'Low-skill Laborers', 'Secretaries', 'Waiters/barmen staff', 'Realty agents', 'HR staff', 'IT staff'))
    HOUSETYPE_MODE = st.selectbox('Where you live?', ('block of flats', 'specific housing', 'terraced house'))
    CREDIT_ACTIVE = st.selectbox('Last Credit Status', ('Closed', 'Sold'))
    CREDIT_TYPE = st.selectbox('What kind of credit do you have?', ('Consumer credit', 'Credit card', 'Car loan'))
    NAME_CONTRACT_TYPE = st.selectbox('Type of Contract Credit:', ('Cash loansConsumer loans', 'Cash loansCash loans', 'Revolving loansConsumer loans'))
    NAME_CONTRACT_STATUS = st.selectbox('Your Contract Status:', ('ApprovedActiveActive', 'ApprovedCompletedActive', 'ApprovedActiveCompleted', 'ApprovedSignedActive', 'ApprovedCompletedCompleted', 'ApprovedReturned to the storeActive', 'ApprovedActiveSigned'))
    CNT_INSTALMENT = st.number_input('How many installments in the previous loan')
    AMT_INCOME_TOTAL = st.number_input('Input your total income:')
    YEARS_ENTRY_PAYMENT = st.number_input('When was the installments of previous credit paid actually')
    EMPLOYED_TO_AGE_RATIO = st.number_input('The ratio of your employed years and your age')
    AMT_ANNUITY = st.number_input('Annuity of previous application') 
    NUM_INSTALMENT_NUMBER = st.number_input('On which installment do we observe payment')
    YEARS_EMPLOYED = st.number_input('How many years you have been employee before you Start this loans')
    AMT_CREDIT = st.number_input('Credit amount of the loan:')
    EXT_SOURCE_MEAN = st.number_input('The Average score from external data sources')
    result =""

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, OCCUPATION_TYPE, HOUSETYPE_MODE, CREDIT_ACTIVE, CREDIT_TYPE, NAME_CONTRACT_TYPE, NAME_CONTRACT_STATUS, CNT_INSTALMENT, AGE_YEARS, AMT_INCOME_TOTAL, YEARS_ENTRY_PAYMENT, EMPLOYED_TO_AGE_RATIO, AMT_ANNUITY, NUM_INSTALMENT_NUMBER, YEARS_EMPLOYED, AMT_CREDIT, EXT_SOURCE_MEAN) 
        st.success('Default Risk Prediction is {}'.format(result))

if __name__=='__main__':
    main()