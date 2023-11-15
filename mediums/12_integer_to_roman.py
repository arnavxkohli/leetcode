# Roman numerals are represented by seven different symbols: I, V, X, L, C,
# D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.


# Example 1:
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.

# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
class Solution:
    def intToRoman(self, num: int) -> str:
        '''O(n)'''
        numerals = {0:'',1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        num_str = str(num)
        length = len(num_str)
        roman = ''
        # Iterate through all of the numbers
        for i, num_val in enumerate(num_str):
            # Keep the number of zeros aside, useful calculation
            scale_factor = 10**(length-1-i)
            num_val = int(num_val)
            # If the value is 9, then you need to perform a special calculation
            if num_val == 9:
                roman += numerals[scale_factor] + numerals[scale_factor*10]
            # Otherwise proceed as normal
            else:
                # Self explanatory, get 500 out if for example you are at 800
                upper_val = (num_val//5 * scale_factor) * 5
                # Get 3, don't get 100 from scale factor so that you can query
                # the dictionary
                lower_val = num_val%5
                processed_lower_val = ''
                # 4s are the discrepancy, different logic for if 4 or not
                if lower_val != 4:
                    processed_lower_val = numerals[scale_factor]*lower_val
                else:
                    processed_lower_val = numerals[scale_factor] + \
                        numerals[5*scale_factor]
                # Add to the value after all processing is done
                roman += numerals[upper_val] + processed_lower_val

        return roman

    def stupidSolution(self, num: int) -> str:
        ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        hdrs = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        thds = ['','M','MM','MMM']

        return thds[num/1000] + hdrs[(num%1000)/100] + \
            tens[(num%100)/10] + ones[num%10]
