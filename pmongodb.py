import streamlit as st
import pymongo

# Initialize connection.
# Uses st.experimental_singleton to only run once.
# @st.experimental_singleton

# uri = "mongodb+srv://mtuong:Wellcome2@oucru-it.bcq3ord.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(**st.secrets["mongo"])

try:
    st.write(client.server_info())
except Exception:
    st.write("Unable to connect to the server.")

# Pull data from the collection.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def get_data():
    db = client.InkMgmt
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.experimental_memo
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['beds']}:")
