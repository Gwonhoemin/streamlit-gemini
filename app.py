import streamlit as st
from google import genai
from pathlib import Path


def get_file_content(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"파일을 읽는 중 오류가 발생했습니다: {e}"


def ask_model(client: genai.Client, file_content: str, question: str) -> str:
    # 한국어로 동작하는 수산물 전문가 역할 로프롬프트를 구성합니다.
    prompt = (
        "너는 한국 수산물과 수산물 시장, 어종 분류, 신선도 판별, 보관/조리법, 계절별 수요와 가격 동향 등을 잘 아는 수산물 전문가 어시스턴트야."
        "사용자가 수산물 관련 질문을 하면 친절하고 구체적으로 답해줘. 필요한 경우 추천 조리법, 보관 팁, 유통 과정 설명, 안전한 섭취 여부 판단 기준 등을 포함해줘."
        "응답은 한국어로 해주고, 가능하면 핵심 요약과 자세한 설명(순서대로)을 제공해줘.\n\n"
        f"사용자 질문:\n{question}\n\n"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return getattr(response, "text", str(response))


def main():
    st.title("수산물 도우미")

    if "GEMINI_API_KEY" not in st.secrets:
        st.error("GEMINI_API_KEY가 Streamlit secrets에 설정되어 있지 않습니다.")
        return

    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    file_path = Path(__file__).resolve()
    file_content = get_file_content(file_path)

    with st.expander("`app.py` 내용 (클릭하여 보기)"):
        st.code(file_content, language="python")

    if "history" not in st.session_state:
        st.session_state.history = []  # list of (role, text)

    question = st.text_input("이 파일에 대해 질문하세요:")
    if st.button("질문하기"):
        if not question.strip():
            st.warning("질문을 입력해 주세요.")
        else:
            st.session_state.history.append(("user", question))
            with st.spinner("모델 응답 생성 중..."):
                try:
                    answer = ask_model(client, file_content, question)
                except Exception as e:
                    answer = f"모델 호출 중 오류가 발생했습니다: {e}"
                st.session_state.history.append(("assistant", answer))

    # 채팅 형식으로 히스토리 출력
    for role, text in st.session_state.history:
        if role == "user":
            st.markdown(f"**질문:** {text}")
        else:
            st.markdown("**답변:**")
            st.code(text)

    st.caption("이 앱은 로컬 `app.py` 파일 내용을 기반으로 질문에 답합니다. `GEMINI_API_KEY`는 Streamlit secrets에 설정되어야 합니다.")


if __name__ == '__main__':
    main()