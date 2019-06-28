import filters

def main():
    file_name = input("enter the name of the image file you want to edit: ")

    img = filters.load_img(file_name)

    new_img = filters.obamicon(img)

    new_img_2 = filters.greyscale(new_img)

    blue = (30, 85, 115)

    new_img_3 = filters.emphasize(img, blue, 50)

    new_img_4 = filters.add_color(img, blue)

    new_img_5 = filters.invert(new_img_4)

    #save filtered image as a new image
    filters.save_img(new_img_2, "new_im.jpg")



if __name__ == '__main__':
    main()
