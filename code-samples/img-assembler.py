from PIL import Image
import Image
import image_slicer

def main():
    # slice size and no. of rows and columns will be extracted from index frame 
    slice_size = (73, 73)
    rows, cols = 2,2
    # Image slices will be extracted by reading the index and list t will be populated in a loop
    t = []
    t.append(Image.open("extracted1.png").resize((slice_size[0], slice_size[1])))
    t.append(Image.open("extracted2.png").resize((slice_size[0], slice_size[1])))
    t.append(Image.open("extracted3.png").resize((slice_size[0], slice_size[1])))
    t.append(Image.open("extracted4.png").resize((slice_size[0], slice_size[1])))
    reassemble_image(t)

def reassemble_image(t, slice_size = (73,73), rows = 2, cols = 2):
    tiles = [] # The tiles of the image to be assembled
    number = 0
    for j in range(0,rows):
        for i in range(0,cols):
            coord_x = i*slice_size[0]
            coord_y = j*slice_size[1]
            coords = (coord_x, coord_y)
            position = (i+1,j+1)
            tile = image_slicer.Tile(t[number], number, position, coords)
            tiles.append(tile)
    res = image_slicer.join(tuple(tiles))
    res.save("Final.png")


if __name__ == '__main__':
    main()
