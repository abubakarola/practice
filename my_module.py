def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_vowels(text):
    """Count the number of vowels in a given string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)
