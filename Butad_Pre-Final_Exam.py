# Define a function to check if a number is prime
def is_prime(n):
  # If n is less than 2, it is not prime
  if n < 2:
    return False
  # Loop from 2 to the square root of n
  for i in range(2, int(n**0.5) + 1):
    # If n is divisible by i, it is not prime
    if n % i == 0:
      return False
  # If none of the above, it is prime
  return True

# Ask the user to enter the start and end of the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# If start is negative, prompt a message
if start < 0:
  print("Enter a non-negative number.")
# If end is less than start, prompt a message
elif end < start:
  print("Enter a number greater than", start)
# If start or end is zero, terminate the program
elif start == 0 or end == 0:
  print("Program terminated.")
# Otherwise, loop from start to end and display the prime numbers
else:
  print("The prime numbers in the range are:")
  for i in range(start, end + 1):
    if is_prime(i):
      print(i)

