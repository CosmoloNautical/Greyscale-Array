def greyscale_arr(image):
    """
    Images can be described as 3D arrays.
    This program takes a 3d array representation of an image and returns the greyscaled version of that image
    """

    def image_input():
        width, height = input(f"Enter the dimensions of the image (e.g. 3x3)\n>").strip().lower().split("x")
        width, height = int(width), int(height)
        image = [[list(map(int, input(
            f"Enter the RGB values (each separated by a space) for column {w + 1} in row {h + 1}: ").strip().split()))
                  for w in range(width)]
                 for h in range(height)]
        return image

    def print_image(image):
        for z in range(len(image)):
            print(image[y])

    def greyscale(image):
        for y in range(len(image)):
            for x in range(len(image[y])):
                for z in range(0, 3):
                    if image[y][x][z] > 255:
                        image[y][x][z] = 255
                    elif image[y][x][z] < 0:
                        image[y][x][z] = 0
                greyscaled = round((image[y][x][0] + image[y][x][1] + image[y][x][2]) / 3)
                image[y][x][0] = greyscaled
                image[y][x][1] = greyscaled
                image[y][x][2] = greyscaled
        return image

    # image_input()
    # print_image()
    return greyscale(image)
