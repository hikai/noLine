"""
Python captcha no line.

@hikai.
"""
from PIL import Image


def get_line(start, end):
    """
    Bresenham Line Algorithm.
    Produces a list of tuples from start and end.
    """

    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points


def detector(pixel, points):
    """Pixel rgb detector."""
    count = 0
    for x, y in points:
        if pixel[x, y][0] < 255:
            count += 1

    return count


img = Image.open("1.gif")
img = img.convert("RGBA")
pixdata = img.load()
mask = [1, -1]

for count in range(0, 3):
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            edge = 0

            for i in range(len(mask)):
                try:
                    edge += pixdata[x, y + i][0] * mask[i]
                except:
                    continue

            edge = abs(edge)
            knee = 200
            if edge > knee:
                pixdata[x, y] = (255, 255, 255, 255)

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y][0] < 200:
            continue

        pixdata[x, y] = (255, 255, 255, 255)

result = []
for x in range(img.size[0]):
    for y in range(img.size[1]):
        if x == 0 and y == 0:
            for i in range(0, 70):
                points = get_line((x, y), (199, i))
                result.append(detector(pixdata, points))

            for j in range(199, 0, -1):
                points = get_line((x, y), (j, 69))
                result.append(detector(pixdata, points))

        elif x == 199 and y == 0:
            for i in range(0, 70):
                points = get_line((x, y), (0, i))
                result.append(detector(pixdata, points))

            for j in range(0, 200):
                points = get_line((x, y), (j, i))
                result.append(detector(pixdata, points))

        elif x == 0 and y == 69:
            for i in range(69, 0, -1):
                points = get_line((x, y), (199, i))
                result.append(detector(pixdata, points))

            for j in range(199, 0, -1):
                points = get_line((x, y), (j, 0))
                result.append(detector(pixdata, points))

        elif x == 199 and y == 69:
            for i in range(69, 0, -1):
                points = get_line((x, y), (0, i))
                result.append(detector(pixdata, points))

            for j in range(199, 0, -1):
                points = get_line((x, y), (j, 0))
                result.append(detector(pixdata, points))

        elif 0 < x < 199 and y == 0:
            for i in range(0, 70):
                points = get_line((x, y), (0, i))
                result.append(detector(pixdata, points))

            for j in range(0, 200):
                points = get_line((x, y), (j, 69))
                result.append(detector(pixdata, points))

            for k in range(69, 0, -1):
                points = get_line((x, y), (199, k))
                result.append(detector(pixdata, points))

        elif 0 < x < 199 and y == 69:
            for i in range(69, 0, -1):
                points = get_line((x, y), (0, i))
                result.append(detector(pixdata, points))

            for j in range(0, 200):
                points = get_line((x, y), (j, 0))
                result.append(detector(pixdata, points))

            for k in range(0, 70):
                points = get_line((x, y), (199, k))
                result.append(detector(pixdata, points))

        elif x == 0 and 0 < y < 69:
            for i in range(0, 200):
                points = get_line((x, y), (i, 0))
                result.append(detector(pixdata, points))

            for j in range(0, 70):
                points = get_line((x, y), (199, j))
                result.append(detector(pixdata, points))

            for k in range(199, 0, -1):
                points = get_line((x, y), (k, 69))
                result.append(detector(pixdata, points))

        elif x == 199 and 0 < y < 69:
            for i in range(199, 0, -1):
                points = get_line((x, y), (i, 0))
                result.append(detector(pixdata, points))

            for j in range(0, 70):
                points = get_line((x, y), (0, j))
                result.append(detector(pixdata, points))

            for k in range(0, 200):
                points = get_line((x, y), (k, 69))
                result.append(detector(pixdata, points))

        else:
            for i in range(0, 200):
                points = get_line((x, y), (i, 0))
                result.append(detector(pixdata, points))

            for j in range(0, 70):
                points = get_line((x, y), (199, j))
                result.append(detector(pixdata, points))

            for k in range(199, 0, -1):
                points = get_line((x, y), (k, 69))
                result.append(detector(pixdata, points))

            for l in range(69, 0, -1):
                points = get_line((x, y), (0, l))
                result.append(detector(pixdata, points))

        print(result, end='')
    print('\n')

img.save("1_unline.gif", "GIF")
