def book_club_points():
    # User inputs number of books purchased
    while True:
        try:
            books_purchased = int(input("Enter the number of books you have purchased this month: "))
            if books_purchased < 0:
                print("    Number of books cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("    Invalid input. Please enter an integer.")

    # Determination of points awarded
    if books_purchased == 0:
        points = 0
    elif books_purchased == 2:
        points = 5
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 6:
        points = 30
    elif books_purchased >= 8:
        points = 60
    else:
        points = 0  # Default case if conditions change

    # Display the points
    print(f"\nYou have earned {points} points for purchasing {books_purchased} books.")

book_club_points()
