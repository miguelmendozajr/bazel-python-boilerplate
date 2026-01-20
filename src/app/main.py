import numpy as np

def sum(arr1: np.ndarray, arr2: np.ndarray) -> int:
    result = np.sum(arr1 + arr2)
    return result

def main():
    result = sum(
        np.array([1, 2, 3, 4, 5]),
        np.array([10, 20, 30, 40, 50]),
    )
    print(f"Sum of arrays: {result}")

if __name__ == "__main__":
    main()