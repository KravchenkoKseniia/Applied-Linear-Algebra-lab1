import numpy as np
import matplotlib.pyplot as plt


def plot_object(obj, title, color):
    print(f"{title} matrix:\n{obj}")
    plt.plot(obj[:, 0], obj[:, 1], color)
    plt.title(title)
    plt.axis('equal')
    plt.grid()
    plt.gca().set_xlim([-20, 20])
    plt.gca().set_ylim([-20, 20])
    plt.show()


def rotate_object(obj, angle):
    theta = np.radians(angle)

    if obj.shape[1] == 2:
        rotation = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
    elif obj.shape[1] == 3:
        rotation = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])
    else:
        raise ValueError("Invalid object shape")

    return np.dot(obj, rotation)


def scale_object(obj, scale):
    if obj.shape[1] == 2:
        scale_matrix = np.array([
            [scale, 0],
            [0, scale]
        ])
    elif obj.shape[1] == 3:
        scale_matrix = np.array([
            [scale, 0, 0],
            [0, scale, 0],
            [0, 0, 1]
        ])
    else:
        raise ValueError("Invalid object shape")

    return np.dot(obj, scale_matrix)


def reflect_object(obj, axis):

    if axis == "x":
        reflection = np.array([
            [1, 0],
            [0, -1]
        ])
    elif axis == "y":
        reflection = np.array([
            [-1, 0],
            [0, 1]
        ])
    else:
        raise ValueError("Invalid axis")

    return np.dot(obj, reflection)


def slope_of_axis(obj, slope_factor, axis):
    if axis == "x":
        slope_matrix = np.array([
            [1, slope_factor],
            [0, 1]
        ])
    elif axis == "y":
        slope_matrix = np.array([
            [1, 0],
            [slope_factor, 1]
        ])
    else:
        raise ValueError("Invalid axis")
    return np.dot(obj, slope_matrix)


def universal_transformation(obj, transformation_matrix):
    return np.dot(obj, transformation_matrix)


def main():
    asymmetric_vectors = np.array([
        [0, 0],
        [2, 1],
        [1, 3],
        [3, 4],
        [2, 2],
        [4, 1],
        [0, 0]
    ])

    hexagon = np.array([
        [1, 2],
        [2, 4],
        [4, 5],
        [5, 3],
        [3, 1],
        [1, 1],
        [1, 2]
    ])

    object_3d = np.array([
        [0, 0, 0],
        [1, 2, 1],
        [2, 0, 3],
        [1, 3, 2],
        [0, 0, 0]
    ])

    plot_object(asymmetric_vectors, "Asymmetric vectors (original)", 'r')
    plot_object(hexagon, "Hexagon (original)", 'b')
    plot_object(object_3d, "3D object (original)", 'g')

    # Rotation

    # asymmetric_vectors_rotated = rotate_object(asymmetric_vectors, 90)
    # hexagon_rotated = rotate_object(hexagon, 90)
    object_3d_rotated = rotate_object(object_3d, 90)

    # plot_object(asymmetric_vectors_rotated, "Asymmetric vectors (rotated)", 'g')
    # plot_object(hexagon_rotated, "Hexagon (rotated)", 'y')
    plot_object(object_3d_rotated, "3D object (rotated)", 'purple')

    # Scaling

    # asymmetric_vectors_scaled = scale_object(asymmetric_vectors, 2)
    # hexagon_scaled = scale_object(hexagon, 2)
    #
    # plot_object(asymmetric_vectors_scaled, "Asymmetric vectors (scaled)", 'g')
    # plot_object(hexagon_scaled, "Hexagon (scaled)", 'y')

    # Reflection

    # asymmetric_vectors_reflected_x = reflect_object(asymmetric_vectors, "x")
    # asymmetric_vectors_reflected_y = reflect_object(asymmetric_vectors, "y")
    # hexagon_reflected_y = reflect_object(hexagon, "y")
    # hexagon_reflected_x = reflect_object(hexagon, "x")
    #
    # plot_object(asymmetric_vectors_reflected_x, "Asymmetric vectors (reflected x)", 'g')
    # plot_object(hexagon_reflected_x, "Hexagon (reflected x)", 'y')
    # plot_object(asymmetric_vectors_reflected_y, "Asymmetric vectors (reflected y)", 'purple')
    # plot_object(hexagon_reflected_y, "Hexagon (reflected y)", 'orange')

    # Slope of axis

    # slope_x_asymmetric_vectors = slope_of_axis(asymmetric_vectors, 2, "x")
    # slope_y_asymmetric_vectors = slope_of_axis(asymmetric_vectors, 0.5, "y")
    # slope_x_hexagon = slope_of_axis(hexagon, 2, "x")
    # slope_y_hexagon = slope_of_axis(hexagon, 0.5, "y")
    #
    # plot_object(slope_x_asymmetric_vectors, "Slope of x-axis", 'g')
    # plot_object(slope_y_asymmetric_vectors, "Slope of y-axis", 'y')
    # plot_object(slope_x_hexagon, "Slope of x-axis", 'purple')
    # plot_object(slope_y_hexagon, "Slope of y-axis", 'orange')

    # Universal transformation

    # transformation_matrix = np.array([
    #     [-5, 7],
    #     [0.8, 3]
    # ])
    #
    # asymmetric_vectors_transformed = universal_transformation(asymmetric_vectors, transformation_matrix)
    # hexagon_transformed = universal_transformation(hexagon, transformation_matrix)
    #
    # plot_object(asymmetric_vectors_transformed, "Asymmetric vectors (transformed)", 'pink')
    # plot_object(hexagon_transformed, "Hexagon (transformed)", 'skyblue')


if __name__ == "__main__":
    main()
