from unittest import TestCase
import pytest
import numpy as np
class TestCase(TestCase):
    def test_placeholder(self):
        print("hello world")
        a = [0,1,2]
        b = [0,1,2]

        assert a==b


if __name__ == "__test_placeholder__":
    pytest.test_placeholder()