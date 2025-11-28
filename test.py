# 1. Setting up the start
num_A = 0
num_B = 1

# Tell the computer to print the first two numbers right away
print(num_A)
print(num_B)

# 2. Start the Loop: Do the rest of the steps 8 more times (to get 10 numbers total)
for count in range(8):
    # Step A: Add them to get the Next number
    Next_Num = num_A + num_B

    # Step B & C: Shift the numbers!
    num_A = num_B  # The old B becomes the new A
    num_B = Next_Num # The new Next_Num becomes the new B

    # Print the result
    print(Next_Num)