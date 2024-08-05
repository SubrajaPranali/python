class Operations:
    # Odd or Even
    def OddEven():
        num = int(input("Enter a number: "))
        if (num % 2) == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

    # Eligibility for Marriage
    def EligibilityForMarriage():
        gender = input("Your gender: ").lower()
        age = int(input("Your age: "))
        if gender == 'male':
            if age >= 21:
                print("eligible")
            else:
                print("not eligible")
        elif gender == 'female':
            if age >= 18:
                print("eligible")
            else:
                print("not eligible")

    # Calculate Percentage
    def Percentage():
        a = int(input("Subject 1: "))
        b = int(input("Subject 2: "))
        c = int(input("Subject 3: "))
        d = int(input("Subject 4: "))
        e = int(input("Subject 5: "))
        total = a + b + c + d + e
        print("Total:", total)
        per = float(total) * (100 / 500)
        print("Percentage:", per)

    # Calculate Triangle Area and Perimeter
    def Triangle():
        height = int(input("Height: "))
        breadth = int(input("Breadth: "))
        area = breadth * height / 2
        print("Area formula: (height * breadth) / 2")
        print("Area:", area)
        
        height1 = int(input("Height1: "))
        height2 = int(input("Height2: "))
        breadth = int(input("Breadth: "))  # Note: This overwrites the previous breadth value
        perimeter = height1 + height2 + breadth
        print("Perimeter formula: height1 + height2 + breadth")
        print("Perimeter of Triangle:", perimeter)

    # List Sub-fields in AI
    def SubfieldsInAI():
        fields = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        print("Sub-fields in AI are:")
        for field in fields:
            print(field)
