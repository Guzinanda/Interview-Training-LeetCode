'''
@   Longest Substring Without Repeating Characters | 03

@   Problem
    Given a string s, find the length of the longest substring without repeating characters.

@   Example
    Input:  s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

@   Template

'''

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    used = {}

    max_length = 0
    start = 0

    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
            
        used[c] = i

    return max_length


# TEST _______________________________________________________________________________

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
