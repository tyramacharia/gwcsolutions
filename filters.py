from PIL import Image
import math

def load_img(file_name):
    im = Image.open(file_name)
    return im

def show_img(im):
    im.show()

def save_img(im, file_name):
    im.save(file_name, "jpeg")
    show_img(im)

def obamicon(im):
    pixels = im.getdata()
    new_pixels = []

    dark_blue = (0, 51, 76)

    red = (217, 26, 33)

    light_blue = (112, 150, 158)

    yellow = (252, 227, 116)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]
        if intensity < 182:
            new_pixels.append(dark_blue)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(light_blue)
        elif intensity >= 546:
            new_pixels.append(yellow)

    new_im = Image.new("RGB", im.size)
    new_im.putdata(new_pixels)
    return new_im

def greyscale(im):
    pixels = im.getdata()
    new_pixels = []
    for p in pixels:
        new_p = avg_pixel(p)
        new_pixels.append(new_p)
    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

def emphasize(im, rgb_color, threshold):
    pixels = im.getdata()
    new_pixels = []
    r_target = rgb_color[0]
    g_target = rgb_color[1]
    b_target = rgb_color[2]

    for p in pixels:
        r = p[0]
        g = p[1]
        b = p[2]

        color_dist = math.sqrt((r_target-r)**2 + (g_target-g)**2 + (b_target-b)**2)
        if color_dist > threshold:
            new_p = avg_pixel(p)
            new_pixels.append(new_p)
        else:
            new_pixels.append(p)
        new_im = Image.new("RGB", im.size)
        new_im = im.putdata(new_pixels)
        return new_im

def add_color(im, color):
    pixels = im.getdata()
    new_pixels = []

    for p in pixels:
        new_r = p[0]+color[0]
        new_g = p[1]+color[1]
        new_b = p[2]+color[2]
        new_pixels.append((new_r, new_g, new_b))

    new_im = Image.new("RGB", im.size)
    new_im.putdata(new_pixels)
    return new_im

def invert(im):
    pixels = im.getdata()
    new_pixels = []

    for p in pixels:
        new_r = 255-p[0]
        new_g = 255-p[1]
        new_b = 255-p[2]
        new_pixels.append((new_r, new_g, new_b))

    new_im = Image.new("RGB", im.size)
    new_im.putdata(new_pixels)
    return new_im

def avg_pixel(pixel):
    avg = (pixel[0] + pixel[1] + pixel[2]) // 3
    return (avg, avg, avg)

def aashi_filter(img):
    pixels = img.getdata()
    new_pixels = []

    dark_blue =(90, 75, 102)
    red = (120, 40, 88)
    light_blue = (102, 39, 90)
    yellow = (152, 127, 97)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]
        if intensity < 182:
            new_pixels.append(dark_blue)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(light_blue)
        elif intensity >= 546:
            new_pixels.append(yellow)
    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    return new_img

def eden_filter(img):
    pixels = img.getdata()
    new_pixels = []

    dark_blue = (255, 255, 255)
    red = (105, 255, 255)
    light_blue = (105, 42, 178)
    yellow = (230, 172, 101)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]
        if intensity < 182:
            new_pixels.append(dark_blue)
        elif intensity>= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >=364 and intensity < 546:
            new_pixels.append(light_blue)
        elif intensity >= 546:
            new_pixels.append(yellow)
    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    return new_img

def lizbeth_filter(img):
    pixels = img.getdata()
    new_pixels = []
    dark_blue = (218, 104, 158)
    red = (189, 96, 200)
    light_blue = (45, 145, 255)
    yellow = (229, 253, 172)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]
        if intensity < 182:
            new_pixels.append(red)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(dark_blue)
        elif intensity >= 364 and intensity <564:
            new_pixels.append(light_blue)
        elif intensity >= 546:
            new_pixels.append(yellow)
    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    return new_img
#     print("aww its me")
def maya_filter(img):
    pixels = img.getdata()
    new_pixels = []

    dark_blue = (187, 78, 198)
    red = (167, 10, 181)
    light_blue = (114, 18, 141)
    yellow = (140, 42, 198)

    for p in pixels:
        intensity  = p[0] + p[1] + p[2]
        if intensity < 192:
            new_pixels.append(dark_blue)
        elif intensity >= 170 and intensity < 42:
            new_pixels.append(red)
        elif intensity >= 10 and intensity < 95:
            new_pixels.append(light_blue)
        elif intensity >= 24:
            new_pixels.append(yellow)

    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    return new_img

def natalie_filter(img):
    pixels = img.getdata()
    new_pixels = []

    light_purple = (170, 164, 225)
    pink = (255, 164, 130)
    light_blue = (77, 156, 225)
    yellow = (155, 211, 130)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]
        if intensity < 182:
            new_pixels.append(light_purple)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(pink)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(light_blue)
        elif intensity >= 546:
            new_pixels.append(yellow)

    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    return new_img

def pearl_filter(img):
    pixels = img.getdata()
    new_pixels = []

    dark_blue = (148, 0, 142)
    red = (187, 170, 255)
    light_blue = (112, 150, 158)
    yellow = (255, 219, 255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]
        if intensity < 182:
            new_pixels.append(dark_blue)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(light_blue)
        elif intensity >=546:
            new_pixels.append(yellow)

    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    return new_img

def makyra_filter(image):
    pixels = image.getdata()
    new_pixels = []

    somepp = (121, 0, 113)
    for p in pixels:
        pixels_r = p[0] + somepp[0]
        pixels_g = p[1] + somepp[1]
        pixels_b = p[2] + somepp[2]

        new_pixels.append((pixels_r, pixels_g, pixels_b))

    new_img = Image.new("RGB", image.size)
    new_img.putdata(new_pixels)
    return new_img
