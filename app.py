"""
비상장 주식투자 도움 에이전트 - 시작 파일
Streamlit 실행: streamlit run app.py
상단 메뉴(내비게이션)와 페이지 목록을 여기서 정합니다.
"""
import streamlit as st

st.set_page_config(
    page_title="비상장 주식투자 도움 에이전트",
    page_icon="📈",
    layout="wide",
)

# 상단 메뉴에 보일 페이지 목록 (순서대로 표시됨)
pages = [
    st.Page("pages/home.py", title="홈", icon="🏠", default=True),
    st.Page("pages/ai_briefing.py", title="AI 브리핑", icon="💬"),
    st.Page("pages/stock_cards.py", title="종목 카드", icon="🗂️"),
    st.Page("pages/market.py", title="시장 현황", icon="📊"),
    st.Page("pages/ipo.py", title="IPO 일정", icon="📅"),
    st.Page("pages/risk_tax.py", title="리스크·세금", icon="⚠️"),
    st.Page("pages/guide.py", title="투자 가이드", icon="📚"),
]

nav = st.navigation(pages, position="top")
nav.run()
