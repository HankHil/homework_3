from move_zeros import move_zeros

def test_move_zeros():
    assert move_zeros([1, 0, 0, 2, 3, 0, 1]) == [1,2,3,1,0,0,0]
    assert move_zeros([3, 0, 4, 6, 0, 1, 7, 0, 0, 0, 4, 4, 0, 1]) == [3,4,6,1,7,4,4,1,0,0,0,0,0,0]
    assert move_zeros([6, 0, 1, 2, 3, 0, 1, 0, 4, 5, 1, 0]) == [6,1,2,3,1,4,5,1,0,0,0,0]