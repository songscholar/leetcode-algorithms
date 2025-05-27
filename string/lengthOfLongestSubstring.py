class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        maxLen = 1
        left = 0
        list = set(s[0])

        for i in range(1, len(s)):
            cur = s[i]
            while cur in list:
                list.remove(s[left])
                left += 1
            curLen = i - left + 1
            maxLen = max(maxLen, curLen)
            list.add(cur)

        return maxLen

if __name__ == '__main__':
    solution = Solution().lengthOfLongestSubstring("abcbdafsfeagdg")
    print(solution)
