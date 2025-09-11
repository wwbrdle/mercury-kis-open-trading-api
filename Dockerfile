# Python 3.13 slim 이미지 사용
FROM python:3.13-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 업데이트 및 필요한 패키지 설치 (한 번에 정리)
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && rm -rf /var/tmp/*

# Python 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip cache purge \
    && rm -rf /root/.cache/pip \
    && find /usr/local/lib/python3.13 -name "*.pyc" -delete \
    && find /usr/local/lib/python3.13 -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

# 애플리케이션 코드 복사 (필요한 파일만)
COPY main.py .
COPY config.py .
COPY apis/ ./apis/
COPY common/ ./common/
COPY examples_llm/ ./examples_llm/
COPY stocks_info/ ./stocks_info/

# 환경변수 설정
ENV ENV=production
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 포트 노출
EXPOSE 8000

# 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1", "--log-level", "info"]
