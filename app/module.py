from datetime import date

MAX_AGE = 60
MIN_AGE = 30
AVG_AGE = 40
MIN_INCOME = 200000


def calculate_insurance(client_info):
    risk_score = __calculate_common_lines_points(client_info)

    client_insurance = {"auto": calculate_auto(client_info, risk_score),
                        "disability": calculate_disability(client_info, risk_score),
                        "home": calculate_home(client_info, risk_score),
                        "life": calculate_life(client_info, risk_score)}
    client_insurance["umbrella"] = calculate_umbrella(client_insurance)

    return client_insurance


def __calculate_common_lines_points(client_info):
    risk_score = sum(client_info["risk_questions"])
    if client_info["age"] < MIN_AGE:
        risk_score -= 2
    elif client_info["age"] <= AVG_AGE:
        risk_score -= 1

    if client_info["age"] > MIN_INCOME:
        risk_score -= 1

    return risk_score


def calculate_auto(client_info, risk_score):
    if not client_info["vehicles"]:
        return "ineligible"

    five_year_ago = int(date.today().strftime("%Y")) - 5
    autos = []
    for index in range(len(client_info["vehicles"])):
        auto = {}
        auto["key"] = client_info["vehicles"][index]["key"]

        auto_risk_score = risk_score
        if client_info["vehicles"][index]["year"] >= five_year_ago:
            auto_risk_score += 1

        auto_risk_score += __calculate_point_only_one(client_info["vehicles"])

        auto["value"] = __determine_insurance_plan(auto_risk_score)
        autos.append(auto)

    return autos


def calculate_disability(client_info, risk_score):
    if client_info["income"] == 0 or client_info["age"] > MAX_AGE:
        return "ineligible"

    for index in range(len(client_info["houses"])):
        if client_info["houses"][index]["ownership_status"] == "mortgaged":
            risk_score += 1
            break

    risk_score += __calculate_dependents_point(client_info)

    if client_info["marital_status"] == "married":
        risk_score -= 1

    return __determine_insurance_plan(risk_score)


def calculate_home(client_info, risk_score):
    if not client_info["houses"]:
        return "ineligible"

    homes = []
    for index in range(len(client_info["houses"])):
        home = {}
        home["key"] = client_info["houses"][index]["key"]

        home_risk_score = risk_score
        if client_info["houses"][index]["ownership_status"] == "mortgaged":
            home_risk_score += 1

        home_risk_score += __calculate_point_only_one(client_info["houses"])

        home["value"] = __determine_insurance_plan(home_risk_score)
        homes.append(home)

    return homes


def calculate_life(client_info, risk_score):
    if client_info["age"] > MAX_AGE:
        return "ineligible"

    risk_score += __calculate_dependents_point(client_info)
    if client_info["marital_status"] == "married":
        risk_score += 1
    return __determine_insurance_plan(risk_score)


def calculate_umbrella(client_insurance):
    return "regular" if __is_eligible_to_umbrella(client_insurance) else "ineligible"


def __calculate_point_only_one(list):
    return 1 if len(list) == 1 else 0


def __determine_insurance_plan(risk_score):
    if risk_score <= 0:
        return "economic"
    elif risk_score <= 2:
        return "regular"
    elif risk_score >= 3:
        return "responsible"


def __calculate_dependents_point(client_info):
    return 1 if client_info["dependents"] > 0 else 0


def __is_eligible_to_umbrella(client_insurance):
    return __is_there_economic(client_insurance["auto"]) or \
           client_insurance["disability"] == str("economic") or \
           __is_there_economic(client_insurance["home"]) or \
           client_insurance["life"] == str("economic")


def __is_there_economic(dict_list):
    if dict_list == "ineligible":
        return False

    for index in range(len(dict_list)):
        if dict_list[index]["value"] == str("economic"):
            return True

    return False
