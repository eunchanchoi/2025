import streamlit as st
import random
from typing import List, Dict

# 페이지 설정
st.set_page_config(
    page_title="음식 이상형 월드컵",
    page_icon="🍽️",
    layout="wide"
)

# 음식 데이터 (로컬 이미지 사용)
FOOD_DATA = {
    "한식": [
        {"name": "김치찌개", "image": "kimchi"},
        {"name": "불고기", "image": "images/korean/bulgogi.jpg"},
        {"name": "비빔밥", "image": "images/korean/bibimbap.jpg"},
        {"name": "삼겹살", "image": "images/korean/samgyeopsal.jpg"},
        {"name": "냉면", "image": "images/korean/naengmyeon.jpg"},
        {"name": "갈비", "image": "images/korean/galbi.jpg"},
        {"name": "떡볶이", "image": "images/korean/tteokbokki.jpg"},
        {"name": "치킨", "image": "images/korean/chicken.jpg"},
        {"name": "김밥", "image": "images/korean/kimbap.jpg"},
        {"name": "순두부찌개", "image": "images/korean/sundubu_jjigae.jpg"},
        {"name": "잡채", "image": "images/korean/japchae.jpg"},
        {"name": "제육볶음", "image": "images/korean/jeyuk_bokkeum.jpg"},
        {"name": "된장찌개", "image": "images/korean/doenjang_jjigae.jpg"},
        {"name": "막국수", "image": "images/korean/makguksu.jpg"},
        {"name": "족발", "image": "images/korean/jokbal.jpg"},
        {"name": "보쌈", "image": "images/korean/bossam.jpg"}
    ],
    "양식": [
        {"name": "스테이크", "image": "images/western/steak.jpg"},
        {"name": "파스타", "image": "images/western/pasta.jpg"},
        {"name": "피자", "image": "images/western/pizza.jpg"},
        {"name": "햄버거", "image": "images/western/hamburger.jpg"},
        {"name": "리조또", "image": "images/western/risotto.jpg"},
        {"name": "샐러드", "image": "images/western/salad.jpg"},
        {"name": "오믈렛", "image": "images/western/omelet.jpg"},
        {"name": "샌드위치", "image": "images/western/sandwich.jpg"},
        {"name": "치킨 윙", "image": "images/western/chicken_wing.jpg"},
        {"name": "타코", "image": "images/western/taco.jpg"},
        {"name": "부리또", "image": "images/western/burrito.jpg"},
        {"name": "그라탱", "image": "images/western/gratin.jpg"},
        {"name": "바게트", "image": "images/western/baguette.jpg"},
        {"name": "크림수프", "image": "images/western/cream_soup.jpg"},
        {"name": "퀘사디아", "image": "images/western/quesadilla.jpg"},
        {"name": "라자냐", "image": "images/western/lasagna.jpg"}
    ],
    "일식": [
        {"name": "초밥", "image": "images/japanese/sushi.jpg"},
        {"name": "라멘", "image": "images/japanese/ramen.jpg"},
        {"name": "우동", "image": "images/japanese/udon.jpg"},
        {"name": "돈카츠", "image": "images/japanese/donkatsu.jpg"},
        {"name": "텐동", "image": "images/japanese/tendon.jpg"},
        {"name": "소바", "image": "images/japanese/soba.jpg"},
        {"name": "야키토리", "image": "images/japanese/yakitori.jpg"},
        {"name": "오니기리", "image": "images/japanese/onigiri.jpg"},
        {"name": "가라아게", "image": "images/japanese/karaage.jpg"},
        {"name": "규동", "image": "images/japanese/gyudon.jpg"},
        {"name": "타코야키", "image": "images/japanese/takoyaki.jpg"},
        {"name": "모츠나베", "image": "images/japanese/motsu_nabe.jpg"},
        {"name": "카레라이스", "image": "images/japanese/curry_rice.jpg"},
        {"name": "나가사키 짬뽕", "image": "images/japanese/nagasaki_champon.jpg"},
        {"name": "스키야키", "image": "images/japanese/sukiyaki.jpg"},
        {"name": "치라시", "image": "images/japanese/chirashi.jpg"}
    ]
}

def init_session_state():
    """세션 상태 초기화"""
    if 'page' not in st.session_state:
        st.session_state.page = 'category_selection'
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = None
    if 'tournament_foods' not in st.session_state:
        st.session_state.tournament_foods = []
    if 'current_round' not in st.session_state:
        st.session_state.current_round = 16
    if 'current_match' not in st.session_state:
        st.session_state.current_match = 0
    if 'winners' not in st.session_state:
        st.session_state.winners = []
    if 'final_winner' not in st.session_state:
        st.session_state.final_winner = None

def category_selection_page():
    """카테고리 선택 페이지"""
    st.title("🍽️ 음식 이상형 월드컵")
    st.markdown("### 어떤 음식 종류로 월드컵을 진행하시겠어요?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🍚 한식", use_container_width=True, type="primary"):
            start_tournament("한식")
    
    with col2:
        if st.button("🍝 양식", use_container_width=True, type="primary"):
            start_tournament("양식")
    
    with col3:
        if st.button("🍣 일식", use_container_width=True, type="primary"):
            start_tournament("일식")

def start_tournament(category: str):
    """토너먼트 시작"""
    st.session_state.selected_category = category
    st.session_state.tournament_foods = FOOD_DATA[category].copy()
    random.shuffle(st.session_state.tournament_foods)
    st.session_state.current_round = 16
    st.session_state.current_match = 0
    st.session_state.winners = []
    st.session_state.page = 'tournament'
    st.rerun()

def tournament_page():
    """토너먼트 페이지"""
    foods = st.session_state.tournament_foods
    current_round = st.session_state.current_round
    current_match = st.session_state.current_match
    
    # 현재 라운드 제목
    round_names = {16: "16강", 8: "8강", 4: "4강", 2: "결승", 1: "우승"}
    st.title(f"🏆 {st.session_state.selected_category} 이상형 월드컵 - {round_names[current_round]}")
    
    # 진행 상황 표시
    total_matches = current_round // 2
    st.progress((current_match) / total_matches)
    st.write(f"경기 진행: {current_match + 1}/{total_matches}")
    
    # 현재 대결할 두 음식
    if current_match < len(foods) // 2:
        food1 = foods[current_match * 2]
        food2 = foods[current_match * 2 + 1]
        
        st.markdown("### 더 좋아하는 음식을 선택하세요!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(food1["image"], caption=food1["name"], use_container_width=True)
            if st.button(f"🥇 {food1['name']}", use_container_width=True, type="primary"):
                select_winner(food1)
        
        with col2:
            st.image(food2["image"], caption=food2["name"], use_container_width=True)
            if st.button(f"🥇 {food2['name']}", use_container_width=True, type="primary"):
                select_winner(food2)
    
    # 홈으로 돌아가기 버튼
    if st.button("🏠 처음으로 돌아가기"):
        reset_tournament()

def select_winner(winner_food: Dict):
    """승자 선택 처리"""
    st.session_state.winners.append(winner_food)
    st.session_state.current_match += 1
    
    # 현재 라운드가 끝났는지 확인
    if st.session_state.current_match >= len(st.session_state.tournament_foods) // 2:
        if st.session_state.current_round == 2:
            # 결승 끝남 - 최종 우승자 결정
            st.session_state.final_winner = winner_food
            st.session_state.page = 'result'
        else:
            # 다음 라운드로 진행
            st.session_state.tournament_foods = st.session_state.winners.copy()
            st.session_state.current_round = st.session_state.current_round // 2
            st.session_state.current_match = 0
            st.session_state.winners = []
    
    st.rerun()

def result_page():
    """결과 페이지"""
    winner = st.session_state.final_winner
    
    st.balloons()
    st.title("🎉 축하합니다!")
    st.markdown(f"## 🏆 {st.session_state.selected_category} 이상형 월드컵 우승자")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(winner["image"], caption=f"👑 {winner['name']}", use_container_width=True)
        st.markdown(f"### 🥇 {winner['name']}")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 다시 하기", use_container_width=True, type="primary"):
            restart_same_category()
    
    with col2:
        if st.button("🏠 처음으로", use_container_width=True):
            reset_tournament()

def restart_same_category():
    """같은 카테고리로 다시 시작"""
    category = st.session_state.selected_category
    start_tournament(category)

def reset_tournament():
    """토너먼트 초기화"""
    st.session_state.page = 'category_selection'
    st.session_state.selected_category = None
    st.session_state.tournament_foods = []
    st.session_state.current_round = 16
    st.session_state.current_match = 0
    st.session_state.winners = []
    st.session_state.final_winner = None
    st.rerun()

def main():
    """메인 함수"""
    init_session_state()
    
    # 현재 페이지에 따라 다른 화면 표시
    if st.session_state.page == 'category_selection':
        category_selection_page()
    elif st.session_state.page == 'tournament':
        tournament_page()
    elif st.session_state.page == 'result':
        result_page()

if __name__ == "__main__":
    main()
