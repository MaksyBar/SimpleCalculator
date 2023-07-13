print("Calculator".center(30))
while True:
    try:
        a, b = tuple(map(int, input("Input number a and b like a b : ").split(' ')))
    except:
        print("Ups. You chose not correct values.")
        continue
    print(f"""
    Chose the action for the numbers {a} 
    and {b}
    \t 0. Exit
    \t 1. Add {a} + {b}
    \t 2. Minus {a} - {b}
    \t 3. Multiply {a} * {b}
    \t 4. Divide {a}/{b}
    \t 5. Power {a}**{b}
    \t 6. Summ of power ({a}**2) + ({b}**2)
    \t 7. Minus of power ({a}**2) - ({b}**2)
    \t 8. ({a}+{b})**2
    \t 9. ({a}-{b})**2
    \t 10. even numbers in range ({a},{b})
    \t 11. odd numbers in range({a},{b})
    \t 12. {a} % {b}
    """)

    user_choice = input("Your choice: ")

    if user_choice == "0":
        break
