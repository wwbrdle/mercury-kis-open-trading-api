from fastapi import FastAPI
from contextlib import asynccontextmanager
from apis.get_domestic_stock_fluctuation import router as fluctuation_router
from apis.inquire_balance import router as inquire_balance
from apis.get_inquire_balance_rlz_pl import router as inquire_balance_rlz_pl
from apis.get_heartbeat import router as heartbeat_router
from config import get_kis_keys

def load_config():
    return get_kis_keys()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("--- Application Startup ---")
    load_config()
    try:
        yield
    finally:
        print("--- Application Shutdown ---")

app = FastAPI(lifespan=lifespan)

# 라우터를 앱에 바로 등록
app.include_router(fluctuation_router, prefix="/uapi", tags=["domestic-stock"])
app.include_router(inquire_balance, prefix="/uapi", tags=["domestic-stock"])
app.include_router(inquire_balance_rlz_pl, prefix="/uapi", tags=["domestic-stock"])
app.include_router(heartbeat_router, tags=["system"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)