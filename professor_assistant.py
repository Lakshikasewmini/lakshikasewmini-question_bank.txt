import random

print("Welcome to professor assistant version 1.0.")

name = input("Please Enter Your Name: ")

print("Hello Professor", name + ", I am here to help you create exams from a question bank.")

while True:
    choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ")

    if choice.lower() == "no":
        print("Thank you professor", name + ". Have a good day!")
        break

    elif choice.lower() == "yes":
        path = input("Please Enter the Path to the Question Bank: ")

        try:
            file = open(path, "r")
            lines = file.readlines()
            file.close()

            print("Yes, indeed the path you provided includes questions and answers.")

            num = int(input("How many question-answer pairs do you want to include in your exam? "))

            total_pairs = len(lines) // 2

            if num > total_pairs:
                print("Sorry, there are only", total_pairs, "question-answer pairs in the file.")
                continue

            output = input("Where do you want to save your exam? ")

            out_file = open(output, "w")

            used = []

            for i in range(num):
                r = random.randint(0, total_pairs - 1)

                while r in used:
                    r = random.randint(0, total_pairs - 1)

                used.append(r)

                q_index = r * 2
                a_index = q_index + 1

                out_file.write("Q" + str(i + 1) + ": " + lines[q_index])
                out_file.write("Answer: " + lines[a_index] + "\n")

            out_file.close()

            print("Congratulations Professor", name + ". Your exam is created and saved in", output)

        except:
            print("Error: File not found. Please check the file path.")

    else:
        print("Please type Yes or No only.")
if __name__ == "__main__":
    
    main()

