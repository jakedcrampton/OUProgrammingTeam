# Solution for the - https://open.kattis.com/problems/imagedecoding
__author__ = "Taras Basiuk"

first = True # First image tracker
while True:
    n = int(input().strip())
    if n == 0:
        break

    if first:
        first = False
    else:
        print() # if the image not the first, print the blank line between the images

    image_template = "{}" * n # Image template consists of n line
    image_lines = []
    pixel_length = None

    for i in range(n):
        line = input().strip().split() # Read in the next out of n lines

        lead_pixel = line[0]
        pixel_lengths = list(map(int, line[1:]))

        # Line template consists of pixel fragments
        image_line_template = ("{}" * len(pixel_lengths))
        # Unless the line is the last add a newline character to it
        if i != n - 1:
            image_line_template += "\n"

        if not pixel_length:
            # Set the expected pixel length of the line
            pixel_length = sum(pixel_lengths)
        elif pixel_length != sum(pixel_lengths):
            # If the line is of unexpected length update the image template
            image_template = ("{}" * n) + "\nError decoding image"

        pixel_fragments = []
        for i in range(len(pixel_lengths)):
            # Pixel fragment is a number of same kind of pixels
            pixel_fragments.append(lead_pixel * pixel_lengths[i])
            lead_pixel = "#" if lead_pixel == "." else "." # Flip the pixel

        # Format the image line and add it to the image
        image_lines.append(image_line_template.format(*pixel_fragments))

    # Format the image and print it out
    print(image_template.format(*image_lines))
