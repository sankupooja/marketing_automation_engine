import sqlite3
import pandas as pd 
import streamlit as st
import db_manager as dbm
import harvester
import processor

def data_load():

    with sqlite3.connect(dbm.get_db_path()) as conn:
        df=pd.read_sql_query("select * from headlines",conn)
        df.drop_duplicates("title",inplace=True)
        st.dataframe(df)
        df["captured_at"]=pd.to_datetime(df["captured_at"])
        daily_sentiment=df.groupby(df['captured_at'].dt.date)['sentiment'].mean()
        st.line_chart(daily_sentiment)
    

    

def main()-> None:
    st.title("Sentiment Dashboard")

    if st.button("Refresh Data"):
        harvester.main()
        processor.main()
        st.success("Data updated")

    data_load()



if __name__=="__main__":
    main()
