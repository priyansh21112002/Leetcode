class Solution:
    def canCompleteCircuit(self, gas: List[int], consumption: List[int]) -> int:
        n = len(gas)

        # Global feasibility check
        if sum(gas) < sum(consumption):
            return -1

        curr_tank = 0
        start = 0

        for i in range(n):
            curr_tank += gas[i] - consumption[i]

            # If fuel drops below 0, reset start
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0

        return start
