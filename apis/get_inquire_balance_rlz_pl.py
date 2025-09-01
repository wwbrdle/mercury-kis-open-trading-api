from fastapi import APIRouter

from examples_llm.domestic_stock.inquire_balance_rlz_pl.inquire_balance_rlz_pl import inquire_balance_rlz_pl
from common.helpers import build_kis_response

from examples_llm import kis_auth as ka

router = APIRouter()

# 인증
ka.auth()
trenv = ka.getTREnv()

@router.get("/domestic-stock/v1/trading/inquire-balance-rlz-pl")
def get_domestic_stock_inquire_balance_rlz_pl():
    print('get_domestic_stock_inquire_balance_rlz_pl')

    ##############################################################################################
    # [국내주식] 주문/계좌 > 주식잔고조회_실현손익[v1_국내주식-041]
    ##############################################################################################

    result1, result2 = inquire_balance_rlz_pl(
        cano=trenv.my_acct,
        acnt_prdt_cd=trenv.my_prod,
        afhr_flpr_yn="N",
        inqr_dvsn="02",
        unpr_dvsn="01",
        fund_sttl_icld_yn="N",
        fncg_amt_auto_rdpt_yn="N",
        prcs_dvsn="01",
        cost_icld_yn="N"
    )
    print('result1', result1)
    print('result2', result2.to_dict(orient="records"))

    return build_kis_response(result1=result1.to_dict(orient="records"), items=result2.to_dict(orient="records"), msg="get_domestic_stock_inquire_balance_rlz_pl")