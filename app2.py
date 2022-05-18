import streamlit as st


st.title("나의 검색기록")
st.write("그동안 내가 검색한 단어 목록을 보여줍니다.")
input = st.text_input("검색어를 쓰세요")
st.write(input)


#list=[]
#while True:
#  input = st.text_input("검색어를 쓰세요")
#  if len(list)<31:
#   list.append(input)
#    st.write(list)
