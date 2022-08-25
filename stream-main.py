import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

import streamlit as st
import streamlit.components.v1 as stc
import streamlit_ace as st_ace
import json
from functools import reduce
import pdb

dictionary = "{{ dic|safe }}";
url_search = "{% url 'search' %}";

languMenu = ['English',"Mandarin","Korean","Cantonese","Hindy","French","Russia","Spanish","Dutch","Italy"]
lang =['en','zh-Hans','ko',     'yue','hi','fr','ru','es','de','it']
speaklang =['en','zh-cn','ko','zh-HK','hi','fr','ru','es','de','it']

padding_top = 1
padding_bottom = 1
padding_left = 1
padding_right = 1

st.set_page_config(
    page_title="Patentfield 教師データ作成支援ツール",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown(f'''
            <style>
            .appview-container .main .block-container{{
        padding-top: {padding_top}rem;    }}
                .reportview-container .sidebar-content {{
                    padding-top: {padding_top}rem;
                }}
                .reportview-container .main .block-container {{
                    padding-top: {padding_top}rem;
                    padding-right: {padding_right}rem;
                    padding-left: {padding_left}rem;
                    padding-bottom: {padding_bottom}rem;
                }}
            </style>
            ''', unsafe_allow_html=True,
            )

st.sidebar.title("Select Language you want")

st.title("Multi Language Dictionary")


try:
    options = st.sidebar.multiselect(
    'Select classification target label',
    languMenu,    default=[])

    st.sidebar.table(options)

    user_choosen = ['location']
    df = st.session_state['df'] 
   
    df_ = df[options]
    st.session_state['df_']=df_
except:
    pass

button = st.button('Search')
country=st.text_input('Word')

if 'df' not in st.session_state:

    #jsonファイルを使って認証情報を取得
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    c = ServiceAccountCredentials.from_json_keyfile_name("refined-sum-258500-b793bf2339c3.json")#‘ダウンロードしたjsonファイル’, scope)

    #認証情報を使ってスプレッドシートの操作権を取得
    gs = gspread.authorize(c)

    #共有したスプレッドシートのキー（後述）を使ってシートの情報を取得
    SPREADSHEET_KEY = "1sUSzKvBfm8mUoplq24V7JuAw2QO882b61AOe3sA-T-0"
    worksheet = gs.open_by_key(SPREADSHEET_KEY).worksheet("test")

    df = pd.DataFrame(worksheet.get_all_values())
    df.columns = list(df.loc[0, :])
    df.drop(0, inplace=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
    st.session_state['df'] = df
#if st.sidebar.button("Change JSON", key=0):
#  st.session_state["count"] += 1

tab2, tab1 = st.tabs(
    ["Selected","Master"])

with tab1:
    if 'df' in st.session_state:    
        st.session_state['df'] = df

        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_grid_options(rowHeight=30)
        gb.configure_pagination()
        gridOptions = gb.build()

        AgGrid(df, theme="blue",
           height=800,
           gridOptions=gridOptions,
           fit_columns_on_grid_load=True
           )

with tab2:
    if 'df_' in st.session_state:
        st.session_state['df_']=df_
        gb2 = GridOptionsBuilder.from_dataframe(df_)
        gb2.configure_grid_options(rowHeight=30)
        gb2.configure_pagination()
        gridOptions2 = gb2.build()

        AgGrid(df, theme="blue",
           height=800,
           gridOptions=gridOptions2,
           fit_columns_on_grid_load=True
           )