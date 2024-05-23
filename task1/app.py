import pickle
import pandas as pd
import streamlit as st

filename = '/content/drive/MyDrive/saved_models/treeleaf2.pkl'

with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)


# Sample data (replace with actual user input)
data = {
    "Age": 30,
    "Experience": "5 years",
    "Income": "$75,000",
    "Family": "Married with 2 children",
    "CCAvg": "$1,500",
    "Education": "Bachelor's degree",
    "Mortgage": "Yes",
    "Home Ownership": "Own",
    "Securities Account": "Yes",
    "CD Account": "No",
    "Online": "Yes",
    "CreditCard": "Yes"
}

# Chatbot response
#print("Welcome! Thanks for sharing your information. Here's a general overview of your financial profile:")

# Print each data point
#for key, value in data.items():
    #print(f"{key}: {value}")

#prompt = st.chat_input("Say something")
#if prompt:
#    st.write(f"User has sent the following prompt: {prompt}")

#import streamlit as st

# Initialize session state to store user data and conversation step
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'step' not in st.session_state:
    st.session_state.step = 0

# Define questions and corresponding keys
questions = [
    ("What's your age?", 'Age'),
    ("How many years of experience do you have?", 'Experience'),
    ("What's your income?", 'Income'),
    ("Tell us about your family (e.g., Married with 2 children).", 'Family'),
    ("What's your average monthly credit card spending?", 'CCAvg'),
    ("What's your highest level of education?", 'Education'),
    ("Do you have a mortgage?", 'Mortgage'),
    ("Do you own or rent your home?", 'Home Ownership'),
    ("Do you have a securities account?", 'Securities Account'),
    ("Do you have a Certificate of Deposit (CD) account?", 'CD Account'),
    ("Do you use online banking?", 'Online'),
    ("Do you have a credit card?", 'CreditCard')
]

# Display title
st.title("User Data Collection Chatbot")

Home = ['Home Owner','Rent','Home Mortage']


# Display the current question based on the conversation step
if st.session_state.step < len(questions):
    question, key = questions[st.session_state.step]
    prompt = st.chat_input(f"{question}")

    if prompt:
        # Store the user's answer
        st.session_state.user_data[key] = prompt
        # Move to the next question
        st.session_state.step += 1

        # Display the new prompt to avoid taking input multiple times
        st.experimental_rerun()

# Once all questions are answered, display the collected data
if st.session_state.step >= len(questions):
    st.write("Thanks for providing your information!")
    st.write("Here is the data you provided:")
    st.json(st.session_state.user_data)
    
    # Button to reset the chat
    if st.button("Restart"):
        st.session_state.step = 0
        st.session_state.user_data = {}
        st.experimental_rerun()

    st.session_state.user_data['Home Ownership'] = Home.index(st.session_state.user_data['Home Ownership'])

    X_input = pd.DataFrame.from_dict([st.session_state.user_data])
    X_input.index = ["User 1"]  # Setting a custom index

    X_input = X_input.astype(float)

    loan_prediction = loaded_model.predict(X_input)

        #['Home Owner', 'Rent', 'Home Mortage']
    if loan_prediction == 0:
      st.write("Loan not approved")
    
    else :
      st.write("Loan approved")
    st.write(loan_prediction)
        #loan_prediction = loaded_model.predict(X_input)

        #Home Ownership



#st.write("Loan Prediction:", loan_prediction)

# Additional message based on specific data points
#if data["Mortgage"] == "Yes" and data["Income"] == "$75,000":
    #print("\nConsidering your mortgage and income, you might be interested in exploring options for optimizing your interest rates.")

#print("\nThis is a basic analysis. Please consult with a financial advisor for personalized recommendations.")


# Verify by making a prediction
#predictions = loaded_model.predict(X_test)
#print(predictions)


