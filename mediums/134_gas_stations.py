# There are n gas stations along a circular route, where the amount of gas at
# the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from the ith station to its next (i + 1)th station. You begin the
# journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's
# index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1. If there exists a solution, it is guaranteed to be
# unique

# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas.
# Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel
# back to station 3.
# Therefore, return 3 as the starting index.

# Example 2:
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas.
# Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you
# start.
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            O(n)
        """

        # If the cost is higher than the gas, it is impossible to complete
        # the journey, in all other cases it should be possible
        if sum(gas) < sum(cost):
            return -1
        # Start at the first station with an empty tank
        starting_station = 0
        gas_tank = 0
        # Iterate through all of the stations
        for i in range(len(gas)):
            # At each station assess if it's possible to go to the next
            # To go to the next one, you need to fill as much gas at your
            # current station, and then assess the cost needed for the journey
            gas_tank = gas_tank - cost[i] + gas[i]
            # If the journey is not possible, you need to start at the next
            # station. Since you are guaranteed to have a solution this
            # checks all the stations. Remember that since you are starting
            # out again, you need to reset the gas.
            if gas_tank < 0:
                starting_station = i + 1
                gas_tank = 0

        return starting_station

    def On2SolutionCheckValid(self, gas: List[int], cost: List[int], \
        stations: int) -> bool:
        gas_tank = gas[0]
        previous_station = 0

        for next_station in range(1, stations):
            if gas_tank < cost[previous_station]:
                return False
            gas_tank = gas_tank - cost[previous_station] + gas[next_station]
            previous_station = next_station

        if gas_tank < cost[stations - 1]:
            return False

        return True

    def On2Solution(self, gas: List[int], cost: List[int]) -> int:
        """
            O(n^2)
        """
        # Iterate through the array and check if the journey is possible
        # So at each element, explore till the end of the list and then
        # explore the start of the list
        # As an example, at index 1, do 2, 3, 4 (till you reach the length)
        # in one for loop and then do 0 in another for loop
        stations = len(gas)

        for station in range(stations):
            # Re-arrange the values for the gases and costs so that you always
            # have them in the right order
            gas_temp = gas[station:] + gas[:station]
            cost_temp = cost[station:] + cost[:station]
            # Check if you have a valid combination
            if self.On2SolutionCheckValid(gas_temp, cost_temp, stations):
                return station

        # Arbitrary return, for completeness but code never reaches here
        return -1
