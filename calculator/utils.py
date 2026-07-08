# Riktig KPI-data från SCB (1980 = 100)
# Källa: https://www.scb.se/hitta-statistik/statistik-efter-amne/priser-och-konsumtion/konsumentprisindex/konsumentprisindex-kpi/
KPI_DATA = {
    1980: 100.0,
    1981: 112.1,
    1982: 121.7,
    1983: 132.6,
    1984: 143.2,
    1985: 153.8,
    1986: 160.3,
    1987: 167.0,
    1988: 176.8,
    1989: 188.1,
    1990: 207.6,
    1991: 227.2,
    1992: 232.3,
    1993: 243.1,
    1994: 248.2,
    1995: 255.3,
    1996: 256.2,
    1997: 259.6,
    1998: 261.3,
    1999: 262.5,
    2000: 265.9,
    2001: 272.1,
    2002: 277.8,
    2003: 282.5,
    2004: 283.6,
    2005: 284.2,
    2006: 288.0,
    2007: 294.1,
    2008: 304.0,
    2009: 303.3,
    2010: 306.0,
    2011: 314.8,
    2012: 318.3,
    2013: 318.5,
    2014: 318.6,
    2015: 316.4,
    2016: 319.3,
    2017: 324.1,
    2018: 331.3,
    2019: 336.4,
    2020: 339.8,
    2021: 347.1,
    2022: 376.3,
    2023: 405.2,
    2024: 418.8,
    2025: 425.0,  # Uppskattat baserat på trend
    2026: 431.0,  # Uppskattat baserat på trend
}


def calculate_inflation_price(original_price, from_year, to_year=2026):
    """
    Räkna ut vad en pryl skulle kosta idag baserat på SCB:s KPI.
    Använder riktig historisk data + uppskattning för framtida år.
    """
    if from_year in KPI_DATA and to_year in KPI_DATA:
        from_kpi = KPI_DATA[from_year]
        to_kpi = KPI_DATA[to_year]
        factor = to_kpi / from_kpi
        current_value = float(original_price) * factor
        return round(current_value, 2)
    else:
        # Fallback till 2% snittinflation om årtal saknas
        years = to_year - from_year
        current_value = float(original_price) * ((1.02) ** years)
        return round(current_value, 2)


def calculate_custom_inflation(price, year):
    """Räkna ut inflation för valfritt pris och årtal"""
    try:
        price = float(price)
        year = int(year)
        return calculate_inflation_price(price, year)
    except (ValueError, TypeError):
        return None


def get_inflation_factor(from_year, to_year=2026):
    """Returnerar inflationsfaktorn mellan två år"""
    if from_year in KPI_DATA and to_year in KPI_DATA:
        return round(KPI_DATA[to_year] / KPI_DATA[from_year], 2)
    return None


def get_fun_comparisons(price):
    """Returnerar roliga jämförelser för dagens värde"""
    comparisons = []

    if price >= 60:
        pizzor = round(price / 85)
        comparisons.append(f"🍕 {pizzor} pizzor")

    if price >= 15:
        biobiljetter = round(price / 150)
        comparisons.append(f"🎬 {biobiljetter} biobiljetter")

    if price >= 5:
        glassar = round(price / 25)
        comparisons.append(f"🍦 {glassar} mjukglassar")

    if price >= 20:
        liter_bensin = round(price / 20)
        comparisons.append(f"⛽ {liter_bensin} liter bensin")

    return comparisons