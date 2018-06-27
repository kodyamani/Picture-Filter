from PIL import Image

def load_img(filename):
    return Image.open(filename)

def show_img(any_img):
    any_img.show()

def save_img(any_img,filename):
    any_img.save(filename)

def kody(any_img):
    new_img = Image.new("RGB", any_img.size)

    mintyrose = (255,228,225)
    lightpink = (255,182,193)
    red = (217,26,33)
    palevioletred1 = (255,130,171)

    newpixels = []
    imagepixels = list(any_img.getdata())

    for individualpixel in imagepixels:
        redvalue = individualpixel[0]
        greenvalue = individualpixel[1]
        bluevalue = individualpixel[2]

        intensity = redvalue + greenvalue + bluevalue

        if intensity < 182:
            newpixels.append(palevioletred1)
        elif intensity < 364 and intensity >= 182:
            newpixels.append(red)
        elif intensity < 546 and intensity >= 364:
            newpixels.append(lightpink)
        else:
            newpixels.append(mintyrose)

    new_img.putdata(newpixels)
    return new_img
