import sys

import streamlit as st
from transcription import transcribe
from summarize import summary


st.title('Get a quick summary of your today\'s lecture')
st.subheader('Start by uploading an audio file you need _summarized_ :blue[below]  :books:')
uploaded_file = st.file_uploader("Choose a file")
if st.button('Transcribe audio'):
    if uploaded_file is not None:
        if sys.getsizeof(uploaded_file) > 10485760:
            raise Exception('Incorrect audio size')
        try:
            # read file as bytes:
            bytes_data = uploaded_file.getvalue()
            transcription = transcribe(bytes_data)
            st.write(f'{transcription}')
            st.button('Summarize this !')
            summ = summary(transcription)
            st.write(f'{summ}')

        finally:
            st.write('Try again')
