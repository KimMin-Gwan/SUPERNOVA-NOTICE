## 📝 공지글 등록 방법

새로운 공지글을 등록하려면 아래 순서를 따라주세요.

### 1️⃣ `body`에 해당하는 `.md` 파일을 생성합니다.
- 파일명은 자동으로 생성될 `nid` 값과 동일해야 합니다.  
- 예: `0d438d46-bb5e-4f83-8d52-7a19c6b77e11.md`  
- 위치: `/meta-data/notice/` 폴더 (또는 실제 경로에 맞게 수정)

### 2️⃣ 스크립트를 실행하여 메타데이터를 갱신합니다.
```bash
    python make_new_notice_meta_data.py
```

 + 실행 시 notice-meta-data.json에 새로운 공지 메타데이터가 자동 추가됩니다.
 + 항목 구성:
   + nid: 고유 식별자 (자동 생성)
   + title : 공지 제목
   + date: 생성 날짜 (YYYY-MM-DD 형식)

### 3️⃣ 작성한 temp.md의 이름을 생성성 된 nid.md로 수정한다.

### 4️⃣ 생성된 데이터의 title을 목적에 맞게 수정한다.

### 5️⃣ GTI PUSH 한다.

### ✅ 예시

 + notice-meta-data.json
 ```
    [
        {
            "nid": "0d438d46-bb5e-4f83-8d52-7a19c6b77e11",
            "title": "임시로 제작된 데이터 제목입니다."
            "date": "2025-10-29"
        }
    ]
```