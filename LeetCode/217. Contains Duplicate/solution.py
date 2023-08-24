class Solution(object):
    def containsDuplicate(self, nums):
        empty_set = set()
        for i in range(0, len(nums)):
            if (nums[i] in empty_set) == True:
                print("Contains duplicate")
                return True
            else:
                empty_set.add(nums[i])
        print("No duplicates!")
        return False

instance = Solution()
print(instance.containsDuplicate([1,2,3,4,5,6,7]))
print(instance.containsDuplicate([1,2,3,4,5,6,1]))
