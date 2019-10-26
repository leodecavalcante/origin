from datetime import date


def create_client_insurance_default():
    client_insurance = {
        "auto": [
            {"key": 1, "value": "regular"}
        ],
        "disability": "ineligible",
        "home": [
            {"key": 1, "value": "economic"},
            {"key": 2, "value": "regular"}
        ],
        "life": "regular",
        "umbrella": "regular"
    }
    return client_insurance


def create_client_info_default():
    client_info = {
        "age": 35,
        "dependents": 1,
        "houses": [
            {"key": 1, "ownership_status": "owned"},
            {"key": 2, "ownership_status": "mortgaged"}
        ],
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicles": [
            {"key": 1, "year": int(date.today().strftime("%Y")) - 1}
        ]
    }
    return client_info


def create_client_info_ineligible():
    client_info = {
        "age": 90,
        "dependents": 0,
        "houses": [],
        "income": 0,
        "marital_status": "single",
        "risk_questions": [0, 0, 0],
        "vehicles": []
    }
    return client_info


def create_client_info_economic():
    client_info = {
        "age": 35,
        "dependents": 0,
        "houses": [
            {"key": 1, "ownership_status": "owned"}
        ],
        "income": 1,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
        "vehicles": [
            {"key": 1, "year": 1900}
        ]
    }
    return client_info


def create_client_info_regular():
    client_info = {
        "age": 50,
        "dependents": 1,
        "houses": [
            {"key": 1, "ownership_status": "owned"}
        ],
        "income": 1,
        "marital_status": "single",
        "risk_questions": [0, 1, 0],
        "vehicles": [
            {"key": 1, "year": 1900}
        ]
    }
    return client_info


def create_client_info_responsible():
    client_info = {
        "age": 50,
        "dependents": 1,
        "houses": [
            {"key": 1, "ownership_status": "mortgaged"}
        ],
        "income": 1,
        "marital_status": "married",
        "risk_questions": [1, 1, 1],
        "vehicles": [
            {"key": 1, "year": int(date.today().strftime("%Y"))}
        ]
    }
    return client_info


def create_client_insurance_ineligible():
    client_insurance = {
        "auto": "ineligible",
        "disability": "ineligible",
        "home": "ineligible",
        "life": "ineligible",
        "umbrella": "ineligible"
    }
    return client_insurance
