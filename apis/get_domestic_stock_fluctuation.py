from fastapi import APIRouter

from examples_llm.domestic_stock.fluctuation.fluctuation import fluctuation
from common.helpers import build_kis_response

router = APIRouter()

@router.get("/domestic-stock/v1/ranking/fluctuation")
def get_domestic_stock_fluctuation():
    print('get_domestic_stock_fluctuation')

    # 사용 예시: 등락률 순위 조회
    df = fluctuation(
        fid_cond_mrkt_div_code="J",      # KRX
        fid_cond_scr_div_code="20170",   # 등락률
        fid_input_iscd="0000",           # 전체
        fid_rank_sort_cls_code="0",      # 등락률순
        fid_input_cnt_1="0",             # 조회 개수(0이면 API 기본값 사용, 필요 시 "50" 등으로 지정)
        fid_prc_cls_code="0",            # 가격 구분 전체
        fid_input_price_1="",            # 가격 하한(없으면 빈 문자열)
        fid_input_price_2="",            # 가격 상한(없으면 빈 문자열)
        fid_vol_cnt="",                  # 최소 거래량(없으면 빈 문자열)
        fid_trgt_cls_code="0",           # 대상 전체
        fid_trgt_exls_cls_code="0",      # 제외 대상 없음
        fid_div_cls_code="0",            # 분류 전체
        fid_rsfl_rate1="",               # 등락 비율 하한
        fid_rsfl_rate2=""                # 등락 비율 상한
        # tr_cont="",
        # dataframe=None
    )

    print(df.to_dict(orient="records"))

    # pandas DataFrame은 그대로 반환하면 직렬화 오류가 날 수 있습니다.
    # return df.to_dict(orient="records")
    return build_kis_response(result1=df.to_dict(orient="records"), items="")

