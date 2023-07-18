from ...hello.hellos import give_me_hi


def test_hello_func():
    assert give_me_hi() == "Hi"
