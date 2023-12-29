from django.shortcuts import render
from msg_encrypt.models import Message
import random

# Create your views here.
def error_404(request, exception) :
    return render(request, '404.html')

def index(request):
    return render(request, 'index.html')

def encrypt(request):
    if request.method == "POST":
        new_message = request.POST.get('message')
        password = request.POST.get('password')
        otu = request.POST.get('otu')
        encrypted = encrypt_message(new_message)
        duplicate = True
        while(duplicate):
            if not check_duplicate(encrypted):
                duplicate = False
            else:
                encrypted = encrypt_message(new_message)
        # print(new_message, password, encrypted) 
        if otu == None:
            new_msg = Message(message = new_message, encryption = encrypted, password = password, one_time_use = False)
        else:
            new_msg = Message(message = new_message, encryption = encrypted, password = password, one_time_use = True)            
        new_msg.save()
        context = {
            'encrypted_string' : encrypted,
        }
    return render(request, 'encrypt.html', context)

def decrypt(request):
    if request.method == "POST":
        user_enc = request.POST.get('user_enc')    
        password = request.POST.get('password')
        # print(user_enc, password)
        content = decrypt_message(user_enc, password)
        if content[0] == True:
            context = {
                "encrypted_string" : content[1]
            }
        else:
            context = {}
    return render(request, 'decrypt.html', context)

def encrypt_message(new_message):
    encryption = {'a' : '😀', 'b': '😁', 'c' : '😂', 'd' : '🤣', 'e' : '😄', 'f' : '😅', 'g' : '😆', 'h' : '😉', 'i' : '😊', 'j' : '😋', 'k' : '😎', 'l' : '😍', 'm' : '😘', 'n' : '🥰', 'o' : '😗', 'p' : '😙', 'q' : '🥲', 'r' : '😚', 's' : '🙂', 't' : '🤗', 'u' : '🤩', 'v' : '🤔', 'w' : '🫡', 'x' : '🤨', 'y' : '😐', 'z' : '😑', 'A' : '😶', 'B' : '🫥', 'C' : '😶‍🌫️', 'D' : '🙄', 'E' : '😏', 'F' : '😣', 'G' : '😥', 'H' : '😮', 'I' : '🤐', 'J' : '😯', 'K' : '😪', 'L' : '😫', 'M' : '🥱', 'N' : '😴', 'O' : '😌', 'P' : '😛', 'Q' : '😜', 'R' : '😝', 'S' : '🤤', 'T' : '😒', 'U' : '😓', 'V' : '😔', 'W' : '😕', 'X' : '🙃', 'Y' : '🫠', 'Z' : '🤑'}
    encrypted_message = ''
    for char in new_message:
        encrypted_char = encryption.get(char, char)
        encrypted_message += encrypted_char
    enc_list = list(encrypted_message)
    random.shuffle(enc_list)
    shuffled_message = ''.join(enc_list)
    return shuffled_message

def check_duplicate(encrypted):
    encrypted_list = Message.objects.values('encryption')
    if encrypted in encrypted_list:
        return True
    return False

def decrypt_message(user_enc, password):
    try:
        stored_message = Message.objects.get(encryption = user_enc)
        if stored_message.password == password:
            if stored_message.one_time_use == True:
                stored_message.delete()
            return True, stored_message.message
        else:
            return False, "Invalid password!"
    except Message.DoesNotExist:
        return False, "Encrypted message not found. Decryption failed."