import pandas as pd
import warnings
import streamlit as st
warnings.filterwarnings('ignore')

@st.cache_data(show_spinner=False)
def data_preprocessing(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name = sheet_name, skiprows = 1, header = None)

    #df = df.drop(df.columns[0], axis = 1)

    df = df.iloc[:, [2, 3, 4, 5, 6, 7, 8]]

    df = df.dropna()

    column_names = ['Line', 'LKDB', 'LKKTTR', 'HT', 'NN', 'NNG', 'Group']

    df.columns = column_names

    df['HT'] = df['HT'].astype(float).astype(int).astype(str)
    df['NN'] = df['NN'].astype(float).astype(int).astype(str)
    df['NNG'] = df['NNG'].astype(float).astype(int).astype(str)

    df = df.astype(str)

    return df