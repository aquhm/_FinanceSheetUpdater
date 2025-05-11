from enum import Enum

class FinancialSector(Enum):
    BANK = "020000"
    SPECIALIZED_FINANCIAL = "030200"
    SAVINGS_BANK = "030300"
    INSURANCE = "050000"
    INVESTMENT = "060000"

API_FIELDS = {
    "company": {
        "base": ["dcls_month", "fin_co_no", "kor_co_nm", "dcls_chrg_man", "homp_url", "cal_tel"],
        "option": ["dcls_month", "fin_co_no", "area_cd", "area_nm", "exis_yn"]
    },
    "deposit": {
        "base": ["dcls_month", "fin_co_no", "fin_prdt_cd", "kor_co_nm", "fin_prdt_nm", "join_way", "mtrt_int", "spcl_cnd", "join_deny", "join_member", "etc_note", "max_limit", "dcls_strt_day", "dcls_end_day", "fin_co_subm_day"],
        "option": ["dcls_month", "fin_co_no", "fin_prdt_cd", "intr_rate_type", "intr_rate_type_nm", "save_trm", "intr_rate", "intr_rate2"]
    },
    "saving": {
        "base": ["dcls_month", "fin_co_no", "fin_prdt_cd", "kor_co_nm", "fin_prdt_nm", "join_way", "mtrt_int", "spcl_cnd", "join_deny", "join_member", "etc_note", "max_limit", "dcls_strt_day", "dcls_end_day", "fin_co_subm_day"],
        "option": ["dcls_month", "fin_co_no", "fin_prdt_cd", "intr_rate_type", "intr_rate_type_nm", "rsrv_type", "rsrv_type_nm", "save_trm", "intr_rate", "intr_rate2"]
    },
    "annuity": {
        "base": ["dcls_month", "fin_co_no", "fin_prdt_cd", "kor_co_nm", "fin_prdt_nm", "join_way", "pnsn_kind", "pnsn_kind_nm", "sale_strt_day", "mntn_cnt", "prdt_type", "prdt_type_nm", "avg_prft_rate", "dcls_rate", "guar_rate", "btrm_prft_rate_1", "btrm_prft_rate_2", "btrm_prft_rate_3", "etc", "sale_co", "dcls_strt_day", "dcls_end_day", "fin_co_subm_day"],
        "option": ["dcls_month", "fin_co_no", "fin_prdt_cd", "pnsn_recp_trm", "pnsn_recp_trm_nm", "pnsn_entr_age", "pnsn_entr_age_nm", "mon_paym_atm", "mon_paym_atm_nm", "paym_prd", "paym_prd_nm", "pnsn_strt_age", "pnsn_strt_age_nm", "pnsn_recp_amt"]
    },
    "mortgage": {
        "base": ["dcls_month", "fin_co_no", "fin_prdt_cd", "kor_co_nm", "fin_prdt_nm", "join_way", "loan_inci_expn", "erly_rpay_fee", "dly_rate", "loan_lmt", "dcls_strt_day", "dcls_end_day", "fin_co_subm_day"],
        "option": ["dcls_month", "fin_co_no", "fin_prdt_cd", "mrtg_type", "mrtg_type_nm", "rpay_type", "rpay_type_nm", "lend_rate_type", "lend_rate_type_nm", "lend_rate_min", "lend_rate_max", "lend_rate_avg"]
    },
    "rent": {
        "base": ["dcls_month", "fin_co_no", "fin_prdt_cd", "kor_co_nm", "fin_prdt_nm", "join_way", "loan_inci_expn", "erly_rpay_fee", "dly_rate", "loan_lmt", "dcls_strt_day", "dcls_end_day", "fin_co_subm_day"],
        "option": ["dcls_month", "fin_co_no", "fin_prdt_cd", "rpay_type", "rpay_type_nm", "lend_rate_type", "lend_rate_type_nm", "lend_rate_min", "lend_rate_max", "lend_rate_avg"]
    },
    "credit": {
        "base": ["dcls_month", "fin_co_no", "fin_prdt_cd", "crdt_prdt_type", "kor_co_nm", "fin_prdt_nm", "join_way", "cb_name", "crdt_prdt_type_nm", "dcls_strt_day", "dcls_end_day", "fin_co_subm_day"],
        "option": ["dcls_month", "fin_co_no", "fin_prdt_cd", "crdt_prdt_type", "crdt_lend_rate_type", "crdt_lend_rate_type_nm", "crdt_grad_1", "crdt_grad_4", "crdt_grad_5", "crdt_grad_6", "crdt_grad_10", "crdt_grad_11", "crdt_grad_12", "crdt_grad_13", "crdt_grad_avg"]
    },
}