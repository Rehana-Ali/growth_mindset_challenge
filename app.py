# import streamlit as st
# import random

# # Custom CSS for styling and responsiveness
# st.markdown("""
#     <style>
#         .main {
#             background-color: #f0f2f6;
#         }
#         h1 {
#             text-align: center;
#             color: #333;
#         }
#         .container {
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#         }
#         .button-container {
#             display: flex;
#             gap: 10px;
#             justify-content: center;
#             margin-top: 20px;
#         }
#         .result {
#             text-align: center;
#             font-size: 20px;
#             font-weight: bold;
#             margin-top: 20px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Game logic
# def get_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == "Rock" and computer_choice == "Scissors") or \
#          (user_choice == "Paper" and computer_choice == "Rock") or \
#          (user_choice == "Scissors" and computer_choice == "Paper"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# # Streamlit UI
# st.title("Growth Mindset Challenge Using Streamlit")
# st.title("Rock, Paper, Scissors Game")
# st.header("Play against the Computer")

# choices = ["Rock", "Paper", "Scissors"]
# user_choice = st.radio("Choose one:", choices, horizontal=True)

# if st.button("Play"):
#     computer_choice = random.choice(choices)
#     result = get_winner(user_choice, computer_choice)
    
#     st.write(f"### You chose: {user_choice}")
#     st.write(f"### Computer chose: {computer_choice}")
#     st.write(f'<p class="result">{result}</p>', unsafe_allow_html=True)

#     st.markdown("<h4 style 'text-align: center; color: #ff4757;'>Made by Rehana Ali</h4>", unsafe_allow_html=True)



import streamlit as st
import random

# Custom styles for Streamlit app
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        width: 100%;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #ff4757 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title and instructions
st.markdown("<h1 style='text-align: center; color: #ff4757;'>Growth Mindset Challeng Using Streamlit</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ff4757;'>🪨📜✂️ Rock, Paper, Scissors Game</h1>", unsafe_allow_html=True)
st.write("### 🤖 Play against the Computer!")

# User choice selection
choices = ["Rock ✊", "Paper 📜", "Scissors ✂️"]
user_choice = st.selectbox("👉 Select your move:", choices)

# Play button logic
if st.button("🔥 Play Now!"):
    computer_choice = random.choice(choices)

    # Extract text without emojis
    user_choice_clean = user_choice.split(" ")[0]  
    computer_choice_clean = computer_choice.split(" ")[0]

    # Determine the result
    if user_choice_clean == computer_choice_clean:
        result = "😮 It's a tie!"
    elif (
        (user_choice_clean == "Rock" and computer_choice_clean == "Scissors") or
        (user_choice_clean == "Paper" and computer_choice_clean == "Rock") or
        (user_choice_clean == "Scissors" and computer_choice_clean == "Paper")
    ):
        result = "🎉 You win!"
    else:
        result = "😢 Computer wins!"

    # Display the choices and result
    st.write(f"**🧑 You chose:** {user_choice}")
    st.write(f"**💻 Computer chose:** {computer_choice}")
    st.markdown(f"<h2 style='text-align: center; color: #ff4757;'>{result}</h2>", unsafe_allow_html=True)

# Footer
st.markdown("<h4 style='text-align: center; color: #ff4757;'>Made with ❤️ by Rehana Ali</h4>", unsafe_allow_html=True)
