import numpy as np
import sys
import cv2 as cv


def show_wait_destroy(winname, img):
    cv.imshow(winname, img)
    cv.moveWindow(winname, 0,0)
    cv.resizeWindow(winname, 600,600 )
    cv.waitKey(0)
    cv.destroyWindow(winname)


def main():

    # Load the image
    path = input("Input path of image: ")
    src = cv.imread(path, cv.IMREAD_COLOR)

    # Show source image
    # cv.imshow("src", src)
    # [load_image]

    # [gray]
    # Transform source image to gray if it is not already
    if len(src.shape) != 2:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    else:
        gray = src

    # Show gray image
    # cv.imshow("gray", gray)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # show_wait_destroy("gray", gray)
    # [gray]

    # [bin]
    # Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)
    # Show binary image
    # cv.imshow("binary", bw)
    # [bin]

    # [init]
    # Create the images that will use to extract the horizontal and vertical lines
    horizontal = np.copy(bw)
    vertical = np.copy(bw)
    # [init]

    # [horiz]
    # Specify size on horizontal axis
    cols = horizontal.shape[1]
    horizontal_size = cols // 30

    # Create structure element for extracting horizontal lines through morphology operations
    horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))

    # Apply morphology operations
    horizontal = cv.erode(horizontal, horizontalStructure)
    horizontal = cv.dilate(horizontal, horizontalStructure)
    b_hor = horizontal
    # Show extracted horizontal lines
    # cv.imshow("horizontal", horizontal)
    horizontal = cv.bitwise_not(horizontal)

    # [horiz]

    # [vert]
    # Specify size on vertical axis
    rows = vertical.shape[0]
    verticalsize = rows // 30

    # Create structure element for extracting vertical lines through morphology operations
    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

    # Apply morphology operations
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)

    # Show extracted vertical lines
    # show_wait_destroy("vertical", vertical)
    # cv.imshow("vertical", vertical)
    b_vert = vertical

    # [vert]

    # [smooth]
    # Inverse vertical image
    vertical = cv.bitwise_not(vertical)
    # cv.imshow("vertical_bit", vertical)

    '''
    Extract edges and smooth image according to the logic
    1. extract edges
    2. dilate(edges)
    3. src.copyTo(smooth)
    4. blur smooth img
    5. smooth.copyTo(src, edges)
    '''

    # Step 1
    edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
    # cv.imshow("edges", edges)
    edges2 = cv.adaptiveThreshold(horizontal, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
    # Step 2
    kernel = np.ones((2, 2), np.uint8)
    edges = cv.dilate(edges, kernel)
    edges2 = cv.dilate(edges2, kernel)
    # cv.imshow("dilate", edges)

    # Step 3
    smooth = np.copy(vertical)
    smooth2 = np.copy(horizontal)

    # Step 4
    smooth = cv.blur(smooth, (2, 2))
    smooth2 = cv.blur(smooth2, (2, 2))

    # Step 5
    (rows, cols) = np.where(edges != 0)
    vertical[rows, cols] = smooth[rows, cols]

    (rows2, cols2) = np.where(edges2 != 0)
    horizontal[rows2, cols2] = smooth2[rows2, cols2]
    # Show final result
    # cv.imshow("smooth - final", vertical)
    # [smooth]

    cv.imwrite('test_image_lines.jpg',vertical)
    img1 = cv.imread(path, 0)
    img2 = cv.imread('test_image_lines.jpg', 0)
    # img3 = b_vert - 50
    # img3 = img1 + vertical
    # img3 = img1 - vertical
    # img3 = vertical + img1
    img3 = bw - b_vert - edges - edges2 - b_hor
    img3 = cv.bitwise_not(img3)
    cv.imshow("minused", img3)
    # img3 = bw - b_vert - edges
    # cv.imshow("minused2", img3)
    cv.imwrite('minused.png',img3)

    cv.waitKey(0)
    cv.destroyAllWindows() 
    return 0

if __name__ == "__main__":
    main()