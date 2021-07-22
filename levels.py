def tps_max_green_alien(score) -> float:
    if score > 10000:
        return 0.5
    elif score > 5000:
        return 1
    elif score > 2000:
        return 1.5
    elif score > 1000:
        return 2.0
    elif score > 500:
        return 2.5
    elif score > 200:
        return 3.0
    elif score > 100:
        return 4.0
    elif score > 50:
        return 4.0
    else:
        return 5.0


def tps_max_red_alien(score) -> float:
    if score > 10000:
        return 1.5
    elif score > 5000:
        return 2.0
    elif score > 2000:
        return 2.0
    elif score > 1000:
        return 2.5
    elif score > 500:
        return 3.0
    else:
        return 0
