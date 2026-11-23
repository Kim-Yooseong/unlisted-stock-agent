"""
AI 브리핑 (대화형 에이전트)
3주차에 Gemini API를 연결할 예정입니다. 지금은 화면 틀만 있습니다.
"""
import streamlit as st

from utils import show_disclaimer

st.title("💬 AI 브리핑")
st.caption("질문하면 ① 종목 요약 → ② 리포트 핵심 → ③ 거래 플랫폼 → ④ 주의사항 순서로 답해 드려요.")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 홈 화면 검색창에서 넘어온 질문 처리
pending = st.session_state.pop("pending_question", None)
if pending:
    st.session_state["messages"].append({"role": "user", "content": pending})
    st.session_state["messages"].append(
        {"role": "assistant", "content": "AI 연결을 준비 중이에요. 곧 실제 브리핑으로 답해 드릴게요."}
    )

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("궁금한 비상장 종목이나 질문을 입력하세요"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.session_state["messages"].append(
        {"role": "assistant", "content": "AI 연결을 준비 중이에요. 곧 실제 브리핑으로 답해 드릴게요."}
    )
    st.rerun()

show_disclaimer()
