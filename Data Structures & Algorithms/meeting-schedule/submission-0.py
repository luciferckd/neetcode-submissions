"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # sort the intervals 

        intervals.sort(key=lambda x: x.start)

        # loop this intervals 
        for i in range(1, len(intervals)):

            # check the overlap meetings
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

