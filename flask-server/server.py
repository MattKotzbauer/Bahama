from flask import Flask
from flask import request
import json

import rsa

app = Flask(__name__)

# Api Route

questions = []


@app.route("/question", methods=["POST"], strict_slashes=False)
def question():
    user_id = json.loads(request.data.decode('utf-8'))['user_id']
    question_id = json.loads(request.data.decode('utf-8'))['question_id']
    question = json.loads(request.data.decode('utf-8'))['question']
    value = json.loads(request.data.decode('utf-8'))['value']

    questions.append(
        {"user_id": user_id, "question_id": question_id, "question": question, "value": value})

    print(f"{questions}")
    '''
    # Assume user 1: encrypt with user 2's public key
    with open("user2_public.pem", "rb") as fileRead:
        user2_public = rsa.PublicKey.load_pkcs1(fileRead.read())
3
    input = str(user_input)
    encrypted_message_fromUser1 = rsa.encrypt(input.encode(), user2_public)

    print(f"Encrypted Message: {encrypted_message_fromUser1}")

    # (send to blockchain)
    '''

    return questions


@app.route("/answer", methods=["POST"], strict_slashes=False)
def answer():
    answer = json.loads(request.data.decode('utf-8'))['answer']

    with open("user2_public.pem", "rb") as fileRead:
        user2_public = rsa.PublicKey.load_pkcs1(fileRead.read())

    input = str(answer)
    encrypted_message_fromUser1 = rsa.encrypt(input.encode(), user2_public)

    return encrypted_message_fromUser1


if __name__ == "__main__":
    app.run(debug=True)
