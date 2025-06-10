bool isPalindrome(int x) {
    // negative numbers are not palindromes
    if (x < 0) return false;

    int original = x;
    long long reverse = 0;

    while (x > 0) {
        reverse = 10 * reverse + x % 10;
        x /= 10;

        // check for overflow
        if (reverse > INT_MAX) return false;
    }
    
    return original == reverse;
}