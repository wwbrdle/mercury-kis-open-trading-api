from datetime import datetime
from typing import Any, Dict, List, Optional, Sequence

def build_kis_response(
    result1: Any,
    items: Optional[Sequence[Any]] = None,
    *,
    status: str = "ok",
    msg: str = "한국투자증권 데이터 취득 성공",
    connection_status: str = "connected",
    response_code: int = 200,
) -> Dict[str, Any]:
    """
    공통 응답 포맷 헬퍼.

    Args:
        result1: 요약/결과 값 (data.summary에 매핑)
        items: 항목 리스트(없으면 빈 리스트)
        status: 상위 status 필드
        msg: 메시지
        connection_status: 연결 상태
        response_code: HTTP 유사 코드

    Returns:
        dict: 규격화된 응답 딕셔너리
    """
    safe_items: List[Any] = list(items) if items is not None else []
    return {
        "status": status,
        "msg": msg,
        "connection_status": connection_status,
        "response_code": response_code,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": {
            "summary": result1,
            "items": safe_items,
            "count": len(safe_items),
        },
    }