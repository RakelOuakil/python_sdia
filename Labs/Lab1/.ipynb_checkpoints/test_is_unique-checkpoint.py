def test_is_unique():
    assert is_unique([])
    assert is_unique([1])
    assert is_unique([1, 2, 3, 4])

    assert not is_unique([2, 3, 2])


