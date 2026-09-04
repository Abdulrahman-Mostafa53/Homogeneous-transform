from matrix import Matrix
from math import sin, cos, pi


def create_homogeneous_matrix_ab_y(theta, offsets):
    # create homogeneous matrix for rotating framw about y and translating it by offset

    theta = theta * (pi / 180)
    return Matrix(
        [
            [cos(theta), 0, sin(theta), offsets[0]],
            [0, 1, 0, offsets[1]],
            [-sin(theta), 0, cos(theta), offsets[2]],
            [0, 0, 0, 1],
        ]
    )


def tf_from_camera_frame_to_origin(coordinates):
    # transform coordinate from camera frame to parent frame

    homogeneous_matrix = create_homogeneous_matrix_ab_y(-15, [0.5, 0.0, 0.2])
    points_results = []

    for point in coordinates:
        point = Matrix([[point[0]], [point[1]], [point[2]], [1]])
        result = homogeneous_matrix * point
        result.pop()
        points_results.append(result)

    return points_results


def main():
    points = [[2.0, 0.0, -0.2], [3.5, 1.0, -0.3], [1.5, -0.8, -0.1]]

    # get new transformed coordinated
    results = tf_from_camera_frame_to_origin(points)

    # logging the result
    for i, result in enumerate(results):
        point = []
        for comp in result:
            point.append(round(comp[0], 2))

        print(f"Obstacle {i}: [{point[0]},{point[1]},{point[2]}]")


if __name__ == "__main__":
    main()
