from num_chop import chop

def test_num_chop():
    assert chop(1.234, 2) == 1.2
    assert chop(0.1234, 2) == 0.12
    assert chop(1234, 2) == 1200
    assert chop(-0.1234, 2) == -0.12
    assert chop(-1234, 2) == -1200


if __name__ == '__main__':
    test_num_chop()
    print('Tests have passed.')
