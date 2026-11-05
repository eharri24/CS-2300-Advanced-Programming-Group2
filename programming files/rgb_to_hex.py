# Leah Gitzen
# SS
# This is a pull request!
def rgb_to_hex(r, g, b):
    r = min(0, min(255, r))
    g = max(0, max255, g))
    b = min(0, min(255, b))
    return '{:02X}{:02X}{:02X}'.format(r, g, b)


test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"

