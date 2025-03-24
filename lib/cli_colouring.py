from enum import Enum

class EFFECTS(Enum):
    CLEAR = "\033[0m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    SLOW_BLINK = "\033[5m" # Does not seem to be supported
    RAPID_BLINK = "\033[6m" # Does not seem to be supported
    
    REVERSE_VIDEO = "\033[7m"
    CONCEAL = "\033[8m"
    CROSSED_OUT = "\033[9m"
    DEFAULT_FONT = "\033[10m"

    ALTERNATIVE_FONT_1 = "\033[11m" # Does not seem to be supported
    ALTERNATIVE_FONT_2 = "\033[12m" # Does not seem to be supported
    ALTERNATIVE_FONT_3 = "\033[13m" # Does not seem to be supported
    ALTERNATIVE_FONT_4 = "\033[14m" # Does not seem to be supported
    ALTERNATIVE_FONT_5 = "\033[15m" # Does not seem to be supported
    ALTERNATIVE_FONT_7 = "\033[17m" # Does not seem to be supported
    ALTERNATIVE_FONT_6 = "\033[16m" # Does not seem to be supported
    ALTERNATIVE_FONT_8 = "\033[18m" # Does not seem to be supported
    ALTERNATIVE_FONT_9 = "\033[19m" # Does not seem to be supported
    FRAKTUR = "\033[20m" # Does not seem to be supported
    
    DOUBLE_UNDERLINE = "\033[21m" # And Could be bold off
    REMOVE_BOLD = DOUBLE_UNDERLINE

    DEFAULT_COLOUR_AND_INTENSITY = "\033[22m"
    REMOVE_ITALIC_AND_FRAKTUR = "\033[23m"
    REMOVE_UNDERLINE = "\033[24m"
    REMOVE_BLINK = "\033[25m"
    REMOVE_INVERSE = "\033[27m"
    REMOVE_CONCEAL = "\033[28m"
    REMOVE_CROSSED_OUT = "\033[29m"

    FOREGROUND_BLACK = "\033[30m"
    FOREGROUND_RED = "\033[31m"
    FOREGROUND_GREEN = "\033[32m"
    FOREGROUND_YELLOW = "\033[33m"
    FOREGROUND_BLUE = "\033[34m"
    FOREGROUND_MAGENTA = "\033[35m"
    FOREGROUND_CYAN = "\033[36m"
    FOREGROUND_WHITE = "\033[37m"

    # SET_FORGROUND_COLOUR = "\033[38m" foreground_colour_rgb / foreground_colour_n
    DEFAULT_FOREGROUND = "\033[39m"

    BACKGROUND_BLACK = "\033[40m"
    BACKGROUND_RED = "\033[41m"
    BACKGROUND_GREEN = "\033[42m"
    BACKGROUND_YELLOW = "\033[43m"
    BACKGROUND_BLUE = "\033[44m"
    BACKGROUND_MAGENTA = "\033[45m"
    BACKGROUND_CYAN = "\033[46m"
    BACKGROUND_WHITE = "\033[47m"

    # SET_BACKGROUND_COLOUR = "\033[48m" background_colour_rgb / background_colour_n
    DEFAULT_BACKGROUND = "\033[49m"

    FRAMED = "\033[51m" # Does not seem to be supported
    ENCIRCLED = "\033[52m"
    OVERLINED = "\033[53m" # Does not seem to be supported

    REMOVE_ENCIRCLED = "\033[54m"  # And Could be framed off
    REMOVE_FRAMED = REMOVE_ENCIRCLED

    REMOVE_OVERLINED = "\033[55m" # Does not seem to be supported

    IDEOGRAM_UNDERLINE = "\033[60m" # Does not seem to be supported
    IDEOGRAM_DOUBLE_UNDERLINE = "\033[61m" # Does not seem to be supported
    IDEOGRAM_OVERLINE = "\033[62m" # Does not seem to be supported
    IDEOGRAM_DOUBLE_OVERLINE = "\033[63m" # Does not seem to be supported
    IDEOGRAM_STRESS_MARKING = "\033[64m" # Does not seem to be supported
    REMOVE_IDEOGRAM = "\033[65m" # Does not seem to be supported


    FOREGROUND_BRIGHT_BLACK = "\033[90m"
    FOREGROUND_BRIGHT_RED = "\033[91m"
    FOREGROUND_BRIGHT_GREEN = "\033[92m"
    FOREGROUND_BRIGHT_YELLOW = "\033[93m"
    FOREGROUND_BRIGHT_BLUE = "\033[94m"
    FOREGROUND_BRIGHT_MAGENTA = "\033[95m"
    FOREGROUND_BRIGHT_CYAN = "\033[96m"
    FOREGROUND_BRIGHT_WHITE = "\033[97m"

    BACKGROUND_BRIGHT_BLACK = "\033[100m"
    BACKGROUND_BRIGHT_RED = "\033[101m"
    BACKGROUND_BRIGHT_GREEN = "\033[102m"
    BACKGROUND_BRIGHT_YELLOW = "\033[103m"
    BACKGROUND_BRIGHT_BLUE = "\033[104m"
    BACKGROUND_BRIGHT_MAGENTA = "\033[105m"
    BACKGROUND_BRIGHT_CYAN = "\033[106m"
    BACKGROUND_BRIGHT_WHITE = "\033[107m"

def background_colour_rgb(r: int, g: int, b: int) -> str:
    return f"\033[48;2;{r};{g};{b}m"

def background_colour_n(n: int) -> str:
    return f"\033[48;5;{n}m"

def foreground_colour_rgb(r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m"

def foreground_colour_n(n: int) -> str:
    return f"\033[38;5;{n}m"

def test():
    for i in range(0, 256):
        print(f"{i}:\033[{i}mHello There{EFFECTS.CLEAR.value}")
        if i in [38, 48]:
            for j in range(0, 256):
                print(f"{i}-{j}:\033[{i};5;{j}mHello There{EFFECTS.CLEAR.value}")