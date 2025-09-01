from fastapi import APIRouter

from examples_llm.domestic_stock.inquire_balance.inquire_balance import inquire_balance
from common.helpers import build_kis_response

from examples_llm import kis_auth as ka

router = APIRouter()

# 인증
ka.auth()
trenv = ka.getTREnv()

@router.get("/domestic-stock/v1/trading/inquire-balance")
def get_domestic_stock_inquire_balance():
    print('get_domestic_stock_inquire_balance')

    result1, result2 = inquire_balance(
        env_dv="real",
        cano=trenv.my_acct,
        acnt_prdt_cd=trenv.my_prod,
        afhr_flpr_yn="N",
        inqr_dvsn="01",
        unpr_dvsn="01",
        fund_sttl_icld_yn="N",
        fncg_amt_auto_rdpt_yn="N",
        prcs_dvsn="00"
    )
    print('result1', result1)
    print('result2', result2.to_dict(orient="records"))

    # pandas DataFrame은 그대로 반환하면 직렬화 오류가 날 수 있습니다.
    # return result1, result2.to_dict(orient="records")
    return build_kis_response(result1=result1.to_dict(orient="records"), items=result2.to_dict(orient="records"))

