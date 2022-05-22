import sys
import pyperclip

# https://en.wikipedia.org/wiki/Box-drawing_character
SYMBOL_HEAD: str = "─"
SYMBOL_BUTT: str = "─"

# Comment section needs to start with /*
PRE_HEAD: str = "/*┌"
PRE_BODY: str = "▏*│"
PRE_BUTT: str = "\*└"

# "\\" is one symbol: escaped \
POST_HEAD: str = "┐*\\"
POST_BODY: str = "│*▕"
POST_BUTT: str = "┘*/"
# Comment section needs to end with */

# Total width (including tabulation) for headers
WIDTH: int = 80

# Amount of spaces used for tabulation
TAB: int = 4
# Set this to False, if you use TAB symbol for tabulating. I won't judge you.
TAB_SPACE: bool = True

# Set this to True, if you want the head line to be tabbed.
HEAD_TAB: bool = False
# Set this to True, if you want the rest of the lines to be tabbed.
REST_TAB: bool = True
# Set this to True, if you want the line following the headers to be tabbed.
ADD_EXTRA_TAB: bool = True


if __name__ == "__main__":
    # Extract args, skip the first one: it is "headers.py"
    args = sys.argv[1:]

    # Check that all decorators have the same width
    assert len(PRE_HEAD) == len(PRE_BODY) == len(PRE_BUTT)
    assert len(POST_HEAD) == len(POST_BODY) == len(POST_BUTT)

    # Check head/butt decorator
    assert len(SYMBOL_HEAD) == len(SYMBOL_BUTT) == 1

    # Text width is total width, minus tab, minus decorators
    width: int = WIDTH - TAB - len(PRE_BODY) - len(POST_BODY)

    # Concatenate all args, using space as deliminator
    # len(args) == 0 will lead to drawing a pretty, yet empty, box
    title: str = (" ".join(args)).upper()

    tab: str = " " * TAB if TAB_SPACE else "\t"
    # Tabulation used for the head line
    tab_h: str = tab if HEAD_TAB else ""
    # Tabulation used for the rest of the lines
    tab_r: str = tab if REST_TAB else ""
    
    # Construct decorators
    head: str = SYMBOL_HEAD * width
    butt: str = SYMBOL_BUTT * width

    # Body is title string, centered
    body: str = f"{title:^{width}}"

    # The merge
    headers: str = \
        f"{tab_h}{PRE_HEAD}{head}{POST_HEAD}\n"\
        f"{tab_r}{PRE_BODY}{body}{POST_BODY}\n"\
        f"{tab_r}{PRE_BUTT}{butt}{POST_BUTT}\n"\
        f"{tab_r if ADD_EXTRA_TAB else ''}"

    # Add extra tab, if first line is not tabbed, for prettier console look.
    print((tab if REST_TAB and not HEAD_TAB else "") + headers)
    pyperclip.copy(headers)
