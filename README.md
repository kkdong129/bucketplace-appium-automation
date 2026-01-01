# 🏠 오늘의집 안드로이드 앱 자동화 테스트 프로젝트

본 프로젝트는 '오늘의집' 안드로이드 애플리케이션의 로그인 관련 주요 시나리오를 자동화한 테스트 스크립트입니다.  
**Appium**과 **Python unittest**를 기반으로 하며, 유지보수가 용이한 **Page Object Model(POM)** 구조로 설계되었습니다.

---

## 🚀 테스트 범위 (Test Scenarios)
전체적인 시나리오 중 내부적으로 관리가 가능한 **이메일 계정 로그인 시나리오**을 중심으로 자동화하였습니다.
소셜 계정 로그인은 외부 플랫폼(애플, 카카오, 네이버)의 보안 정책이나 세션 유지 문제, UI 변경에 민감하여 이번 자동화 범위에서 제외되었습니다.

| ID | 테스트 케이스 명 | 주요 검증 포인트 |
|:---:|:---|:---|
| **TC-01** | 앱 설치 및 진입 | 앱 설치 확인 및 스플래시 이후 로그인 화면 진입 여부 |
| **TC-02** | 메인 로그인 UI | 로고, SNS 로그인 버튼, 이메일 로그인 버튼 노출 확인 |
| **TC-03~05** | 이메일 로그인 화면 이동 | 화면 진입 및 뒤로가기(아이콘/시스템 키) 동작 확인 |
| **TC-06~07** | 입력 데이터 초기화 | 이탈 후 재진입 시 입력했던 정보가 비워져 있는지 확인 |
| **TC-08~09** | 미입력 예외 처리 | 정보 미입력 시 나타나는 안내 토스트 메시지 검증 |
| **TC-10~11** | 로그인 성공 및 홈 UI | 정상 계정 로그인 후 홈 화면 진입 및 팝업 제어 |
| **TC-12** | 로그인 실패 시나리오 | 유효하지 않은 비밀번호 입력 시 오류 메시지 확인 |
| **TC-13** | **계정 잠금 시나리오** | 10회 이상 실패 시 발생하는 로그인 제한 동작 검증 |

#### 상세 테스트 케이스는 아래 문서를 참고해주세요.
- [자동화 테스트케이스(Excel)](bucketplace/automation/testcase_spreadsheet.xlsx), [메뉴얼 테스트케이스(Excel)](bucketplace/automation/manual_testcase_spreadsheet.xlsx)

---

## 🛠️ 기술 스택 (Tech Stack)

- **Language:** Python
- **Test Framework:** unittest
- **Automation Tool:** Appium (UiAutomator2 Driver)
- **Design Pattern:** Page Object Model (POM)
- **Configuration:** JSON 기반 환경 설정 관리

---

## 📂 프로젝트 구조 (Project Structure)

```text
automation
├── pages/                     # UI 요소 및 화면 단위 로케이터 정의 (Page Objects)
│   ├── base_page.py           # 공통 유틸리티 (Wait, Click, Type 등)
│   ├── login_page.py          # 로그인 화면
│   ├── email_login_page.py    # 이메일 로그인 화면
│   └── home_page.py           # 로그인 이후 홈(메인) 화면
├── tests/                     # 테스트 시나리오 (Test Cases)
│   ├── base_capability.py     # Appium 드라이버 및 Config 로드 공통 설정
│   └── test_login_flow.py     # 시나리오별 테스트 메서드
├── config.json.example        # 환경 설정 샘플 파일
├── testcase_spreadsheet.xlsx  # 테스트케이스 엑셀 파일
└── README.md                  # 프로젝트 가이드
```

## 💻 개발 및 테스트 환경 (Environment)
- **OS:** Windows 10
- **Editor:** ATOM
- **Python Version:** 3.14.2
- **Appium Version:** 3.1.2
- **Appium Python Client:** 5.2.4
- **Android Driver:** UiAutomator2
- **Test Device:** Galaxy Z Flip (Android 12)
- **Test App Version:** 25.41.0

---

## 🛠️ 설치 및 실행 방법 (Setup & Execution)

### 1. 필수 소프트웨어 설치
- **Python:** [python.org](https://www.python.org/)에서 설치 후 환경 변수 설정 확인
- **Appium Server:** Node.js 설치 후 `npm install -g appium`으로 설치
- **UiAutomator2 Driver:** `appium driver install uiautomator2` 명령어로 드라이버 설치

### 2. 라이브러리 설치
프로젝트 루트 폴더에서 아래 명령어를 실행하여 필요한 패키지를 설치합니다.
```bash
pip install Appium-Python-Client
```

### 3. 환경 설정 (config.json)
- 보안 및 기기별 설정 관리를 위해 config.json 파일을 수동으로 생성해야 합니다.
- 프로젝트 루트 폴더에 있는 config.json.example 파일을 복사합니다.
- 파일 이름을 config.json으로 변경합니다.
- 본인의 기기 UDID와 테스트용 계정 정보를 입력합니다.
- Note: config.json 파일은 계정 비밀번호 등 민감한 정보를 포함하므로 보안을 위해 .gitignore에 등록되어 있습니다. 깃허브 추적에서 제외되므로 반드시 개별적으로 수동 생성해야 테스트가 정상 작동합니다.

### 4. 테스트 실행 (Execution)
테스트를 시작하기 전, Appium 서버를 먼저 실행한 상태여야 합니다. (기본 포트: 4723)

```bash
# 프로젝트 루트 폴더에서 모든 테스트 파일을 찾아 상세히 실행
python -m unittest discover -v -s . -p "test_*.py"
```

#### 명령어 옵션 설명:
- -v (verbose): 테스트 결과(성공/실패/에러)를 상세하게 출력합니다.
- -s .: 현재 디렉토리(.)에서 테스트 탐색을 시작합니다.
- -p "test_*.py": 파일명이 test_로 시작하는 모든 파이썬 파일을 테스트 대상으로 지정합니다.

---

### ⚠️ 주의 사항 (Precautions)
- 계정 잠금 주의 (TC-13): 비밀번호 10회 오류 테스트는 실제 오늘의집 서버에 요청을 보냅니다. 테스트 직후 해당 계정의 로그인이 일정 시간 제한될 수 있으므로, 반드시 실제 사용하지 않는 테스트 전용 계정을 사용하십시오.
- Appium 서버 연결: 테스트 실행 전 반드시 Appium 서버가 127.0.0.1:4723 포트에서 정상적으로 대기 중(Listening)인지 확인하십시오.
- 기기 화면 유지: 테스트 도중 기기의 화면이 잠기면 요소를 찾지 못해 에러가 발생합니다. 안드로이드 [설정] > [개발자 옵션] > '충전 중 화면 켜짐 유지' 기능을 활성화하는 것을 권장합니다.
- 토스트 메시지 검증: 토스트 메시지는 매우 짧은 시간 동안만 노출됩니다. 사용 중인 PC나 기기의 사양(성능)에 따라 인식이 실패할 수 있으니, 에러가 발생한다면 base_page.py의 WebDriverWait 시간을 소폭 늘려 조정하십시오.
