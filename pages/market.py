"""
시장 현황 - 거래소별 순위 (예시 데이터)
"""
import streamlit as st

from utils import load_csv, sample_badge, show_disclaimer

st.title("📊 시장 현황")
st.caption("거래 플랫폼별로 많이 거래된 종목을 보여줍니다. 매주 직접 확인해 기준일과 함께 업데이트할 예정이에요.")

rank = load_csv("sample_ranking.csv")
platform = st.segmented_control(
    "플랫폼", ["K-OTC", "Npay 비상장", "서울거래 비상장"], default="K-OTC"
) or "K-OTC"

st.dataframe(
    rank[rank["플랫폼"] == platform].drop(columns=["플랫폼"]),
    hide_index=True,
    use_container_width=True,
)
st.caption("거래대금 기준 순위이며 투자 추천이 아닙니다. 38커뮤니케이션은 게시판 형태라 순위에서 제외했어요.")
sample_badge()

show_disclaimer()
