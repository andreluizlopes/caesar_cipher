import pytest
from cipher import *

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class TestCipher:
  def test_all_lower(self):
    assert all_lower('AAAA') == 'aaaa'

  def test_find_char(self):
    assert find_char(',! ') == ',! '