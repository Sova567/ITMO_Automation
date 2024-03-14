def test_hw():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)

def test_hw1():
    assert ('home', 'work') == ('home', 'work')

def test_hw2():
    assert not 'QA' == 'QC'