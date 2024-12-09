from PIL import ImageColor
from PIL import ImageFont
from PIL.ImageFont import FreeTypeFont

color_primary = ImageColor.getcolor("#FF5053", "RGB")
color_highlight = ImageColor.getcolor("#FEF2FF", "RGB")
color_accent_a = ImageColor.getcolor("#B2AAFF", "RGB")
color_accent_b = ImageColor.getcolor("#6A5FDB", "RGB")
color_accent_c = ImageColor.getcolor("#29114C", "RGB")
color_accent_d = ImageColor.getcolor("#261A66", "RGB")
color_accent_e = ImageColor.getcolor("#190B2F", "RGB")
color_background = ImageColor.getcolor("#0F000A", "RGB")
# color_background = ImageColor.getcolor("#000000", "RGB")

color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)


def font_headline(size: int) -> FreeTypeFont:
    return ImageFont.truetype(
        "/Users/sschaeffner/Downloads/38c3-styleguide-assets-v2/fonts/pilowlava/Fonts/Pilowlava-Regular.otf",
        size=size
    )


def font_numbers(size: int) -> FreeTypeFont:
    return ImageFont.truetype(
        "/Users/sschaeffner/Downloads/38c3-styleguide-assets-v2/fonts/space-mono/SpaceMono-Regular.ttf",
        size=size
    )
