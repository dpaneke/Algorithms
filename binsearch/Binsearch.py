from typing import Union, Optional

class Bsearch:
    @staticmethod
    def binsearch_right(a: Union[list[int], list[float]], x: Union[int, float]) -> Optional[int]:
        """finds min i : a_i >= x"""
        if not a or x > a[-1]: return None
        if x <= a[0]: return 0
        left, right = 0, len(a) - 1
        while right - left > 1:
            middle = (left + right) // 2
            if x <= a[middle]:
                right = middle
            else:
                left = middle
        return right

    @staticmethod
    def binsearch_left(a: Union[list[int], list[float]], x: Union[int, float]) -> Optional[int]:
        """finds max i : a_i <= x"""
        if not a or x < a[0]: return None
        if x >= a[-1]: return len(a) - 1
        left, right = 0, len(a) - 1
        while right - left > 1:
            middle = (left + right) // 2
            if a[middle] <= x:
                left = middle
            else:
                right = middle
        return left