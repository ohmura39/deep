import streamlit as st
import pandas as pd

# Streamlitのページ設定
st.set_page_config(page_title="Deep Data Analysis", layout="wide")

# タイトルと説明を表示
st.title("Deep Data Analysis with Streamlit")
st.write("This is a sample Streamlit app to demonstrate data analysis.")

# ファイルアップロード機能
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    # CSVデータを読み込み
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded data:", data.head())
    
    # データの基本統計量を表示
    st.write("Data Description:", data.describe())
