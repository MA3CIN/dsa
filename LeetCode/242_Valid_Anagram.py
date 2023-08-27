class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s)!=len(t)):
            return False
        # dict for counters
        s_dict,t_dict = {}, {}
        for i in range(len(t)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        return s_dict == t_dict
