import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Cyril")
    content = """
    wieurkthcngisruktgrhncvwilseudrhgcvmxsileuhr
    $sdkrjg,hcvxsoetdihmcgsvd
    sxiduhkgcvrotlhbonrflxihcbgcdoriflxgn!
    """
    st.info(content)

content2 = """
eirfkhjnwelrnfvleisdutfnvliseuthnvlresuitbfnvilrsutbkvfnlsiudbkfvnslidtukbfvsdvlkfnj
"""
st.info(content2)

col3, empty_col, col4 = st.columns([1.5, 0.3, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Dat as e Link]({row['url']})")

with col4:
     for index, row in df[10:].iterrows():
         st.header(row["title"])
         st.image("images/" + row["image"])
         st.write(row["description"])
         st.write(f"[Dat as e Link]({row['url']})")