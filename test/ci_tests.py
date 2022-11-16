from unittest import TestCase
import pytest
import numpy as np

class test_placeholder(TestCase):
    def test_placeholder(self):
        print("hello world")
        a = [0,1,2]
        b = [0,1,2]

        assert a==b

print(test_placeholder())