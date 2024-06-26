import csv
import uuid

csv_file = 'payments.csv'


def get_payments():
    message_list = []
    with open(csv_file, mode='r', encoding="utf-8") as file:
        data = csv.reader(file)
        next(data)  # Skip the first row (column names)
        for rows in data:
            message_id, user_id, username, message = rows
            message_list.append({'message_id': message_id, 'user_id': user_id, 'username': username, 'message': message})
    return message_list


def add_payment(user_id, username, message):
    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        message_id = str(uuid.uuid4())
        writer.writerow([message_id, user_id, username, message])


def remove_payment(message_id):
    message_list = get_payments()

    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["MessageID", "UserID", "Username", "Message"])

        for message in message_list:
            if message['message_id'] != message_id:
                writer.writerow([message['message_id'], message['user_id'], message['username'], message['message']])


def get_formatted_payments():
    message_list = get_payments()
    rows_list = []
    for message in message_list:
        rows_list.append(f'MessageID: {message["message_id"]}, UserID: {message["user_id"]}, Username: {message["username"]}, Message: {message["message"]}')
    return "\n".join(rows_list)


def get_first_payment():
    message_list = get_payments()
    return message_list[0] if message_list else None