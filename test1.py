import streamlit as st #Importing the Streamlit library
import os# Importing the os module for environment variable management

#Main function to run the Streanlit app.

def main():
    # Set page configurations
    st.set_page_config(page_title="PDF Summarizer")
    st.title("PDF Summarizing App") #Setting the title of the app
    st.write("Summarize your pdf files in just a few seconds.") # Displaying a description
    st.divider() #Inserting a divider for better layout

    # Creating a file uploader widget to upload PDF files

    pdf = st.file_uploader("Upload your PDF Document", type='pdf')
    # Creating a button for users to submit their PDF F sommarization
    submit= st.button("Generate Summary")
    #Python script execution starts here
    if __name__=='__main__':
        main() # Calling the main function to start the Streamlit app
