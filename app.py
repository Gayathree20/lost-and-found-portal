import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Lost and Found Matcher",
    page_icon="🔍",
    layout="wide"
)

# Create CSV files if they don't exist
if not os.path.exists("lost_items.csv"):
    pd.DataFrame(
        columns=["ItemName", "Description", "Location", "Date", "Contact"]
    ).to_csv("lost_items.csv", index=False)

if not os.path.exists("found_items.csv"):
    pd.DataFrame(
        columns=["ItemName", "Description", "Location", "Date", "Contact"]
    ).to_csv("found_items.csv", index=False)


st.title("🔍 Lost & Found Portal")

st.write(
    """
    Welcome to the Lost & Found Matcher! 👜📱

    This website helps students report lost items,
    report found items, and search for missing belongings easily.

    Use the sidebar to get started 👈
    """
)

menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Report Lost Item",
        "Report Found Item",
        "Search Items"
    ]
)


# Report Lost Item
if menu == "Report Lost Item":

    st.header("📝 Report Lost Item")

    item = st.text_input("Item Name")
    desc = st.text_input("Description")
    location = st.text_input("Location Lost")
    date = st.date_input("Date Lost")
    contact = st.text_input("Contact")

    if st.button("Submit Lost Report"):

        new_data = pd.DataFrame(
            [[item, desc, location, date, contact]],
            columns=[
                "ItemName",
                "Description",
                "Location",
                "Date",
                "Contact"
            ]
        )

        new_data.to_csv(
            "lost_items.csv",
            mode="a",
            header=False,
            index=False
        )

        st.success("✅ Lost Item Report Submitted!")


# Report Found Item
elif menu == "Report Found Item":

    st.header("📦 Report Found Item")

    item = st.text_input("Item Name")
    desc = st.text_input("Description")
    location = st.text_input("Location Found")
    date = st.date_input("Date Found")
    contact = st.text_input("Contact")

    if st.button("Submit Found Report"):

        new_data = pd.DataFrame(
            [[item, desc, location, date, contact]],
            columns=[
                "ItemName",
                "Description",
                "Location",
                "Date",
                "Contact"
            ]
        )

        new_data.to_csv(
            "found_items.csv",
            mode="a",
            header=False,
            index=False
        )

        st.success("✅ Found Item Report Submitted!")


# Search Items
elif menu == "Search Items":

    st.header("🔍 Search Items")

    search = st.text_input("Enter Item Name")

    if search:

        lost = pd.read_csv("lost_items.csv")
        found = pd.read_csv("found_items.csv")

        st.subheader("Lost Items")

        st.dataframe(
            lost[
                lost["ItemName"]
                .str.contains(search, case=False, na=False)
            ]
        )

        st.subheader("Found Items")

        st.dataframe(
            found[
                found["ItemName"]
                .str.contains(search, case=False, na=False)
            ]
        )
