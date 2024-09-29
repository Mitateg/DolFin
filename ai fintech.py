import random

# Define topics for DolFin course
topics = ["Budgeting", "Saving", "Debt Management", "Investing", "Taxation"]

# Define levels for each topic
levels = {
    "Budgeting": ["Basic", "Intermediate", "Advanced"],
    "Saving": ["Basic", "Intermediate", "Advanced"],
    "Debt Management": ["Basic", "Intermediate", "Advanced"],
    "Investing": ["Basic", "Intermediate", "Advanced"],
    "Taxation": ["Basic", "Intermediate", "Advanced"]
}

# Define simple financial exercises for each topic and level
exercises = {
    "Budgeting": {
        "Basic": ["Create a weekly budget for a student with $500 income.",
                  "Identify unnecessary expenses from a sample budget."],
        "Intermediate": ["Track your monthly spending and identify areas to reduce costs.",
                         "Create a budget for a small business."],
        "Advanced": ["Analyze the budgeting strategy of a company and suggest improvements.",
                     "Create a long-term budget including investments and savings goals."]
    },
    "Saving": {
        "Basic": ["Calculate how much you need to save monthly for a $1000 goal in 6 months.",
                  "Identify different types of savings accounts."],
        "Intermediate": ["Create a savings plan with a 10% salary increase.",
                         "Compare savings rates across multiple banks."],
        "Advanced": ["Develop a comprehensive savings strategy for retirement.",
                     "Analyze how inflation impacts your savings."]
    },
    # Other topics...
}


# Function to suggest next exercise based on user's progress
def suggest_exercise(user_progress):
    current_topic = user_progress.get('current_topic', "Budgeting")
    current_level = user_progress.get('current_level', "Basic")
    user_score = user_progress.get('score', 0)

    # Check if user needs to move to the next level or topic
    if user_score >= 80:
        current_level_idx = levels[current_topic].index(current_level)
        if current_level_idx < len(levels[current_topic]) - 1:
            current_level = levels[current_topic][current_level_idx + 1]
        else:
            current_topic_idx = topics.index(current_topic)
            if current_topic_idx < len(topics) - 1:
                current_topic = topics[current_topic_idx + 1]
                current_level = "Basic"
            else:
                return "Congratulations! You have completed all levels of financial literacy!"

    exercise = random.choice(exercises[current_topic][current_level])

    return {
        "next_topic": current_topic,
        "next_level": current_level,
        "exercise": exercise
    }


# Function for basic budgeting exercise prototype with input
def run_basic_exercise():
    print("Exercise: Create a weekly budget for a student with a $500 income.")
    print("You need to divide the $500 into the following categories:")

    categories = ["Rent", "Food", "Entertainment", "Savings", "Other"]
    total_income = 500
    user_budget = {}

    print(f"Total available income: ${total_income}")

    for category in categories:
        while True:
            try:
                amount = float(input(f"How much will you allocate for {category}? $"))
                if amount < 0:
                    print("The amount cannot be negative. Try again.")
                elif sum(user_budget.values()) + amount > total_income:
                    print("You have exceeded the total income. Please allocate a smaller amount.")
                else:
                    user_budget[category] = amount
                    break
            except ValueError:
                print("Please enter a valid number.")

    print("\nYour Budget:")
    for category, amount in user_budget.items():
        print(f"{category}: ${amount}")

    total_spent = sum(user_budget.values())
    if total_spent == total_income:
        print("\nGreat job! You've successfully allocated the entire budget.")
        return 90  # Simulate success and return score
    else:
        print(f"\nYou have ${total_income - total_spent} remaining. Try to allocate all your income.")
        return 60  # Simulate a lower score due to incomplete allocation


# Function to handle the full interaction with the user
def play_dolfin():
    # Get initial user progress
    current_topic = input("Choose a starting topic (Budgeting, Saving, Debt Management, Investing, Taxation): ")
    current_level = input(f"Choose a starting level for {current_topic} (Basic, Intermediate, Advanced): ")

    # Ensure valid input
    if current_topic not in topics or current_level not in levels[current_topic]:
        print("Invalid input! Starting with Budgeting at Basic level.")
        current_topic = "Budgeting"
        current_level = "Basic"

    user_progress = {
        "current_topic": current_topic,
        "current_level": current_level,
        "score": 0  # Start with a default score
    }

    while True:
        next_exercise = suggest_exercise(user_progress)

        if isinstance(next_exercise, str):
            print(next_exercise)
            break  # End the game if all levels are completed

        print(f"\nNext Topic: {next_exercise['next_topic']}")
        print(f"Next Level: {next_exercise['next_level']}")
        print(f"Next Exercise: {next_exercise['exercise']}")

        # Simulate running the basic budgeting exercise
        if next_exercise['exercise'] == "Create a weekly budget for a student with $500 income.":
            user_score = run_basic_exercise()
            user_progress['score'] = user_score
        else:
            # Simulate other exercises (for now we just update the score)
            print(f"Complete the exercise: {next_exercise['exercise']}")
            user_score = int(input("Enter your score (out of 100) for this exercise: "))
            user_progress['score'] = user_score

        # Update progress
        user_progress['current_topic'] = next_exercise['next_topic']
        user_progress['current_level'] = next_exercise['next_level']


# Run the DolFin game
play_dolfin()
