# 🎊 Wanted X Wecode PreOnBoarding Backend Course | 무한루프 팀

원티드 3주차 기업 과제 : Human Scape Assignment Project
✅ 휴먼 스케이프 기업 과제입니다.

- [휴먼 스케이프 사이트](https://humanscape.io/kr/index.html)
- [휴먼 스케이프 채용공고 링크](https://www.wanted.co.kr/wd/41413)

<br>
<br>

# 🔖 목차

- Team 소개
- 과제 내용
- 기술 환경 및 tools
- 모델링 ERD
- API 명세 및 기능 설명
- 설치 및 실행 방법

<br>
<br>

# 🧑‍🤝‍🧑 Team 소개

|                      이름                      |                                    담당 기능                                    | 블로그 |
| :--------------------------------------------: | :-----------------------------------------------------------------------------: | :----: |
|                      공통                      | 초기환경 설정, DB 모델링, postman api 문서 작성, README.md 작성, 배포, UnitTest |   X    |
|       [유동헌](https://github.com/dhhyy)       |                              임상 정보 리스트 API                               |        |
|     [하예준](https://github.com/TedJunny)      |                            임상정보 수집 batch task                             |        |
| [오지윤(팀장)](https://github.com/Odreystella) |                             임상 정보 상세 조회 API                             |        |
|      [송치헌](https://github.com/Oraange)      |                            임상정보 수집 batch task                             |        |

<br>
<br>

# 📖 과제 내용

### **[ 필수 포함 사항 ]**

- README 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

### **[ 개발 요구 사항 ]**

- ORM 사용 필수
- DB SQLite 사용
- 구현 기능

  - 임상정보를 수집하는 batch task

    - 참고: [공공데이터 포털 페이지](https://www.data.go.kr/data/3074271/fileData.do#/API목록/GETuddi%3Acfc19dda-6f75-4c57-86a8-bb9c8b103887)

  - 수집한 임상정보에 대한 API

    - 특정 임상정보 읽기(키 값은 자유)

  - 수집한 임상정보 리스트 API
    - 최근 일주일내에 업데이트(변경사항이 있는) 된 임상정보 리스트
      - pagination 기능

### **[ 가산점 ]**

- Unit test의 구현
- 배포하여 웹에서 사용 할 수 있도록 제공
- 임상정보 검색 API 제공

<br>
<br>

# ➡️ Build(AWS EC2)

API URL : http://18.216.91.118:8000

<br>
<br>

# ⚒️ 기술 환경 및 tools

- Back-End: `Python 3.9.7`, `Django 3.2.9`
- Database: `Sqlite3`
- Deploy: `AWS EC2`
- ETC: `Git`, `Github`, `Postman`

<br>
<br>

# 📋 모델링 ERD

[Aquerytool URL](https://aquerytool.com/aquerymain/index/?rurl=dde567a2-e41b-431c-b323-05e75d42c47c&)  
Password : dm612s

![db](https://user-images.githubusercontent.com/77820352/141988846-fef565eb-b6cb-4e97-b71d-bf2608c56f2d.png)

<br>
<br>

# 🌲 디렉토리 구조

```
.
├── config
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── cron.py
│   ├── models.py
│   ├── openapi.py
│   ├── tests.py
│   ├── utils.py
│   └── views.py
├── clinics
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── db.sqlite3
├── my_settings.py
├── CONVENTION.md
├── PULL_REQUEST_TEMPLATE.md
├── README.md
└── requirements.txt
```

<br>
<br>

# 🔖 API 명세서

[Postman API Document 보러가기](https://documenter.getpostman.com/view/18212819/UVCB94M3)

<br>

### 👉 임상정보를 수집하는 batch task

1. `my_settings.py`에 `OPEN_API_KEY`라고 키를 정의하여, 공공 API를 호출합니다.
2. 매일 자정에 크론잡이 활성화됩니다.
3. `python manage.py crontab add` 명령어로 크론잡을 활성화합니다.
4. `python manage.py crontab show` 명령어로 크론잡의 목록을 확인합니다.
5. `python manage.py crontab remove` 명령어로 크론잡의 목록을 삭제합니다.

<br>

### 👉 임상 정보 상세 조회 API

1. `path parameter`에 해당하는 임상 정보를 출력합니다.
2. 해당하는 임상 정보가 없으면 데이터가 없다는 메시지를 반환합니다.
3. `is_active`라는 필드를 두어 `False` 이면 삭제된 데이터라고 간주하고 보여주지 않습니다.

- Method: GET

```
http://18.216.91.118:8000/clinics/C160045
```

- parameter : path_parameter

- response

```
{
  "data": {
    "name": "만성뇌혈관질환 바이오뱅크 컨소시엄 운영사업",
    "id": "C160045",
    "duration": "5년",
    "scope": "국내다기관",
    "type": "기타",
    "institution": null,
    "trial": "",
    "subjects": 765,
    "department": "Psychiatry",
    "updated_at": "2021-11-16 22:09:04"
  }
}

```

<br>

### 👉 임상 정보 목록 API

1. `query_parameter`에서 가져온 페이지에 해당하는 일주일 이내 갱신된 임상 정보의 리스트를 출력합니다.
2. 기본적으로 한 페이지에 10개의 임상정보를 출력합니다.
3. 일주일 이내 갱신된 임상 정보가 없고, `is_active`가 `False` 이면 데이터가 없다는 메시지를 반환합니다.
4. `is_active`라는 필드를 두어 `False` 이면 삭제된 데이터라고 간주하고 보여주지 않습니다.

- Method: GET

```
http://18.216.91.118:8000/clinics/list?page=1
```

- parameter : query_parameter

- response

```
{
  "result": {
    "data": [
      {
        "name": "조직구증식증 임상연구 네트워크 구축 및 운영(HLH)",
        "id": "C130010",
        "duration": "3년",
        "scope": "국내다기관",
        "type": "관찰연구",
        "institution": null,
        "trial": "코호트",
        "subjects": 120,
        "department": "Pediatrics",
        "updated_at": "2021-11-16 22:09:03"
      },
      {
        "name": "대한민국 쇼그렌 증후군 코호트 구축",
        "id": "C130011",
        "duration": "6년",
        "scope": "국내다기관",
        "type": "관찰연구",
        "institution": null,
        "trial": "코호트",
        "subjects": 500,
        "department": "Rheumatology",
        "updated_at": "2021-11-16 22:09:03"
      },

      ...

      {
        "name": "지속성외래복막투석(CAPD) 및 자동복막투석(APD) 환자의 삶의 질(QOL)을 비교하기 위한, 전향적, 다기관, 관찰연구",
        "id": "C110004",
        "duration": "12개월",
        "scope": "국내다기관",
        "type": "중재잊연구",
        "institution": null,
        "trial": "Phase 4",
        "subjects": 300,
        "department": "Nephrology",
        "updated_at": "2021-11-16 22:09:03"
      },
      {
        "name": "제2형 당뇨병 임상연구네트워크 구축사업",
        "id": "C140014",
        "duration": "120개월",
        "scope": "국내다기관",
        "type": "관찰연구",
        "institution": null,
        "trial": "코호트",
        "subjects": 700,
        "department": "Endocrinology",
        "updated_at": "2021-11-16 22:09:03"
      }
    ],
    "general_information": {
      "count": 10,
      "total_count": 145,
      "page": 1,
      "total_page": 15,
      "per_page": 10
    }
  }
}

```

<br>

### 👉 유닛 테스트 결과

![테스트 결과](https://user-images.githubusercontent.com/77820352/142019330-04708472-ad63-419c-b6d1-2f1aab6eb54e.png)

- 임상 정보 상세 조회 API, 임상 정보 목록 조회 API 테스트 진행하였습니다.
- 각 API에 대한 성공 / 실패 테스트 진행하였습니다.

<br>
<br>

# 🔖 설치 및 실행 방법

### 로컬 및 테스트용

1. 해당 프로젝트를 `clone`하고, 프로젝트로 들어간다.

```shell
$ git clone https://github.com/wanted-InfinityLoop/human-scape-InfinityLoop.git .
$ cd human-scape-InfinityLoop
```

2. 가상환경으로 `miniconda`를 설치한다. [Go](https://docs.conda.io/en/latest/miniconda.html)

```shell
$ conda create -n humanscape python=3.9
$ conda actvate humanscape
```

3. 가상환경 생성 후, `requirements.txt`에 명시된 패키지를 설치한다.

```shell
$ pip install -r requirements.txt
```

```shell
# requirements.txt

bcrypt==3.2.0
Django==3.2.9
django-cors-headers==3.10.0
gunicorn==20.1.0
django-crontab==0.7.1
requests==2.26.0
```

4. migrate 후 로컬 서버 가동
   > 런서버 실행을 위해 my_settings.py에서 MY_SECRET_KEY를 정의하였습니다.

```shell
$ python manage.py migrate
$ python manage.py runserver
```
