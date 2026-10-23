def ispalindrome(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]
print(ispalindrome("A man a plan a canal Panama"))
print(ispalindrome("Hello"))
  # Returns True

    