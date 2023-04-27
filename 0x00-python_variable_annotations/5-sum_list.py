#!/usr/bin/env python3
"""type-annotated function sum_list which takes a list input_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns:the sum of the float in the list"""
    return float(sum(input_list))
