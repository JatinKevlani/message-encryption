from django.shortcuts import render
from msg_encrypt.models import Message
import random

# Create your views here.
def error_404(request, exception) :
    return render(request, '404.html')

def index(request):
    context = {
        "css_str":"@import url(https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap);.form-section,.slider{transition:.5s ease-in-out}.btn,.form-section,body,header{display:flex}.clkbtn,.slider{background-image:linear-gradient(to right,#ffc36e,#ff925b)}*{margin:0;padding:0;box-sizing:border-box;font-family:Poppins,sans-serif}body{height:100vh;width:100vw;justify-content:center;align-items:center;flex-direction:column;gap:30px;background-color:#e7e7e7}header{width:100%;flex-direction:column;align-items:center;justify-content:center;gap:8px}.heading,a,h1{color:green!important}.heading,a:hover,h1{color:#00f!important;text-decoration:underline 2px!important}.title{font-weight:400;letter-spacing:1.5px}.container{height:600px;width:500px;background-color:#fff;box-shadow:8px 8px 20px grey;position:relative;overflow:hidden}.btn{height:60px;width:300px;margin:20px auto;box-shadow:10px 10px 30px #fed7bc;border-radius:50px;justify-content:space-around;align-items:center}.login,.signup{font-size:22px;border:none;outline:0;background-color:transparent;position:relative;cursor:pointer}.slider{height:60px;width:150px;border-radius:50px;position:absolute;top:20px;left:100px}.moveslider{left:250px}.form-section{height:500px;width:1000px;padding:20px 0;position:relative;left:0}.form-section-move{left:-500px}.login-box,.signup-box{height:100%;width:500px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 40px}.login-box{gap:50px}.signup-box{gap:30px}.ele{height:60px;width:400px;outline:0;border:none;color:#4d4d4d;background-color:#f0f0f0;border-radius:50px;padding-left:30px;font-size:18px}.clkbtn{height:60px;width:150px;border-radius:50px;font-size:22px;border:none;cursor:pointer}@media screen and (max-width:650px){.container{height:600px;width:300px}.title{font-size:15px}.btn{height:50px;width:200px;margin:20px auto}.login,.signup{font-size:19px}.slider{height:50px;width:100px;left:50px}.moveslider{left:150px}.form-section{height:500px;width:600px}.form-section-move{left:-300px}.login-box,.signup-box{height:100%;width:300px}.ele{height:50px;width:250px;font-size:15px}.clkbtn{height:50px;width:130px;font-size:19px}}@media screen and (max-width:320px){.container{height:600px;width:250px}.heading{font-size:30px}.title{font-size:10px}.btn{height:50px;width:200px;margin:20px auto}.login,.signup{font-size:19px}.slider{height:50px;width:100px;left:27px}.moveslider{left:127px}.form-section{height:500px;width:500px}.form-section-move{left:-250px}.login-box,.signup-box{height:100%;width:250px}.ele{height:50px;width:220px;font-size:15px}.clkbtn{height:50px;width:130px;font-size:19px}}",

        "js_str":"let signup=document.querySelector('.signup'),login=document.querySelector('.login'),slider=document.querySelector('.slider'),formSection=document.querySelector('.form-section');document.addEventListener('DOMContentLoaded',()=>{signup.addEventListener('click',()=>{slider.classList.add('moveslider'),formSection.classList.add('form-section-move')}),login.addEventListener('click',()=>{slider.classList.remove('moveslider'),formSection.classList.remove('form-section-move')})});"
    }
    return render(request, 'index.html', context=context)

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