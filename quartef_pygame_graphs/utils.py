


def format_number(value):
    suffixes = ["", "k", "M", "B", "T"]

    index = 0
    while abs(value) >= 1000 and index < len(suffixes) - 1:
        value /= 1000
        index += 1

    if value == int(value):
        return f"{int(value)}{suffixes[index]}"
    else:
        return f"{value:.1f}{suffixes[index]}"
    
def adjust_color(hex_color, factor=0.2):
    hex_color = hex_color.lstrip('#')
    
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    if factor >= 0:
        # Darken (approach 0)
        r = max(0, int(r * (1 - factor)))
        g = max(0, int(g * (1 - factor)))
        b = max(0, int(b * (1 - factor)))
    else:
        # Lighten (approach 255) using positive target factor
        abs_factor = abs(factor)
        r = min(255, int(r + (255 - r) * abs_factor))
        g = min(255, int(g + (255 - g) * abs_factor))
        b = min(255, int(b + (255 - b) * abs_factor))
    
    return f"#{r:02X}{g:02X}{b:02X}"

def render_text(font, text, color, x, y, surface):
    text = font.render(text, True, color)
    text_surface = text.get_rect()
    text_surface.center = (x, y)
    surface.blit(text, text_surface) #the caption for the x axis numbers