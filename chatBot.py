import json
from difflib import get_close_matches

#loading data from json file

def load_data(file_path:str) -> dict:
    with open(file_path,'r') as file:
        data: data = json.load(file)
    return data

#saving data to json file

def save_data(file_path:str, data:dict) -> None:
    with open(file_path,'w') as file:
        json.dump(data,file, indent=2)

#finding the best match for the user question

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.5)
    return matches[0] if matches else None

#finding the answer for the best match

def get_answer_for_questions(question: str, data: dict) -> str | None:
    for q in data["questions"]:
        if q["question"] == question:
            return q["answer"]
        

#Creating our chat bot
        

def chat_bot():
    data:dict = load_data("data.json")

    while True:
        usser_input: str = input("Enter your question: ")

        if usser_input.lower() == "quit":
            break

        best_match: str | None = find_best_match(usser_input, [q["question"] for q in data["questions"]])

        if best_match:
            answer: str = get_answer_for_questions(best_match, data)
            print(f'Bot: {answer}')
        else:
            print("Bot: Sorry, I don't know the answer to that question. Please teach me to help me get better.")
            new_answer: str = input("Enter the answer to your question or enter 'skip' to skip: ")

            if new_answer.lower() != "skip":
                data["questions"].append({"question": usser_input, "answer": new_answer})
                save_data("data.json", data)    
                print("Bot: Thank you for teaching me. I will remember that for next time.")


#running the chat bot

if __name__ == "__main__":
    chat_bot()