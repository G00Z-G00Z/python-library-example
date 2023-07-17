from my_awesome_lib.hello.hellos import give_me_hi


def test_give_me_hi():
    assert give_me_hi() == "Hi"
