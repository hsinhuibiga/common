#Capacity To Ship Packages Within D Days

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        l = max(weights)
        r = sum(weights)
        # [l, r)
        while l < r:
            mid = l + (r - l) / 2
            need = 1
            cur = 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                l = mid + 1
            else:
                r = mid
        return l