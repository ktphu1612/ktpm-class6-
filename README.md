# Tuần 04 — Smoke test đầu tiên

## Nội dung
- `test_smoke.py` — mở trang chủ [The Internet](https://the-internet.herokuapp.com/) và kiểm tra tiêu đề trang đúng là "The Internet".
- `evidence/smoke-test-pass.png` — ảnh minh chứng test chạy pass.

## Yêu cầu
- Python 3.x
- Google Chrome (Selenium 4 tự tải driver, không cần cài chromedriver thủ công)

## Cách chạy

Chạy từ thư mục gốc của repo:

```powershell
# 1. Tạo môi trường ảo (chỉ làm lần đầu)
python -m venv .venv

# 2. Cài thư viện cần thiết
.venv\Scripts\pip install -r requirements.txt

# 3. Chạy test
.venv\Scripts\python -m pytest week-04 -v
```

Kết quả mong đợi: `1 passed`
