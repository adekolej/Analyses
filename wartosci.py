
def duza_liczba(num):
    if num >= 1_000_000:
        return f"{num // 1_000_000} mln"
    elif num >= 1_000:
        return f"{num // 1_000} tys."
    else:
        return str(num)