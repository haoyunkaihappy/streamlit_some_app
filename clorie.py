import streamlit as st

st.set_page_config(layout="wide")


def daixie_cal(gender, year, weight, high):
    if gender == '男':
        result = 13.7 * weight/2 + 5 * high - 6.8 * year + 66
    elif gender == '女':
        result = 9.6 * weight/2 + 1.8 * high - 4.7 * year + 655
    return result

row0_1, row0_2, row0_3, row0_4, row0_5 = st.columns([1, 2, 1, 2, 1])
with row0_3:
    st.markdown('''
    ## 小工具
    ''')
row1_1, row1_2, row1_3, row1_4 = st.columns([1, 2, 2, 1])
with row1_3:
    want_lose = st.number_input('你想要减重多少？（斤）', value=0.0)

with row1_2:
    calorie_per_g = st.number_input('假设条件：1g脂肪提供热量（千卡）', value=9.46, min_value=0.00)
    lose_calorie = int(calorie_per_g * 500 * want_lose)
    markdown_1 = "你需要消耗**{}千卡**热量！".format(lose_calorie)
    st.markdown(markdown_1)

row2_1_1, row1_2_1, row1_3_1, row1_4_1 = st.columns([1, 2, 2, 1])
with row1_2_1:
    st.markdown("#### 计算基础代谢：")

row2_1, row2_2, row2_3, row2_4, row2_5, row2_6 = st.columns([2, 2, 2, 2, 2, 2])

with row2_3:
    year = st.number_input('年龄', value=18, min_value=0)
with row2_4:
    weight = st.number_input('体重（斤）', value=135.0, min_value=0.0)
with row2_5:
    high = st.number_input('身高（厘米）', value=175.0, min_value=0.0)
with row2_2:
    gender = st.selectbox("性别", ("男", "女"), index=0)

row3_1, row3_2, row3_3, row3_4 = st.columns([1, 2, 2, 1])
with row3_2:
    fundamental_need = int(daixie_cal(gender, year, weight, high))
    markdown_2 = "你的基础代谢：**{}千卡**！".format(fundamental_need)
    st.markdown(markdown_2)
    markdown_3 = "如果放弃吃饭，**{}天**就可以减肥成功！".format(int(lose_calorie/fundamental_need))
    st.markdown(markdown_3)

row4_1, row4_2, row4_3, row4_4 = st.columns([1, 2, 2, 1])
with row4_2:
    st.markdown("#### 每日摄入热量：")
    st.markdown("点击查询各类食物卡路里(https://www.boohee.com/food)")
    input_calorie = st.number_input('每日摄入量（千卡）', value=0.0, min_value=0.0)

row5_1, row5_2, row5_3, row5_4 = st.columns([1, 2, 2, 1])
with row4_2:
    st.markdown("#### 每日消耗热量：")
    st.markdown("点击查询各类运动卡路里(https://zhuanlan.zhihu.com/p/260515747)")

    output_calorie = st.number_input('每日消耗量（千卡）', value=0.0, min_value=0.0)

    net_calorie = (output_calorie+fundamental_need-input_calorie)

    markdown_4 = "**{}天**就可以减肥成功！".format(int(lose_calorie/net_calorie))
    st.markdown(markdown_4)
