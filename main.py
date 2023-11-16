import streamlit as st
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Streamlit UI for file upload
st.title('Upload Files to S3')

uploaded_file = st.file_uploader("Choose a file", type=['mp4'])

if uploaded_file is not None:
    st.write("File Uploaded!")
    
    # Get the file name
    file_name = uploaded_file.name
    
    # Upload the file to S3
    try:
        s3.upload_fileobj(uploaded_file, 'event-driven-arch-videos', file_name)
        st.success("File successfully uploaded to S3!")
    except Exception as e:
        st.error(f"Error uploading file: {e}")
