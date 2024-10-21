from fuzzy import model, fuzzy_operators, inference_mamdani

# (min, max)
EXPERIENCE = (0, 10)
DIPLOMA_SCORE = (60, 100)
PROF_TEST = (0, 100)
ENG_TEST = (0, 10)

VALUES = (EXPERIENCE, DIPLOMA_SCORE, PROF_TEST, ENG_TEST)

RESULT = (0, 10)

inference_mamdani.preprocessing(model.input_lvs, model.output_lv)


def _normalization(x, min_, max_) -> float:
    return round((x - min_) / (max_ - min_), 2)


def _denormalization(y, min_, max_) -> float:
    return round(y * (max_ - min_) + min_, 2)


def main_proces(exp: int, diploma_score: int, test: int, eng_test: int) -> tuple:
    input_data = (exp, diploma_score, test, eng_test)

    normal = [_normalization(v, VALUES[i][0], VALUES[i][1]) for i, v in enumerate(input_data)]
    result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, normal)

    return _denormalization(result[0], *RESULT), result[1]


if __name__ == "__main__":
    # just for test
    num, term = main_proces(10, 100, 100, 10)

    for lv in model.input_lvs:
        fuzzy_operators.draw_lv(lv)
    fuzzy_operators.draw_lv(model.output_lv)

    print(num, term)
