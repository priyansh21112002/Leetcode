class Solution:
    def canCompleteCircuit(self, gas: List[int], consumption: List[int]) -> int:
        total_tank, curr_tank, start = 0, 0, 0

        for i in range(len(gas)):
            total_tank += gas[i] - consumption[i]
            curr_tank += gas[i] - consumption[i]

            if curr_tank < 0:
                start = i + 1
                curr_tank = 0

        return start if total_tank >= 0 else -1