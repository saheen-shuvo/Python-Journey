# Continue and Break statements in Python are used to control the flow of loops. The `continue` statement skips the rest of the code inside the loop for the current iteration and moves to the next iteration. The `break` statement, on the other hand, terminates the loop entirely and transfers control to the statement immediately following the loop.

sum = 0

while count < 10:
    count += 1
    if count == 5:
        continue  # Skip the rest of the code for this iteration when count is 5
    sum += count
    if sum > 20:
        break  # Exit the loop if sum exceeds 20