# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:35:59 2020

@author: vicky
"""
import sys

class Solution:
    def isMapping(self, string1, string2):
        l1, l2 = len(string1), len(string2)
        if l1 != l2:
            return False
        mapDict = {}
        for i in range(len(string1)):
            if string1[i] in mapDict:
                if mapDict[string1[i]] != string2[i]:
                    return False
            else:
                mapDict[string1[i]] = string2[i]
        return True
if __name__ == "__main__":
    sol = Solution()
    str1, str2 = str(sys.argv[1]), str(sys.argv[2])
    print(str1, str2)
    print(sol.isMapping(str1, str2))