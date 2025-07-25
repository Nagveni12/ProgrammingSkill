def num_decodings(s):
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0

   
    dp = [0] * (n + 1)
    dp[0] = 1 
    dp[1] = 1  

    for i in range(2, n + 1):
        one_digit = int(s[i - 1])         
        two_digits = int(s[i - 2:i])      

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

message = "111"
print("Input:", message)
print("Number of ways to decode:", num_decodings(message))
