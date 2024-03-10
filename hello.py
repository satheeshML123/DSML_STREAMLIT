import streamlit  as st

st.header("This is my first web app!")
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

code='''def cat():
print('Hello, Cat')'''
st.code(code, language='python')

cat=st.checkbot('Do you think this is Good')
if cat:
    st.write('Yes')