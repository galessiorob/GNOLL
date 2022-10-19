#!/usr/bin/env python3

import pytest
from util import Mock, roll


def test_bw_dsix_over_four():
    # TODO: x6, for all stats
    result = roll("6d6f>=4c")
    assert result >= 0
    assert result <= 6
