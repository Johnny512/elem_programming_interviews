

def reverse_digits(x: int) -> int:
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
        
    return -result if x < 0 else result

if __name__ == "__main__":
   assert reverse_digits(12345) == 54321
   assert reverse_digits(54321) == 12345
   assert reverse_digits(1132) == 2311
   assert reverse_digits(919) == 919
   assert reverse_digits(-159) == -951
   assert reverse_digits(123654789) == 987456321