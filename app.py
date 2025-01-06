import streamlit as st
from src.summarizer_functions import summarize

st.set_page_config(page_title = 'Research Article Summarizer', layout = 'centered')

st.title('Research Article Summarizer')
st.write('This app is a simple research article summarizer. Just paste a research article URL in PDF format and the app will generate a summary for you.')

url = st.text_input('Enter the URL of the research article in PDF format', placeholder = 'https://')

if st.button('Summarize'):
    if url:
        try:
            with st.spinner('Summarizing the article...'):
                summary = summarize(url)
            st.markdown('### Final Summary:')
            st.markdown(summary)
        except Exception as e:
            st.error(f'An error occurred: {str(e)}')
    else:
        st.warning('Please enter a valid URL to summarize.')
        

st.write('---')
st.write('Created by [Kamil Stachurski](https://www.linkedin.com/in/kamroki/)')