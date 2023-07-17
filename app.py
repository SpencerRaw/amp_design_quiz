import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
# import calendar  # Core Python Module
# from datetime import datetime  # Core Python Module
# pip install streamlit-option-menu
from streamlit_option_menu import option_menu
import database as db
import time
import pandas as pd
import datetime


# -------------- SETTINGS --------------
# incomes = ["Salary", "Blog", "Other Income"]
# expenses = ["Rent", "Utilities", "Groceries",
#             "Car", "Other Expenses", "Saving"]
# currency = "USD"
page_title = "以:red[破坏细胞膜为抗菌机制]的多肽序列设计问卷"
page_title_raw = "以破坏细胞膜为抗菌机制的多肽序列设计问卷"
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
page_icon = "🧑‍🔬"
layout = "centered"
# --------------------------------------


st.set_page_config(page_title=page_title_raw,
                   page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# st.markdown('Streamlit is **_really_ cool**.')
# st.markdown(
#     "This text is :red[colored red], and this is **:blue[colored]** and bold.")
# st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

# progress_text = "进度条"
# my_bar = st.progress(0, text=progress_text)
pg_now = 0
my_bar = st.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")

# for percent_complete in range(100):
#     time.sleep(0.1)
# my_bar.progress(percent_complete + 1, text=progress_text)


# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
# years = [datetime.today().year, datetime.today().year + 1]
# months = list(calendar.month_name[1:])


research_year = ['待选择', "1-3年", "3-5年(含3年)", "5-10年(含5年)", "≥10年"]

# my_bar = st.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")
# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# with st.form("entry_form", clear_on_submit=True):
col_my = st.selectbox("0.1您从事此类研究的时间经历大约多长时间？:red[(必填)]",
                      research_year, key="research_year")

if col_my != '待选择':
    pg_now += 1
    my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")
  
col_my_2 = st.selectbox("0.2您主要采用哪些研究手段开展此类研究？:red[(必填)]",
                      ["待选择","实验","模拟","两者结合"], key="研究手法")

if col_my_2 != '待选择':
    pg_now += 1
    my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")

with st.expander(f"1.多肽结构"):
    q11 = st.number_input(f"1.1您觉得此类多肽的残基至少要多少个？:red[(必填)]", min_value=0,
                          format="%i", step=1, key="number_aa")
    if q11 != 0:
        pg_now += 1
        my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")

    q12 = st.multiselect(
        '1.2您觉得哪些:red[二级结构]对此类多肽的抗菌性能的影响程度:red[比较重要]？:red[(必填,可多选)]',
        ['Alpha helix', 'Beta sheet', '其他', '都没有'],
        [], key="二级重要")
    # st.write('您觉得还有哪些二级结构对此类多肽的抗菌性能的影响程度比较重要？(选填)')
    if '其他' in q12:
        q121 = st.text_area("您觉得还有哪些:red[二级结构]对此类多肽的抗菌性能的影响程度:red[比较重要]？(选填)",
                            placeholder="您觉得比较重要的二级结构补充 ...", key="二级重要补充")
    else:
        st.session_state["二级重要补充"] = None
    q122 = st.multiselect(
        '您觉得哪些二级结构对此类多肽的抗菌性能的影响程度:red[说不清楚]？:red[(必填,可多选)]',
        ['Alpha helix', 'Beta sheet', '其他', '都没有'],
        [], key="二级含混")
    if '其他' in q122:
        # st.write('您觉得还有哪些二级结构对此类多肽的抗菌性能的影响程度比较重要？(选填)')
        q123 = st.text_area("您觉得还有哪些:red[二级结构]对此类多肽的抗菌性能的影响程度说:red[不清楚]？(选填)",
                            placeholder="您觉得说不清楚的二级结构补充 ...", key="二级含混补充")
    else:
        st.session_state["二级含混补充"] = None
    if q12 and q122:
        pg_now += 1
        my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")

with st.expander(f"2.带电性"):
    q21 = st.multiselect(
        '2.1您觉得哪些:red[带电残基]对此类多肽的抗菌性能的影响程度:red[比较重要]？:red[(必填,可多选)]',
        ["Asp(D)", "Glu(E)", "His(H)", "Cys(C)",
            "Tyr(Y)", "Lys(K)", "Arg(R)", '其他', '都没有'],
        [], key="带电重要")
# st.write('您觉得还有哪些二级结构对此类多肽的抗菌性能的影响程度比较重要？(选填)')
    if '其他' in q21:
        q211 = st.text_area("您觉得还有哪些:red[带电残基]对此类多肽的抗菌性能的影响程度:red[比较重要]？(选填)",
                            placeholder="您觉得比较重要的带电残基补充 ...", key="带电重要补充")
    else:
        st.session_state["带电重要补充"] = None
    q212 = st.multiselect(
        '您觉得哪些:red[带电残基]对此类多肽的抗菌性能的影响程度:red[说不清楚]？:red[(必填,可多选)]',
        ["Asp(D)", "Glu(E)", "His(H)", "Cys(C)",
            "Tyr(Y)", "Lys(K)", "Arg(R)", '其他', '都没有'],
        [], key="带电含混")
    if '其他' in q212:
        # st.write('您觉得还有哪些二级结构对此类多肽的抗菌性能的影响程度比较重要？(选填)')
        q213 = st.text_area("您觉得还有哪些:red[带电残基]对此类多肽的抗菌性能的影响程度:red[说不清楚]？(选填)",
                            placeholder="您觉得说不清楚的带电残基补充 ...", key="带电含混补充")
    else:
        st.session_state["带电含混补充"] = None
    if q21 and q212:
        pg_now += 1
        my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")

    q22 = st.slider(
        '2.2 您觉得多肽:red[带电量]范围是多少？(可不填)',
        -10, 10, (-10, 10), key="带电范围")
    if q22[0] != -10 or q22[1] != 10:
        pg_now += 1
        my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")

with st.expander(f"3.疏水性"):
    q31 = st.multiselect(
        '3.1您觉得哪些:red[疏水残基]对此类多肽的抗菌性能的影响程度:red[比较重要]？:red[(必填,可多选)]',
        ["Trp(W)", "Ile(I)", "Leu(L)", "Phe(F)", "Val(V)", "Tyr(Y)",
            "Ala(A)", "Gly(G)", "Met(M)", "Pro(P)", '其他', '都没有'],
        [], key="疏水重要")
# st.write('您觉得还有哪些二级结构对此类多肽的抗菌性能的影响程度比较重要？(选填)')
    if '其他' in q31:
        q311 = st.text_area("您觉得还有哪些:red[疏水残基]对此类多肽的抗菌性能的影响程度:red[比较重要]？(选填)",
                            placeholder="您觉得比较重要的疏水残基补充 ...", key="疏水重要补充")
    else:
        st.session_state["疏水重要补充"] = None
    q312 = st.multiselect(
        '您觉得哪些:red[疏水残基]对此类多肽的抗菌性能的影响程度:red[说不清楚]？:red[(必填,可多选)]',
        ["Trp(W)", "Ile(I)", "Leu(L)", "Phe(F)", "Val(V)", "Tyr(Y)",
            "Ala(A)", "Gly(G)", "Met(M)", "Pro(P)", '其他', '都没有'],
        [], key="疏水含混")
    if '其他' in q312:
        # st.write('您觉得还有哪些二级结构对此类多肽的抗菌性能的影响程度比较重要？(选填)')
        q313 = st.text_area("您觉得还有哪些:red[疏水残基]对此类多肽的抗菌性能的影响程度:red[说不清楚]？(选填)",
                            placeholder="您觉得说不清楚的疏水残基补充 ...", key="疏水含混补充")
    else:
        st.session_state["疏水含混补充"] = None
    if q31 and q312:
        pg_now += 1
        my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")
    q32 = st.slider('3.2您觉得疏水残基在肽链所占的比例要多少？(可不填)',
                    0.0, 100.0, 0.0, key="疏水比例")

with st.expander(f"4.极性"):
    q41 = st.multiselect(
        '2.1您觉得哪些:red[极性残基]对此类多肽的抗菌性能的影响程度:red[比较重要]？:red[(必填,可多选)]',
        ["Cys(C)", "Asp(D)", "Glu(E)", "His(H)", "Lys(K)", "Asn(N)",
            "Gln(Q)", "Arg(R)", "Ser(S)", "Thr(T)", "Tyr(Y)", '其他', '都没有'],
        [], key="极性重要")
# st.write('您觉得还有哪些二级结构对此类多肽的抗菌性能的影响程度比较重要？(选填)')
    if '其他' in q41:
        q411 = st.text_area("您觉得还有哪些:red[极性残基]对此类多肽的抗菌性能的影响程度:red[比较重要]？(选填)",
                            placeholder="您觉得比较重要的极性残基补充 ...", key="极性重要补充")
    else:
        st.session_state["极性重要补充"] = None
    q412 = st.multiselect(
        '您觉得哪些:red[极性残基]对此类多肽的抗菌性能的影响程度:red[说不清楚]？:red[(必填,可多选)]',
        ["Cys(C)", "Asp(D)", "Glu(E)", "His(H)", "Lys(K)", "Asn(N)",
            "Gln(Q)", "Arg(R)", "Ser(S)", "Thr(T)", "Tyr(Y)", '其他', '都没有'],
        [], key="极性含混")
    if '其他' in q412:
        # st.write('您觉得还有哪些二级结构对此类多肽的抗菌性能的影响程度比较重要？(选填)')
        q413 = st.text_area("您觉得还有哪些:red[极性残基]对此类多肽的抗菌性能的影响程度:red[说不清楚]？(选填)",
                            placeholder="您觉得说不清楚的极性残基补充 ...", key="极性含混补充")
    else:
        st.session_state["极性含混补充"] = None
    if q41 and q412:
        pg_now += 1
        my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")

with st.expander(f"5.封端"):
    q51 = st.multiselect(
        '5.1您觉得:red[封端]对多肽抗菌性能的影响程度如何？若重要,在设计多肽时您会采取下列哪种封端方式？:red[(必填,可多选)]',
        ["N端封端", "C端封端", "两端均封端", "两端均不封端"],
        [], key="封端")

    if q51:
        pg_now += 1
        my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")

# 带电性	二级结构	长度	疏水性	极性	芳香基团	侧链大小
df = pd.DataFrame(
    [
        {"氨基酸属性": "带电性", "排名": 1},
        {"氨基酸属性": "二级结构", "排名": 1},
        {"氨基酸属性": "长度", "排名": 1},
        {"氨基酸属性": "疏水性", "排名": 1},
        {"氨基酸属性": "极性", "排名": 1},
        {"氨基酸属性": "芳香基团", "排名": 1},
        {"氨基酸属性": "侧链大小", "排名": 1}
    ]
)
with st.expander(f"6.补充"):
    st.markdown(
        f"6.1请您对不同氨基酸属性对多肽抗菌性能的影响程度进行排序:red[(从低到高进行排序,1为最重要;排序可并列)]。若您觉得还有其他氨基酸属性很重要可在表格下方添加。:red[(必填)]")
    edited_df = st.data_editor(df, num_rows="dynamic", key="排名")
    if edited_df["排名"].max() > 1:
        pg_now += 1
        my_bar.progress(pg_now*10, text=f"当前进度为: {pg_now}/10")

    p62 = st.text_area("6.2您是否觉得是否有哪些氨基酸的序列片段对此类多肽的设计比较重要？若有请举例（可不填）。",
                       placeholder="重要的氨基酸序列片段 ...", key="重要片段")
with st.form("entry_form", clear_on_submit=True):
    submitted = st.form_submit_button("提交")
    if submitted:
        ts = time.time()
        period = datetime.datetime.fromtimestamp(
            ts).strftime('%Y-%m-%d %H:%M:%S')
        db.insert_period(period, st.session_state["research_year"], st.session_state["number_aa"], st.session_state["二级重要"], st.session_state["二级含混"], st.session_state["带电重要"], st.session_state["带电含混"], st.session_state["疏水重要"], st.session_state["疏水含混"], st.session_state["极性重要"], st.session_state["极性含混"], st.session_state["封端"],
                         st.session_state["排名"], st.session_state["二级重要补充"], st.session_state["二级含混补充"], st.session_state["带电重要补充"], st.session_state["带电含混补充"], st.session_state["带电范围"], st.session_state["疏水重要补充"], st.session_state["疏水含混补充"], st.session_state["疏水比例"], st.session_state["极性重要补充"], st.session_state["极性含混补充"], st.session_state["重要片段"],st.session_state["研究手法"])
        st.success("保存成功!")
        st.markdown('非常感谢您抽出时间参与我们的多肽设计问卷调查。您的意见对于我们深入研究抗菌肽的性能与设计具有重要的价值。如果您对我们的研究感兴趣并希望了解更多相关信息，我们将非常乐意与您分享研究结果。再次衷心感谢您的参与和支持！')
    # st.write(st.session_state[)
