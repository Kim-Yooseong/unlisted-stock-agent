"""
홈 (첫 화면)
① 검색창 ② 플랫폼 바로가기 ③ IPO 일정 ④ 주목 종목 / 거래 TOP 5
⑤ 최신 비상장 뉴스 ⑥ 사기 주의 배너 + 면책 문구
"""
import streamlit as st

from utils import PLATFORMS, load_csv, sample_badge, show_disclaimer

st.title("📈 비상장 주식투자 도움 에이전트")
st.caption("출처가 확실한 자료로 비상장 기업 정보를 브리핑해 드립니다.")

# ① 검색창 → 질문을 AI 브리핑 페이지로 넘김
with st.form("search_form", border=False):
    col_input, col_btn = st.columns([5, 1], vertical_alignment="bottom")
    question = col_input.text_input(
        "궁금한 비상장 종목이나 질문",
        placeholder="요즘 주목받는 AI 비상장 기업 알려줘",
        label_visibility="collapsed",
    )
    submitted = col_btn.form_submit_button("AI에게 묻기", use_container_width=True)
if submitted and question.strip():
    st.session_state["pending_question"] = question.strip()
    st.switch_page("pages/ai_briefing.py")

# ② 거래·정보 플랫폼 바로가기 (카드 전체가 링크)
st.subheader("거래·정보 플랫폼 바로가기")
cols = st.columns(4)
for col, p in zip(cols, PLATFORMS):
    col.markdown(
        f"""
<a href="{p['url']}" target="_blank" style="text-decoration:none; color:inherit;">
  <div style="border:1px solid rgba(128,128,128,0.25); border-radius:12px; padding:16px; height:150px;">
    <div style="font-size:28px;">{p['icon']}</div>
    <div style="font-weight:600; font-size:17px; margin:4px 0;">{p['name']} ↗</div>
    <span style="background:{p['badge_color']}; color:{p['badge_text']}; font-size:12px;
                 padding:2px 8px; border-radius:6px;">{p['badge']}</span>
    <div style="font-size:13px; opacity:0.75; margin-top:8px;">{p['desc']}</div>
  </div>
</a>
""",
        unsafe_allow_html=True,
    )

st.write("")

# ③ IPO 일정 / ④ 주목 종목·거래 TOP 5
left, right = st.columns(2)

with left:
    with st.container(border=True):
        st.markdown("#### 📅 다가오는 IPO 일정")
        ipo = load_csv("sample_ipo.csv").head(4)
        for _, row in ipo.iterrows():
            st.markdown(f"**{row['날짜']}** · {row['기업']} — {row['단계']}")
        sample_badge()
        st.page_link("pages/ipo.py", label="전체 일정 보기 →")

with right:
    with st.container(border=True):
        view = st.segmented_control(
            "보기", ["주목 종목", "거래 TOP 5"], default="주목 종목",
            label_visibility="collapsed",
        )
        if view == "거래 TOP 5":
            st.markdown("#### 📊 이번 주 거래 TOP 5")
            rank = load_csv("sample_ranking.csv")
            rank = rank[rank["플랫폼"] == "K-OTC"].head(5)
            for _, row in rank.iterrows():
                st.markdown(f"**{row['순위']}위** · {row['기업']} — 거래대금 {row['거래대금(억원)']}억원")
            st.caption("거래대금 기준 순위이며 투자 추천이 아닙니다.")
            sample_badge()
            st.page_link("pages/market.py", label="시장 현황 보기 →")
        else:
            st.markdown("#### 🗂️ 이번 주 주목 종목")
            stocks = load_csv("sample_stocks.csv").head(4)
            for _, row in stocks.iterrows():
                st.markdown(f"**{row['기업']}** · {row['섹터']} · {row['투자단계']}")
            sample_badge()
            st.page_link("pages/stock_cards.py", label="종목 카드 보기 →")

# ⑤ 최신 비상장 뉴스 (네이버 뉴스 검색 API 연결 예정, 받은 그대로 표시)
with st.container(border=True):
    st.markdown("#### 📰 최신 비상장 뉴스")
    news = load_csv("sample_news.csv")
    keyword = st.segmented_control(
        "키워드", ["비상장", "IPO", "장외주식", "K-OTC"], default="비상장",
        label_visibility="collapsed",
    ) or "비상장"
    for _, row in news[news["키워드"] == keyword].iterrows():
        st.markdown(f"- [{row['제목']}]({row['링크']}) · {row['언론사']} · {row['날짜']}")
    st.caption("뉴스 제목과 링크는 네이버 뉴스 검색 결과를 가공 없이 보여줄 예정이에요. (현재 예시)")

# ⑥ 사기 주의 배너
st.warning(
    "전화·문자·리딩방에서 권유하는 장외주식은 사기일 수 있어요. "
    "거래 전 기업 실체와 정식 플랫폼 등록 여부를 꼭 확인하세요.",
    icon="🚨",
)

show_disclaimer()
