import streamlit as st
import os 
st.set_page_config(
    page_title="Lost and Found Matcher",
    page_icon="🔍",
    layout="wide"
)
import pandas as pd

st.title("🔍 Lost & Found Portal")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Report Lost Item", "Report Found Item", "Search Items"]
)

if menu == "Report Lost Item":

    st.header("Report Lost Item")

    item = st.text_input("Item Name")
    desc = st.text_input("Description")
    location = st.text_input("Location Lost")
    date = st.date_input("Date Lost")
    contact = st.text_input("Contact")

    if st.button("Submit Lost Report"):

        new_data = pd.DataFrame(
            [[item, desc, location, date, contact]],
            columns=["ItemName","Description","Location","Date","Contact"]
        )

        new_data.to_csv(
            "lost_items.csv",
            mode="a",
            header=False,
            index=False
        )

        st.success("Lost Item Report Submitted!")

elif menu == "Report Found Item":

    st.header("Report Found Item")

    item = st.text_input("Item Name")
    desc = st.text_input("Description")
    location = st.text_input("Location Found")
    date = st.date_input("Date Found")
    contact = st.text_input("Contact")

    if st.button("Submit Found Report"):

        new_data = pd.DataFrame(
            [[item, desc, location, date, contact]],
            columns=["ItemName","Description","Location","Date","Contact"]
        )

        new_data.to_csv(
            "found_items.csv",
            mode="a",
            header=False,
            index=False
        )

        st.success("Found Item Report Submitted!")

elif menu == "Search Items":

    st.header("Search Items")

    search = st.text_input("Enter Item Name")

    if search:

        lost = pd.read_csv("lost_items.csv")
        found = pd.read_csv("found_items.csv")

        st.subheader("Lost Items")
        st.dataframe(
            lost[lost["ItemName"].str.contains(search, case=False, na=False)]
        )

        st.subheader("Found Items")
        st.dataframe(
            found[found["ItemName"].str.contains(search, case=False, na=False)]
        )
