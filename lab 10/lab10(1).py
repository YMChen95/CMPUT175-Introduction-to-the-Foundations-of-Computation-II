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
    img = image.Image(input_img)
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width,height)
    
    for col in range(width):
        for row in range(height):
            i = width-col-1
            px = img.getPixel(i,row)
            newimg.setPixel(col,row,px)
                        
                
    newimg.saveTk(output_img)                
            
                         
def flip_vertical(input_img, output_img):
    #TODO
    img = image.Image(input_img)
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width,height)
    
    for col in range(width):
        for row in range(height):
            i = height - row-1
            px = img.getPixel(col,i)
            newimg.setPixel(col,row,px)
            
    
    newimg.saveTk(output_img)    


def enlarge(input_img, output_img):
    #TODO
    img = image.Image(input_img)
    width = img.getWidth()*4
    height = img.getHeight()*4
    newimg = image.EmptyImage(width,height)

    for col in range(width):
        for row in range(height):
            new_col = col//4
            new_row = row//4
            px = img.getPixel(new_col,new_row)
            newimg.setPixel(col,row,px)
            

    newimg.saveTk(output_img)
flip_vertical("beepbeep.gif","flip_vertical.gif")
enlarge("beepbeep.gif","enlarge.gif")
flip_horizontal("beepbeep.gif","flip_horizontal.gif")
duplicate("beepbeep.gif","duplicate.gif")