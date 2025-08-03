# Number of rows
N = 5

# Outer loop runs N times, once for each row
for i in range(N):
    # Inner loop prints 'i - 1' spaces
    for j in range(i):
        print(" ", end="")
      
    # Inner loop prints '2 * (N - i) + 1' stars
    for k in range(1,2*N+i):
        print("*", end="")
    
    # Move to the next line
    print()
