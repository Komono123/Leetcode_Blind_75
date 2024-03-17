
from typing import List

class Hash_Map:

    """ All Hash Map related questions will be added here."""

    def two_sum(self,nums:List[int],target: int) -> List[int]:

        """Unordered array, Ex: [2,1,5,3] and the target is 4, return [1,3] as index"""
        """核心思想 hash map"""
        
        hash_map = {}

        for i in range(len(nums)):

            seek = target - nums[i]

            if seek in hash_map.keys():

                return [hash_map[seek],i]
            
            else:

                hash_map[nums[i]] = i
    
    def two_sum_ii(self,nums:List[int],target: int) -> List[int]:
        """Given a sorted array, Ex: [1,3,4,5,7,11] and target 9, return [1,2] as index"""
        """核心思想 two pointer 比大小"""

        l,r = 0, len(nums) - 1
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum > target:
                r -= 1 # sorted array attributes
            elif curSum < target:
                l += 1
            else:
                return [l,r] # since guarantee a answer.
    
    def three_sum(self, nums: List[int]) -> List[int]:

        """Given a array Ex: [-1,0,1,2,-1,-4], return the index of three numbers that added up to 0,
        The answer is [-1,1,2], [-1,0,1] with no duplicate triples"""

        """核心思想： 排序，转化为 for loop 遍历确认a, 因为排序了所以a有重复直接跳过，b + c 用two sum ii 双指针思想找答案，
        ⚠️双指针中的指针遍历找所有答案"""

        res = []
        nums.sort()  # [-4, -1, -1, 0, 1, 2]

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: # for loop 遍历确认a, 因为排序了所以a有重复直接跳过
                continue
            else:
                l ,r = i + 1, len(nums) - 1      # l = r + 1

                while l < r:

                    threeSum = a + nums[l] + nums[r]

                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else:
                        res.appedn([a, nums[l], nums[r]]) # find answer [-1,-1,2], continue on searching on [-1, 0, 1, 2]
                        l += 1 # update the left pointer to 0, continue searching
                        while nums[l] == nums[l - 1] & l < r:  # Case when [-1,-1,-1,0,1,2], continue updating left pointer since -1 is duplicate
                            l += 1
            
        return res


        



class Binary_Search:

    def simpliest_binary_search(self):
        print("0")
    
    def search_rotated_sort(self,nums:List[int], target:int) -> int:
        """Given a sorted and rotated array, Ex: [4,5,1,2,3], check if 2 in it."""

        """Step1: [4,5,6,7,1,2,3]: make sure if mid belongs to the right or left portion, here 7 belongs to the [4,5,6,7]
        right portion. 
           Step2: Subcase: If target greater than mid, search the right portion since mid is the largest
                  else means target smaller than mid, and two subcases occurs for [4,5,6]/[1,2,3]
                  And we compare mid with nums[l], if target < nums[l], go right portion, else left portion"""
        
        l, r = 0, len(nums) - 1
        while l <= r: #[1]

            m = (l + r) // 2

            if nums[m] == target:
                return target
            
            else: # 先判断m属于左边还是右边
                if nums[m] >= nums[l]: # m属于左半区
                    if target > nums[m]:
                        l = m + 1
                    elif target < nums[l]: # 可以和前一条件合并
                        l = m + 1
                    else:
                        r = m -1 
                
                else: # m属于右半区
                    if target < nums[m]:
                        r = m - 1
                    elif target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
        return -1 # 没找到




class Solution:

    # Maximum subarray sum
    """ Ex: [-2,1,-3,4,-1,2,1,-5,4] ---> result: 6 [4,-1,2,1]"""

    def max_sum_subarray(self,nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        else:

            maxSum = 0 # return the final result, also a threshold to compare with curSum
            curSum = 0 # hold my current sum

            for n in nums:
                curSum += n
                if curSum < 0:
                    curSum = 0
                
                maxSum = max(curSum, maxSum)
        
        return maxSum



    def maxStock(self, nums: List[int]) -> int:
        l,r = 0,1
        maxReturn = 0
        while r < len(nums):
            curMax = nums[r] - nums[l]
            if curMax < 0:
                l = r
                r = l + 1

            else:
                maxReturn = max(maxReturn,curMax)
                r += 1
        
        return maxReturn



result = Hash_Map()
gen= [2,1,5,3]
print(result.two_sum(gen,4))


