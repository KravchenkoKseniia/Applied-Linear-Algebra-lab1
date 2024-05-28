import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def plot_image(image):
    plt.imshow(image)
    plt.grid(True)
    plt.gca().set_xlim([0, 500])
    plt.gca().set_ylim([500, 0])
    plt.show()


def rotate_image(image, angle, rows, cols):
    m = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), angle, 1)
    dst = cv.warpAffine(image, m, (cols, rows))
    return dst


def scale_image(image, scale):
    new_size = (int(image.shape[1] * scale), int(image.shape[0] * scale))
    res = cv.resize(image, dsize=new_size, fx=scale, fy=scale, interpolation=cv.INTER_CUBIC)
    return res


def reflect_image(image, axis):
    if axis == "x":
        return cv.flip(image, 0)
    elif axis == "y":
        return cv.flip(image, 1)
    else:
        raise ValueError("Invalid axis")


def slope_of_axis(image, slope_factor, axis, rows, cols):
    if axis == "x":
        m = np.float32([[1, slope_factor, 0], [0, 1, 0]])
    elif axis == "y":
        m = np.float32([[1, 0, 0], [slope_factor, 1, 0]])
    else:
        raise ValueError("Invalid axis")

    dst = cv.warpAffine(image, m, (cols, rows))
    return dst


def universal_transform(image, transformation_matrix, rows, cols):
    dst = cv.warpAffine(image, transformation_matrix, (cols, rows))
    return dst


def main():
    image = cv.imread("095eebf0eaad40862d700f5dbbf0d.jpg")
    rows, cols, _ = image.shape

    # Rotation

    rotated_image = rotate_image(image, 67, rows, cols)
    rotated_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)

    plot_image(rotated_image)

    # Scaling

    scaled_image = scale_image(image, 2)
    scaled_image = cv.cvtColor(scaled_image, cv.COLOR_BGR2RGB)

    plot_image(scaled_image)

    # Reflection

    reflected_image = reflect_image(image, "y")
    reflected_image = cv.cvtColor(reflected_image, cv.COLOR_BGR2RGB)

    plot_image(reflected_image)

    # Slope of axis

    slope_image = slope_of_axis(image, -0.7, "y", rows, cols)
    slope_image = cv.cvtColor(slope_image, cv.COLOR_BGR2RGB)

    plot_image(slope_image)

    # Universal transformation

    transformation_matrix = np.array([
        [-2, 0.5, 0],
        [0.5, 1, 0]
    ])

    transformed_image = universal_transform(image, transformation_matrix, rows, cols)
    transformed_image = cv.cvtColor(transformed_image, cv.COLOR_BGR2RGB)

    plot_image(transformed_image)


if __name__ == "__main__":
    main()
