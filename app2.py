import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from pytrends.request import TrendReq

# get google trends data from keyword list
@st.cache
def get_data(keyword):
    keyword = [keyword]
    pytrend = TrendReq(hl='KR', tz=540)
    pytrend.build_payload(kw_list=keyword)
    df = pytrend.interest_over_time()
    df.drop(columns=['isPartial'], inplace=True)
    df.reset_index(inplace=True)
    df.columns = ["날짜 및 기간(주)", "검색량"]
    return df

# sidebar
st.sidebar.write("## 구글 검색량 확인하기")
keyword = st.sidebar.text_input("검색어를 입력하세요.", help="구글 트렌드로 확인하는 검색량입니다.")

if keyword:
    df = get_data(keyword)
    st.dataframe(df)
    fig, ax = plt.subplots()
    ax = df['검색량'].plot()
    st.pyplot(fig)
