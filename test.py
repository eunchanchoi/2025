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
        {"name": "김치찌개", "image": "kimchi.jpeg"},
        {"name": "불고기", "image": "bulgogi.jpeg"},
        {"name": "비빔밥", "image": "bibimbap.jpg"},
        {"name": "삼겹살", "image": "samgyeopsal.jpeg"},
        {"name": "냉면", "image": "naegmyeon.jpeg"},
        {"name": "갈비찜", "image": "galbijjim.jpeg"},
        {"name": "떡볶이", "image": "tteokbokki.jpeg"},
        {"name": "국밥", "image": "gokbap.jpeg"},
        {"name": "김밥", "image": "gimbap.jpeg"},
        {"name": "순두부찌개", "image": "soondubu.jpeg"},
        {"name": "잡채", "image": "japchae.jpeg"},
        {"name": "제육볶음", "image": "jeyuk.jpeg"},
        {"name": "라면", "image": "ramyeon.jpeg"},
        {"name": "파전", "image": "pajeon.jpeg"},
        {"name": "삼계탕", "image": "samgyetang.jpeg"},
        {"name": "칼국수", "image": "kalguksu.jpeg"}
    ],
    "양식": [
        {"name": "스테이크", "image": "steak.jpeg"},
        {"name": "파스타", "image": "pasta.jpeg"},
        {"name": "피자", "image": "pizza.jpeg"},
        {"name": "햄버거", "image": "hamburger.jpeg"},
        {"name": "리조또", "image": "risotto.jpeg"},
        {"name": "샐러드", "image": "salad.jpeg"},
        {"name": "오믈렛", "image": "omelet.jpeg"},
        {"name": "샌드위치", "image": "sandwich.jpeg"},
        {"name": "치킨 윙", "image": "chicken.wing.jpeg"},
        {"name": "타코", "image": "taco.jpeg"},
        {"name": "부리또", "image": "burrito.jpeg"},
        {"name": "그라탱", "image": "gratin.jpeg"},
        {"name": "바게트", "image": "baguette.jpeg"},
        {"name": "크림수프", "image": "cream.soup.jpeg"},
        {"name": "퀘사디아", "image": "quesadilla.jpeg"},
        {"name": "라자냐", "image": "lasagna.jpeg"}
    ],
    "일식": [
        {"name": "초밥", "image": "sushi.jpeg"},
        {"name": "라멘", "image": "ramen.jpeg"},
        {"name": "우동", "image": "udon.jpeg"},
        {"name": "돈카츠", "image": "donkatsu.jpeg"},
        {"name": "텐동", "image": "tendon.jpeg"},
        {"name": "소바", "image": "soba.jpeg"},
        {"name": "야키토리", "image": "yakitori.jpeg"},
        {"name": "오니기리", "image": "onigiri.jpeg"},
        {"name": "가라아게", "image": "karaage.jpeg"},
        {"name": "규동", "image": "gyudon.jpeg"},
        {"name": "타코야키", "image": "takoyaki.jpeg"},
        {"name": "모츠나베", "image": "motsunabe.jpeg"},
        {"name": "카레라이스", "image": "curryrice.jpeg"},
        {"name": "나가사키 짬뽕", "image": "nagasakichampon.jpeg"},
        {"name": "스키야키", "image": "sukiyaki.jpeg"},
        {"name": "치라시", "image": "chirashi.jpeg"}
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
            if st.button(f"🥇 {food1['name']}", use_container_width=True, type="primary"):
                select_winner(food1)
            st.image(food1["image"], caption=food1["name"], use_container_width=True)
            
        
        with col2:
            if st.button(f"🥇 {food2['name']}", use_container_width=True, type="primary"):
                select_winner(food2)
    
            st.image(food2["image"], caption=food2["name"], use_container_width=True)
            
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
        st.markdown(f"### 🥇 {winner['name']}")
        st.image(winner["image"], caption=f"👑 {winner['name']}", use_container_width=True)
        
    
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
