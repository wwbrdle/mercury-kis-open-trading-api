from fastapi import APIRouter
from datetime import datetime
import psutil
import os

router = APIRouter()

@router.get("/heartbeat")
async def get_heartbeat():
    """
    서버 상태를 확인하는 heartbeat 엔드포인트
    """
    try:
        # 시스템 정보 수집
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        # 현재 시간
        current_time = datetime.now()
        
        # 환경 정보
        environment = os.getenv("ENV", "unknown")
        
        return {
            "status": "healthy",
            "timestamp": current_time.isoformat(),
            "server_info": {
                "environment": environment,
                "cpu_usage_percent": cpu_percent,
                "memory": {
                    "total_gb": round(memory.total / (1024**3), 2),
                    "available_gb": round(memory.available / (1024**3), 2),
                    "used_percent": memory.percent
                },
                "disk": {
                    "total_gb": round(disk.total / (1024**3), 2),
                    "free_gb": round(disk.free / (1024**3), 2),
                    "used_percent": round((disk.used / disk.total) * 100, 2)
                }
            },
            "message": "Server is running normally"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "timestamp": datetime.now().isoformat(),
            "error": str(e),
            "message": "Failed to get server status"
        }

@router.get("/health")
async def health_check():
    """
    간단한 헬스체크 엔드포인트
    """
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "service": "mercury-kis-open-trading-api"
    }
