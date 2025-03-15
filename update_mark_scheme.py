import json

FILE_DESTINATION = "./config/mark_scheme.json"
NUM_QUESTION = 25
DEFAULT_CORRECT = 3
DEFAULT_NONE = 1
DEFAULT_INCORRECT = 0

def encode_json(new_mark_scheme):
    with open(FILE_DESTINATION, 'w', encoding='utf-8') as f:
        json.dump(new_mark_scheme, f, ensure_ascii=False, indent=4)


def read_json():
    with open(FILE_DESTINATION) as f:
        mark_scheme = json.load(f)

    return mark_scheme

def get_new_mark_scheme():
    print("Enter the new mark scheme as a column i.e. one question per line...")

    new_mark_scheme = []

    for i in range(NUM_QUESTION):
        answer = input()

        new_mark_scheme.append(answer)

    return new_mark_scheme

def update_mark_scheme(new_mark_scheme, old_mark_scheme):
    for i in range(NUM_QUESTION):
        if f'question_{i+1}' in old_mark_scheme['answer_sheet']:
            old_mark_scheme['answer_sheet'][f'question_{i+1}']['answer'] = new_mark_scheme[i]
        else:
            old_mark_scheme['answer_sheet'][f'question_{i+1}'] = {'answer' : new_mark_scheme[i],
                                                                  'correct' : DEFAULT_CORRECT,
                                                                  'no_answer' : DEFAULT_NONE,
                                                                  'incorrect' : DEFAULT_INCORRECT}
    
    return old_mark_scheme

def main():
    new_mark_scheme = get_new_mark_scheme()
    old_mark_scheme = read_json()
    old_mark_scheme = update_mark_scheme(new_mark_scheme, old_mark_scheme)
    encode_json(old_mark_scheme)
    print("Conversion complete...\nPlease check ./src/mark_scheme.json to verify")

main()
