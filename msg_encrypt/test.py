import random
# from .models import Messages


def encrypt_message(new_message):
    encryption = {'a' : '😀', 'b': '😁', 'c' : '😂', 'd' : '🤣', 'e' : '😄', 'f' : '😅', 'g' : '😆', 'h' : '😉', 'i' : '😊', 'j' : '😋', 'k' : '😎', 'l' : '😍', 'm' : '😘', 'n' : '🥰', 'o' : '😗', 'p' : '😙', 'q' : '🥲', 'r' : '😚', 's' : '🙂', 't' : '🤗', 'u' : '🤩', 'v' : '🤔', 'w' : '🫡', 'x' : '🤨', 'y' : '😐', 'z' : '😑', 'A' : '😶', 'B' : '🫥', 'C' : '😶‍🌫️', 'D' : '🙄', 'E' : '😏', 'F' : '😣', 'G' : '😥', 'H' : '😮', 'I' : '🤐', 'J' : '😯', 'K' : '😪', 'L' : '😫', 'M' : '🥱', 'N' : '😴', 'O' : '😌', 'P' : '😛', 'Q' : '😜', 'R' : '😝', 'S' : '🤤', 'T' : '😒', 'U' : '😓', 'V' : '😔', 'W' : '😕', 'X' : '🙃', 'Y' : '🫠', 'Z' : '🤑'}
    encrypted_message = ''
    for char in new_message:
        encrypted_char = encryption.get(char, char)
        encrypted_message += encrypted_char
    enc_list = list(encrypted_message)
    # print(enc_list)
    random.shuffle(enc_list)
    shuffled_message = ''.join(enc_list)
    return shuffled_message

def check_duplicate(message, encrypted):
    msgs_list = Messages.objects.values('message')
    encrypted_list = Messages.objects.values('encryption')
    print(msgs_list, encrypted_list)
    if message in msgs_list:
        return True
    if encrypted in encrypted_list:
        return True
    
new_message = "hello world"
encrypted = "💀💀"
duplicate = True
while(duplicate):
    if not check_duplicate(new_message, encrypted):
        duplicate = False
    else:
        encrypted = encrypt_message(new_message)
if(check_duplicate(new_message, encrypted)):
    print("same")
else:
    print("not same")
