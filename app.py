import streamlit as st
import re

#Title
st.title("🔒Password Strength Meter")

#Description
st.markdown("""
            Welcome to the **Ultimate Password Strength Checker!**
            Ensure your password is secure by checking:
            - ✅Length
            - ✅Upper and Lowercase letters
            - ✅Numbers
            - ✅Special characters

          >  🟦*Improve your online security by creating strong password!*
            """)

#Input
password = st.text_input("Enter your password:", type="password")

#🟥Password Strength Check
def check_password_strength(password):
     score = 0
     feedback = []

     # Length Check
     if len(password) <= 8:
                score += 1
     else:
         feedback.append("Password should be at least **8 characters** long.")
        
     # Check for Upper and Lowercase 
     if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += 1
     else:
            feedback.append("Password should contain **both uppercase and lowercase** letters.")

     #🟡Digit Check
     if re.search(r'\d', password):
          score += 1
     else:
          feedback.append("Password should contain at least **one digitnumber (0-9)**.")

     # 🈯special character check
     if re.search(r"[!@#$%^&*]",password):
                score += 1
     else:
         feedback.append("Password should contain at least **one special character(!@#$%^&*)**.")

     return score, feedback

            
     # ⏺ Button to check Password
if st.button("check Password Strength"):
  if password:
           score, feedback = check_password_strength(password)

           st.subheader("Password Strength Result:")

           if score == 4:
                    st.success("Your password is strong!")
           elif score == 3:
                    st.warning("Your password is moderate. Consider adding more complexity.")
           else:
                    st.error("Your password is weak. Please improve it.")

           if feedback:
                     st.info("Suggestions to improve your password:")
                     for suggestion in feedback:
                         st.write("suggestion")
           else:
            st.error("Please enter a password to check its strength.")

 #          Footer
st.markdown("""
 ---
by **Samra Waseem**
""")
st.success

               