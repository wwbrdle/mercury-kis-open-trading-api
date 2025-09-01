import os
import boto3
from dotenv import load_dotenv
from functools import lru_cache

@lru_cache(maxsize=1)
def get_kis_keys():
    if os.getenv("ENV") == "production":
        try:
            session = boto3.Session(profile_name="mercury")
            ssm = session.client("ssm", region_name="us-east-1")
            return {
                "my_app": ssm.get_parameter(Name="/kis/my_app", WithDecryption=True)["Parameter"]["Value"],
                "my_sec": ssm.get_parameter(Name="/kis/my_sec", WithDecryption=True)["Parameter"]["Value"],
                "my_htsid": ssm.get_parameter(Name="/kis/my_htsid", WithDecryption=True)["Parameter"]["Value"],
                "my_acct_stock": ssm.get_parameter(Name="/kis/my_acct_stock", WithDecryption=True)["Parameter"]["Value"],
                "my_prod": ssm.get_parameter(Name="/kis/my_prod", WithDecryption=True)["Parameter"]["Value"],
                "prod": ssm.get_parameter(Name="/kis/prod", WithDecryption=True)["Parameter"]["Value"],
                "ops": ssm.get_parameter(Name="/kis/ops", WithDecryption=True)["Parameter"]["Value"],
                "vps": ssm.get_parameter(Name="/kis/vps", WithDecryption=True)["Parameter"]["Value"],
                "vops": ssm.get_parameter(Name="/kis/vops", WithDecryption=True)["Parameter"]["Value"],
                "my_agent": ssm.get_parameter(Name="/kis/my_agent", WithDecryption=True)["Parameter"]["Value"],
            }
        except Exception as e:
            print(f"Error fetching keys from Parameter Store: {e}")
            raise
    else:
        load_dotenv()
        cfg = {
            "my_app": os.getenv("KIS_MY_APP"),
            "my_sec": os.getenv("KIS_MY_SEC"),
            "my_htsid": os.getenv("KIS_MY_HTSID"),
            "my_acct_stock": os.getenv("KIS_MY_ACCT_STOCK"),
            "my_prod": os.getenv("KIS_MY_PROD"),
            "prod": os.getenv("KIS_PROD"),
            "ops": os.getenv("KIS_OPS"),
            "vps": os.getenv("KIS_VPS"),
            "vops": os.getenv("KIS_VOPS"),
            "my_agent": os.getenv("KIS_MY_AGENT")
        }
        required_keys = ["my_app", "my_sec", "my_htsid", "my_acct_stock", "my_prod", "my_prod", "prod", "vps", "vops", "my_agent"]
        missing_keys = [key for key in required_keys if not cfg[key]]
        if missing_keys:
            raise ValueError(f"Missing required keys in .env: {', '.join(missing_keys)}")
        # if not cfg["paper_app"] or not cfg["paper_sec"]:
        #     print("Warning: KIS_PAPER_APP_KEY or KIS_PAPER_SECRET_KEY not found in .env, mo's investment may not work")
        return cfg