from . import TestRepo3

def test_TestRepo3():
    assert TestRepo3.apply("Jane") == "hello Jane"
