"""
IPO 일정 (예시 데이터, 이후 DART OpenAPI로 교체)
"""
import streamlit as st

from utils import load_csv, sample_badge, show_disclaimer

st.title("📅 IPO 일정")
st.caption("상장 예비심사 청구 → 승인 → 증권신고서 제출 → 공모주 청약 → 상장 순서로 진행돼요.")

st.dataframe(load_csv("sample_ipo.csv"), hide_index=True, use_container_width=True)
sample_badge()

show_disclaimer()
