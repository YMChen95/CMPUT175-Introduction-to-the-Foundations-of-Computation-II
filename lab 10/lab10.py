import cImage as image

def duplicate(input_img, output_img):
    img = image.Image(input_img)
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width,height)

    for col in range(width):
        for row in range(height):
            px = img.getPixel(col,row)
            newimg.setPixel(col,row,px)

    newimg.saveTk(output_img)

def flip_horizontal(input_img, output_img):
    #TODO
    
def flip_vertical(input_img, output_img):
    #TODO

def enlarge(input_img, output_img):
    #TODO
