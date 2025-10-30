# streamlit-gemini

간단한 Streamlit 기반 데모 앱으로, 로컬 환경에서 실행 가능한 최소 예제 프로젝트입니다.

## 개요

`streamlit-gemini`는 Streamlit 앱 템플릿으로 빠르게 프로토타입을 만들고 테스트할 수 있도록 구성된 프로젝트입니다. 주요 파일은 `app.py`이며, `requirements.txt`에 필요한 패키지 목록이 포함되어 있습니다.

## 특징

- Streamlit으로 빠르게 웹 UI 실행
- 최소한의 의존성으로 로컬에서 즉시 실행 가능

## 기술 스택

- Python 3.8+
- Streamlit — 빠른 웹 UI 구성 및 데모 실행용 프레임워크 (`streamlit`)
- Google Generative AI (google-genai) — 필요한 경우 Gemini/생성형 AI 연동용 (`google-genai`)


## 요구사항

- Python 3.8 이상
- `requirements.txt`에 명시된 패키지들

## 설치 및 실행

1. 저장소 복제 또는 해당 디렉터리로 이동

2. 가상환경 생성(권장) 및 패키지 설치:

```bash
# macOS (zsh)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Streamlit 앱 실행:

```bash
streamlit run app.py
```

브라우저가 자동으로 열리거나 콘솔에 표시된 로컬 URL(예: http://localhost:8501)을 방문하면 앱을 확인할 수 있습니다.

## 파일 설명

- `app.py` — Streamlit 애플리케이션 진입점
- `requirements.txt` — 필요한 Python 패키지 목록

## 개발 및 기여

작은 변경이나 기능 추가는 환영합니다. 기여 방법:

1. Fork
2. 브랜치 생성: `git checkout -b feature/my-feature`
3. 변경사항 커밋 후 PR 요청

## 라이선스

특별히 지정하지 않았다면 기본적으로 개인/학습용 리포지토리입니다.

## 연락처

프로젝트 관련 문의는 레포 소유자에게 이슈 또는 이메일로 연락하세요.
