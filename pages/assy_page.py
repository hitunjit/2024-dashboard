import streamlit as st
from data.DataPreprocessing import data_preprocessing
from figure.chart import create_bar_chart
from utils.constants import ma_hien_tuong, ma_nguyen_nhan, ma_nguyen_nhan_goc, ma_linh_kien

st.set_page_config(layout = "wide", initial_sidebar_state = "expanded")

file_path = "./BMFY24.xlsx"

df = data_preprocessing(file_path, "ASSY")


ba_df = df[df['LKDB'].str.startswith('BA')]
be_df = df[df['LKDB'].str.startswith('BE')]
bm_df = df[df['LKDB'].str.startswith('BM')]

st.header('Linh Kiện Đồng Bộ')

col1, col2, col3 = st.columns(3)

with col1:
    figure_ba = create_bar_chart(ba_df, 'LKDB', ma_linh_kien, 'BA')
    st.plotly_chart(figure_ba, use_container_width=True, key = 'bar_ba')

with col2:
    figure_be = create_bar_chart(be_df, 'LKDB', ma_linh_kien, 'BE')
    st.plotly_chart(figure_be, use_container_width=True, key = 'bar_be')

with col3:
    figure_bm = create_bar_chart(bm_df, 'LKDB', ma_linh_kien, 'BM')
    st.plotly_chart(figure_bm, use_container_width=True, key = 'bar_bm')


st.header('Linh Kiện Không Thể Tách Rời')

a_df = df[df['LKKTTR'].str.startswith('A')]
e_df = df[df['LKKTTR'].str.startswith('E')]
m_df = df[df['LKKTTR'].str.startswith('M')]

col4, col5, col6 = st.columns(3)

with col4:
    figure_a = create_bar_chart(a_df, 'LKKTTR', ma_linh_kien, 'BA')
    st.plotly_chart(figure_a, use_container_width=True, key = 'bar_a')

with col5:
    figure_e = create_bar_chart(e_df, 'LKKTTR', ma_linh_kien, 'BE')
    st.plotly_chart(figure_e, use_container_width=True, key = 'bar_e')

with col6:
    figure_m = create_bar_chart(m_df, 'LKKTTR', ma_linh_kien, 'BM')
    st.plotly_chart(figure_m, use_container_width=True, key = 'bar_m')