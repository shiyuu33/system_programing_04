import math

def calc_midpoint(start_location: dict[str, float], end_location: dict[str, float]) -> dict[str, float]:

    lat1_rad = math.radians(start_location["lat"])
    lng1_rad = math.radians(start_location["lng"])
    lat2_rad = math.radians(end_location["lat"])
    lng2_rad = math.radians(end_location["lng"])
    
    X1 = math.cos(lat1_rad) * math.cos(lng1_rad)
    Y1 = math.cos(lat1_rad) * math.sin(lng1_rad)
    Z1 = math.sin(lat1_rad)
    
    X2 = math.cos(lat2_rad) * math.cos(lng2_rad)
    Y2 = math.cos(lat2_rad) * math.sin(lng2_rad)
    Z2 = math.sin(lat2_rad)
    
    Xm = (X1 + X2) / 2
    Ym = (Y1 + Y2) / 2
    Zm = (Z1 + Z2) / 2
    
    lat_mid = math.degrees(math.atan2(Zm, math.sqrt(Xm**2 + Ym**2)))
    lng_mid = math.degrees(math.atan2(Ym, Xm))
    
    return {"lat": lat_mid, "lng": lng_mid}