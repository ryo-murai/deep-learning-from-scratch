import numpy as np

def ndim_shape(x):
    print('------------------------------------')
    print(x)
    print(f'ndim:{np.ndim(x)}')
    print(f'shape:{x.shape}')


if __name__ == "__main__":
    ndim_shape(np.array([1,2,3,4]))
    ndim_shape(np.array([[1,2],[3,4],[5,6]]))
