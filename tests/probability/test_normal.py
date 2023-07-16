import numpy as np

import sdr


def test_Q():
    """
    Matlab:
        >> x = -3:0.2:3;
        >> qfunc(x)'
    """
    x = np.arange(-3, 3.2, 0.2)
    p = sdr.Q(x)
    p_truth = np.array(
        [
            0.998650101968370,
            0.997444869669572,
            0.995338811976281,
            0.991802464075404,
            0.986096552486501,
            0.977249868051821,
            0.964069680887074,
            0.945200708300442,
            0.919243340766229,
            0.884930329778292,
            0.841344746068543,
            0.788144601416603,
            0.725746882249926,
            0.655421741610324,
            0.579259709439103,
            0.500000000000000,
            0.420740290560897,
            0.344578258389676,
            0.274253117750074,
            0.211855398583397,
            0.158655253931457,
            0.115069670221708,
            0.080756659233771,
            0.054799291699558,
            0.035930319112926,
            0.022750131948179,
            0.013903447513499,
            0.008197535924596,
            0.004661188023719,
            0.002555130330428,
            0.001349898031630,
        ]
    )

    assert isinstance(p, np.ndarray)
    assert np.allclose(p, p_truth)

    i = np.random.randint(0, x.size)
    pi = sdr.Q(x[i])
    assert isinstance(pi, float)
    assert p[i] == pi
