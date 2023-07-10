import sys

import streamlit as st
from transcription import transcribe
from summarize import summary

def active_transcribe(uploaded_file):
    # read file as bytes:
    bytes_data = uploaded_file.getvalue()
    transcription = transcribe(bytes_data)
    st.write(f'{transcription}')
    return transcription

st.title('Get a quick summary of your today\'s lecture')
st.subheader('Start by uploading an audio file you need _summarized_ :blue[below]  :books:')
uploaded_file = st.file_uploader("Choose a file")

if st.button('Transcribe audio'):
    if uploaded_file is not None:
        if sys.getsizeof(uploaded_file) > 10485760:
            raise Exception('Incorrect audio size')
        try:
            transcription = active_transcribe(uploaded_file)
            if transcription is not None:
                st.button('Summarize this !')
                summ = summary(transcription)
                st.write(f'{summ}')
        finally:
            st.write('All done')
    else:
        st.warning('Please upload a file')
