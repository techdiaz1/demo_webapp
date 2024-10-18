import streamlit as st

# Function to display account balance
def check_balance():
    st.write(f"Your current balance is: ${st.session_state.balance}")

# Function to deposit money
def deposit(amount):
    st.session_state.balance += amount
    st.write(f"${amount} deposited successfully!")
    check_balance()

# Function to withdraw money
def withdraw(amount):
    if amount > st.session_state.balance:
        st.error("Insufficient balance!")
    else:
        st.session_state.balance -= amount
        st.write(f"${amount} withdrawn successfully!")
        check_balance()

# Streamlit app layout
def main():
    st.title("Simple Bank Application")
    st.sidebar.title("Menu")

    # Initialize balance in session_state if it doesn't exist
    if 'balance' not in st.session_state:
        st.session_state.balance = 1000  # Initial balance

    menu = ["Check Balance", "Deposit", "Withdraw"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Check Balance":
        st.subheader("Check your balance")
        check_balance()

    elif choice == "Deposit":
        st.subheader("Deposit Money")
        amount = st.number_input("Enter deposit amount", min_value=1)
        if st.button("Deposit"):
            deposit(amount)

    elif choice == "Withdraw":
        st.subheader("Withdraw Money")
        amount = st.number_input("Enter withdrawal amount", min_value=1)
        if st.button("Withdraw"):
            withdraw(amount)

# Running the app
if __name__ == '__main__':
    main()
