from core import fast_sum_squares

def test_fast_sum_squares():
    assert fast_sum_squares(3) == 5.0  # 0^2 + 1^2 + 2^2 = 5
    assert fast_sum_squares(0) == 0.0