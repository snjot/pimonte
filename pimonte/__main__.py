import math
import random
import time
from typing import List, Tuple


def generate_random_point2d() -> Tuple[float, float]:
    return (random.random(), random.random())


def generate_multiple_random_points2d(num_samples: int) -> List[Tuple[float, float]]:
    points = []
    for _ in range(num_samples):
        points.append(generate_random_point2d())
    return points


def calculate_l2norm(point2d: Tuple[float, float]) -> float:
    return math.sqrt(point2d[0] ** 2 + point2d[1] ** 2)


def count_points_within_quadrant(l2norms: List[float]) -> int:
    num_points = 0
    for l in l2norms:
        if l <= 1:
            num_points += 1
    return num_points


def calculate_pi(num_samples: int) -> float:
    points = generate_multiple_random_points2d(num_samples)
    l2norms = [calculate_l2norm(p) for p in points]
    num_points_within_quadrant = count_points_within_quadrant(l2norms)
    pi = 4 * num_points_within_quadrant / num_samples
    return pi


if __name__ == "__main__":
    random.seed(0, version = 2)

    tic = time.time()
    pi = calculate_pi(10_000_000)
    tac = time.time()

    print(f"pi = {pi}; ({tac - tic} sec)")
