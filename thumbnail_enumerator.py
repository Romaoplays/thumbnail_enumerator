from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFont

import copy


def put_number_in(number, color, font_size, thumbnail):
    draw = ImageDraw.Draw(thumbnail)
    draw.text(
        (thumbnail_width - number_width, number_height),
        number,
        fill=color,
        font=ImageFont.truetype("arial.ttf", font_size),
    )


while True:
    print(
        "\nWhat's the thumbnail file name? [File must be in the same folder as python script]"
    )
    name_answer = input()
    try:
        current_thumbnail = Image.open(name_answer)
        break
    except:
        print(
            "\nFile Not Found, please check spelling, lower/uppercase and if you've included the file extension"
        )
while True:
    print("\nWhat's the font size? ")
    font_size = input()
    try:
        font_size = int(font_size)
        break
    except:
        print("\nPlease type in a number")
while True:
    print("\nWhat color would you like?\nOptions: 'gray', 'red', 'white','black'")
    font_color = input()
    if font_color == "gray":
        break
    elif font_color == "red":
        break
    elif font_color == "white":
        break
    elif font_color == "black":
        break
    else:
        print("\nPlease insert a valid color")
while True:
    print(
        "\nHow many images would you like? [They will be saved in the same folder as the current image]"
    )
    number_of_images = input()
    try:
        number_of_images = int(number_of_images)
        break
    except:
        print("\nPlease type in a number")


thumbnail_width, thumbnail_height = current_thumbnail.size

number_width = thumbnail_width * 0.15
number_height = thumbnail_height * 0.05


for i in range(number_of_images):
    iterating_thumbnail = copy.deepcopy(current_thumbnail)
    put_number_in(str(i + 1), font_color, font_size, iterating_thumbnail)
    iterating_thumbnail.save(name_answer[:-4] + str(i + 1) + ".jpg")
