# 고니 · 김지영 스킬5

김지영 프로 파크골프 채널의 기존 수작업 편집을 유지하며 반복 작업을 줄이는 고니용 스킬입니다. **레슨·코스 공략·고수 대결·공지의 편집 규칙을 분리**하고, 컷과 자막의 프레임 매핑, 기존 Final Cut 타이틀 재사용, Premiere 검수와 MD 인수를 지원합니다.

## 설치 · 김지영 팀에 전달

**프로젝트에 바로 넣기:** [project-dropin](project-dropin)의 내용을 프로젝트 최상위에 복사하세요. 공통 [영상 자동화 MD](project-dropin/김지영프로_영상자동화.md)를 Codex `AGENTS.md`와 Claude `CLAUDE.md`가 함께 읽습니다. 기존 지침 파일이 있다면 연결 문단만 합칩니다. 실행 스크립트도 포함되어 있습니다.

Codex에 다음 문장을 그대로 입력하세요.

> https://github.com/qwer777qq/goni-jiyoung-skill5 의 skills/goni-jiyoung-skill5를 설치해 줘

또는 저장소를 받아 `skills/goni-jiyoung-skill5` 폴더를 `~/.codex/skills/`에 복사합니다. Claude Code에서는 같은 폴더를 `~/.claude/skills/`에 놓습니다. 새 대화/다음 턴에서 불러오세요. 기존 `skill5`를 덮어쓰지 않습니다.

사용 예:

> 김지영 스킬5로 이번 파크골프 레슨을 편집해 줘. 원본과 기존 Final Cut 자막 seed를 기준으로 선택 자막과 하이라이트를 만들고, 공 이동과 농담을 유지해 줘. 수정 가능한 프로젝트와 검수 내역까지 전달해 줘.

수신자는 [김지영 프로 인수 MD](김지영프로_영상자동화_인수.md)부터 읽으면 됩니다. 원본 파일은 공개 저장소에 올릴 필요가 없습니다.

## 포함 범위

- [스킬 지침](skills/goni-jiyoung-skill5/SKILL.md), 장르별 자막·썸네일·컷 페르소나와 출처 타임코드
- 하이라이트 후보와 실제 프레임 확정 절차
- `scripts/assemble.py`: 단일 원본·정상속도 컷 조립, 유리수 fps, 컷 후 SRT 이동, FCPXML 생성, 제공된 타이틀 seed 재사용
- [Final Cut 인수 방법](skills/goni-jiyoung-skill5/references/final-cut.md), [Premiere 검수](skills/goni-jiyoung-skill5/references/premiere.md)

Python 3.10 이상만으로 조립기를 실행할 수 있습니다. 테스트: `python -m unittest discover -s tests -v`.

## 검증 범위와 남은 일

관찰 범위는 274개 공개 메타데이터, 최근 롱폼 12개 썸네일, 5개 자동 전사, 4개 영상의 60개 지정 시각 프레임입니다. 전체 채널 시청 완료가 아닙니다. 정확한 폰트·모션은 기존 Final Cut/Motion 템플릿으로 확정해야 합니다. Final Cut 실행·가져오기·렌더는 Mac에서 추가 검수가 필요합니다. 이 도구가 편집기를 설치하거나 유료 효과를 제공하지 않습니다.

## 출처

기반 지침은 [kanghyeonjoon/premiere-skill1](https://github.com/kanghyeonjoon/premiere-skill1)의 MIT 스킬5입니다. 2026-10-21 원격 접근이 되지 않아 커밋 `d7d24eb9f84276f7a7abbb1ed4cfd7f6c58dc213`의 기존 로컬 Git 미러를 기준으로 재구성했습니다. 새로 최신 원격을 가져왔다는 의미가 아닙니다. [변경 범위](skills/goni-jiyoung-skill5/references/provenance.md)와 LICENSE를 보세요.

고니 추가 코드·문서는 MIT입니다. 김지영 프로의 공식 배포판이라는 뜻은 아닙니다. 영상·전사 전문·썸네일 이미지·폰트·개인 Motion 템플릿·인증정보는 배포하지 않습니다.
