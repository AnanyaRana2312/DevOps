def quiz_game():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Who is known as the Father of the Nation in India?",
            "options": ["A. Jawaharlal Nehru", "B. Subhash Chandra Bose", "C. Mahatma Gandhi", "D. Sardar Patel"],
            "answer": "C"
        },
        {
            "question": "Which is the national animal of India?",
            "options": ["A. Lion", "B. Elephant", "C. Tiger", "D. Leopard"],
            "answer": "C"
        },
        {
            "question": "Which river is considered the holiest in India?",
            "options": ["A. Yamuna", "B. Ganga", "C. Brahmaputra", "D. Narmada"],
            "answer": "B"
        },
        {
            "question": "Who wrote the Indian national anthem?",
            "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Subhash Chandra Bose"],
            "answer": "A"
        },
        {
            "question": "What is the national flower of India?",
            "options": ["A. Lotus", "B. Rose", "C. Sunflower", "D. Marigold"],
            "answer": "A"
        },
        {
            "question": "Which festival is known as the festival of lights in India?",
            "options": ["A. Holi", "B. Diwali", "C. Dussehra", "D. Navratri"],
            "answer": "B"
        },
        {
            "question": "Which sport is most commonly associated with India?",
            "options": ["A. Football", "B. Cricket", "C. Hockey", "D. Badminton"],
            "answer": "B"
        },
        {
            "question": "Which is the highest civilian award in India?",
            "options": ["A. Padma Shri", "B. Bharat Ratna", "C. Padma Bhushan", "D. Padma Vibhushan"],
            "answer": "B"
        },
        {
            "question": "Who was the first Prime Minister of India?",
            "options": ["A. Indira Gandhi", "B. Lal Bahadur Shastri", "C. Jawaharlal Nehru", "D. Rajendra Prasad"],
            "answer": "C"
        }
    ]
    
    score = 0
    
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    
    print(f"\nYour final score is {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
