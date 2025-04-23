import streamlit as st
import re



st.title("Password Strength Checker🔒")
st.markdown("""
## Welcome to the ultimate  password strength checker!
🔐use this simple tool to check the strength of your password🔐""")

password = st.text_input("Enter your password!" , type="password")



feedback = []
score = 0
##button
if st.button("Check"):
    
    st.write("Checking!")
 
 ##for length
if password:
     if len(password) >=8:
        score +=1
else:
        feedback.append("Password should be at least 8 characters long")

##upper+lowercase
if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += 1
else:
            feedback.append("Password should contain both upper and lower case characters.")

##number
if re.search(r'\d', password):
            score += 1
else:
            feedback.append("Password should contain at least one number.")

##special character
if re.search(r'\d', password):
            score +=1
else:   
             feedback.append  ("Password should contain at least one special character(!@#$%*).") 

#final verdict
if score == 4:
    feedback.append("Your password is strong!💪")
elif score == 3:
    feedback.append("Your password is medium. Make it stronger.❌")
else:
    feedback.append("Your password is weak. Make it stronger.⚔️💀")


if feedback:
   st.markdown("##  Improvement Suggestions")
   for tip in feedback:
       st.write(tip)
else:
       st.warning("Please enter a password first.")