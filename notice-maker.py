import json
import datetime
import uuid
import os

FILE_PATH = "./meta-data/notice-meta-data.json"

def make_new_notice_meta_data():
    # 파일이 없으면 빈 리스트로 초기화
    if not os.path.exists(FILE_PATH):
        data = []
    else:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    # 새로운 공지 생성
    nid = str(uuid.uuid4())
    new_notice = {
        "nid": nid,
        "title": "새로운 공지글 등록",
        "date": datetime.date.today().isoformat()
    }

    # 최신 공지가 가장 앞에 오도록 추가
    data.insert(0, new_notice)

    # 파일 다시 저장
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ 새로운 공지 추가 완료: {nid}")

if __name__ == "__main__":
    make_new_notice_meta_data()