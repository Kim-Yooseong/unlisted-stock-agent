"""
여러 페이지에서 같이 쓰는 기능 모음
"""
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).parent / "data"

# 거래·정보 플랫폼 4곳 (링크는 새 창으로 열림)
PLATFORMS = [
    {
        "name": "Npay 비상장",
        "icon": "🟢",
        "desc": "구 증권플러스 비상장 · 제휴 증권사 계좌로 거래",
        "badge": "사설 거래 플랫폼",
        "badge_color": "#E1F5EE",
        "badge_text": "#085041",
        "url": "https://www.ustockplus.com",
    },
    {
        "name": "서울거래 비상장",
        "icon": "🔵",
        "desc": "금융위 지정 혁신금융서비스 · NH·신한 계좌로 거래",
        "badge": "사설 거래 플랫폼",
        "badge_color": "#E1F5EE",
        "badge_text": "#085041",
        "url": "https://www.seoulexchange.kr",
    },
    {
        "name": "K-OTC",
        "icon": "🏛️",
        "desc": "금융투자협회 운영 · 국내 유일 제도권 장외시장",
        "badge": "제도권 시장",
        "badge_color": "#EEEDFE",
        "badge_text": "#3C3489",
        "url": "https://www.k-otc.or.kr",
    },
    {
        "name": "38커뮤니케이션",
        "icon": "📰",
        "desc": "장외 시세·IPO 정보 · 개인 간 직거래 게시판 주의",
        "badge": "정보·게시판",
        "badge_color": "#F1EFE8",
        "badge_text": "#444441",
        "url": "https://www.38.co.kr",
    },
]

DISCLAIMER = (
    "본 서비스의 정보는 투자 판단을 위한 참고 자료이며, 특정 종목의 매수·매도를 권유하지 않습니다. "
    "비상장주식은 원금 손실 위험이 크며, 투자에 대한 책임은 투자자 본인에게 있습니다."
)


@st.cache_data
def load_csv(name: str) -> pd.DataFrame:
    """data 폴더의 CSV 파일을 읽어 표(DataFrame)로 돌려줍니다."""
    return pd.read_csv(DATA_DIR / name)


# 페이지 맨 아래에 작게 보여줄 참고 사이트
REFERENCE_SITES = [
    {"name": "THE VC", "url": "https://thevc.kr"},
]


def show_disclaimer():
    """페이지 맨 아래 면책 문구와 참고 사이트"""
    st.divider()
    st.caption("⚠️ " + DISCLAIMER)
    links = " · ".join(f"[{s['name']} ↗]({s['url']})" for s in REFERENCE_SITES)
    st.caption(f"참고 사이트: {links}")


def sample_badge():
    """예시 데이터임을 알려주는 작은 표시"""
    st.caption("🧪 예시 데이터입니다. 실제 데이터로 교체할 예정이에요.")


def coming_soon(title: str, icon: str, items: list[str]):
    """아직 만들지 않은 페이지에 공통으로 보여줄 안내"""
    st.title(f"{icon} {title}")
    st.info("이 페이지는 준비 중이에요. 아래 내용이 들어갈 예정입니다.")
    for item in items:
        st.markdown(f"- {item}")
    show_disclaimer()
