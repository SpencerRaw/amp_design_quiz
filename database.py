# import streamlit as st  # pip install streamlit
# from deta import Deta  # pip install deta
# import os
# from dotenv import load_dotenv


import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta


# Load the environment variables
DETA_KEY = st.secrets["DETA_KEY"]

# Initialize with a project key
deta = Deta(DETA_KEY)

# Load the environment variables

# load_dotenv(".env")
# DETA_KEY = os.getenv("DETA_KEY")
# # Initialize with a project key
# deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("amp_ques")


def insert_period(period, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,a24):
    return db.put({"key": period, "research_year": a1, "number_aa": a2, "二级重要": a3, "二级含混": a4, "带电重要": a5, "带电含混": a6, "疏水重要": a7, "疏水含混": a8, "极性重要": a9, "极性含混": a10, "封端": a11, "排名": a12, "二级重要补充": a13, "二级含混补充": a14, "带电重要补充": a15, "带电含混补充": a16, "带电范围": a17, "疏水重要补充": a18, "疏水含混补充": a19, "疏水比例": a20, "极性重要补充": a21, "极性含混补充": a22, "重要片段": a23,"研究手法":a24})


# def insert_period(period, incomes, expenses, comment):
    # """Returns the report on a successful creation, otherwise raises an error"""
    # return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)
