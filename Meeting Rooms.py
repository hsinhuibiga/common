#Meeting Rooms

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, v):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        v.sort(key = lambda val: val.start)
        return not any(v[i].start < v[i-1].end for i in range(1,len(v)))