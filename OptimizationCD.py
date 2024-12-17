def main():
    # Step 1: Input the number of values and each assignment
    n = int(input("Enter the Number of Values: "))
    op = []
    for i in range(n):
        l = input(f"left: ")  # Read left side of assignment
        r = input(f"right: ")  # Read right side of assignment
        op.append((l, r))

    # Step 2: Display Intermediate Code
    print("\nIntermediate Code")
    for l, r in op:
        print(f"{l} = {r}")

    # Step 3: Dead Code Elimination
    pr = []
    for i in range(n - 1):
        temp = op[i][0]
        for j in range(n):
            if temp in op[j][1]:  # Check if op[i].l is used in op[j].r
                pr.append(op[i])  # If used, it's not dead code
                break
    # Always add the last operation as it's not eliminated
    pr.append(op[n - 1])

    # Display the result after dead code elimination
    print("\nAfter Dead Code Elimination")
    for l, r in pr:
        print(f"{l} = {r}")

    # Step 4: Eliminate Common Expressions
    for m in range(len(pr)):
        tem = pr[m][1]
        for j in range(m + 1, len(pr)):
            if tem in pr[j][1]:  # Check for common subexpression
                t = pr[j][0]
                pr[j] = (pr[m][0], pr[m][1])  # Replace with the optimized version
                # Replace occurrences of pr[j].l in previous expressions
                for i in range(len(pr)):
                    if pr[i][1] and pr[i][1].find(t) != -1:
                        pr[i] = (pr[i][0], pr[i][1].replace(t, pr[m][0]))

    # Display result after common subexpression elimination
    print("\nEliminate Common Expression")
    for l, r in pr:
        print(f"{l} = {r}")

    # Step 5: Final Code Optimization
    final_pr = []
    for i in range(len(pr)):
        duplicate_found = False
        for j in range(i + 1, len(pr)):
            if pr[i][0] == pr[j][0] and pr[i][1] == pr[j][1]:
                duplicate_found = True
                break
        if not duplicate_found:
            final_pr.append(pr[i])

    # Display optimized code
    print("\nOptimized Code")
    for l, r in final_pr:
        print(f"{l} = {r}")

if __name__ == "__main__":
    main()
