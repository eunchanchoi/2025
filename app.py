import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="🍜 음식 이상형 월드컵", layout="wide")
st.title("🍜 음식 이상형 월드컵")

# 음식 데이터 (이름, 이미지 경로)
foods = [
    ("비빔밥", "images.bibim.jpg"),
    ("비빔밥", "images.bossam.jpg"),
    ("불고기", "images.bulgogi.jpg"),
    ("치킨", "images.chicken.jpg"),
    ("된장찌개", "images.doenjang.jpg"),
    ("갈비찜", "images.galbijjim.jpg"),
    ("감자탕", "images.gamjatang.jpg"),
    ("김밥", "images.gimpbap.jpg"),
    ("곱창구이", "images.gopchang.jpg"),
    ("잡채", "images.japchae.jpg"),
    ("제육볶음", "images.jeyuk.jpg"),
    ("족발", "images.jokbal.jpg"),
    ("김치찌개", "images.kimchi.jpg"),
    ("냉면", "images.naengmyeon.jpg"),
    ("파전", "images.pajeon.jpg"),
    ("삼겹살", "images.samgyepsal.jpg"),
    ("삼계탕", "images.samgyetang.jpg"),
    ("순두부찌개", "images.sundubu.jpg"),
    ("떡볶이", "images.tteokbokki.jpg"),
    ("해물탕", "images.haemultang.jpg"),
]

# 세션 상태 초기화
if "round_foods" not in st.session_state:
    st.session_state.round_foods = random.sample(foods, len(foods))
    st.session_state.next_round = []
    st.session_state.stage = 1
    st.session_state.round_num = len(st.session_state.round_foods)
    st.session_state.total_round = len(st.session_state.round_foods)

# CSS 애니메이션 스타일
st.markdown("""
<style>
.choice-img {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}
.choice-img:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 15px rgba(255, 165, 0, 0.7);
}
.fade-out {
    animation: fadeOut 0.5s forwards;
}
@keyframes fadeOut {
    to {
        opacity: 0;
        transform: scale(0.8);
    }
}
</style>
""", unsafe_allow_html=True)

# 진행 중일 때
if st.session_state.stage == 1:
    # 진행률 표시
    progress = (1 - len(st.session_state.round_foods) / st.session_state.total_round) * 100
    st.progress(progress / 100)

    st.subheader(f"⚡ {st.session_state.round_num}강")

    if len(st.session_state.round_foods) >= 2:
        col1, col2 = st.columns(2)
        food1 = st.session_state.round_foods[0]
        food2 = st.session_state.round_foods[1]

        def select_food(food):
            # 선택 애니메이션 효과
            st.session_state.selected_food = food
            time.sleep(0.3)
            st.session_state.next_round.append(food)
            st.session_state.round_foods = st.session_state.round_foods[2:]

        with col1:
            if st.button(food1[0]):
                select_food(food1)
            st.image(food1[1], caption=food1[0], use_container_width=True, output_format="auto")

        with col2:
            if st.button(food2[0]):
                select_food(food2)
            st.image(food2[1], caption=food2[0], use_container_width=True, output_format="auto")

    else:
        st.session_state.round_foods = st.session_state.next_round
        st.session_state.next_round = []
        st.session_state.round_num = len(st.session_state.round_foods)

        if len(st.session_state.round_foods) == 1:
            st.session_state.stage = 2
        else:
            st.experimental_rerun()

# 우승자 화면
elif st.session_state.stage == 2:
    winner = st.session_state.round_foods[0]
    st.success("🎉 최종 우승!")
    st.image(winner[1], caption=winner[0], use_container_width=True)
    st.markdown(f"**🏆 {winner[0]}** 우승!")

    if st.button("다시 시작하기"):
        st.session_state.clear()
        st.experimental_rerun()

