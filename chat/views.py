from re import T
from django.shortcuts import render
from .forms import *
from .models import *
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()

def chat(request):
    all = Chat.objects.all() # all chat objects
    id_externe = request.POST.get('submit_button', None) # the one he wants to contact
    id_interne = request.user.id # our logged in user
    username_interne = User.objects.get(id = id_interne).username # the username of our logged in user
    current_messages = [] # to use later
    other_messages = [] # to use later
    b = False
    print(id_externe)
    if id_externe != None: # if we are coming from the page of matching
        username_externe = User.objects.get(id = id_externe).username # we get the username of the one we wanna talk to
        for conversation in all: # we search in all conversations
            if (str(conversation.etudiant1) == str(username_externe) and str(conversation.etudiant2) == str(username_interne)) or (str(conversation.etudiant1) == str(username_interne) and str(conversation.etudiant2) == str(username_externe)): # we check if a conv between em already exists
                """print('here1') # if yes
                id = conversation.id # we get the id of the convo
                user = User.objects.filter(id = id_interne) # we search for our request.user
                user.update(id_conv = id)
                user = User.objects.filter(id = id_externe) # question : wht the hell are we uptading
                user.update(id_conv = id)
                b = True
                break"""
                print('here')
                b = True
                pass
            else: # we did not find a conv for em, so we create one
                print('here2')
                new_object = Chat.objects.create(etudiant1 = username_externe, etudiant2 = username_interne) # we create a new conv with the usernames of these two
                new_object.save() # we save it in the db
                id_new_object = new_object.id # we get the id of the conv we just checked
                user = User.objects.filter(id = id_interne) # we get our logged in user
                user.update(id_conv = id_new_object) #we update the id of conv with new id of conv
                user = User.objects.filter(id = id_externe) # we search for external user
                user.update(id_conv = id_new_object)# we update the id of conv
                b = True
        if not b :
            new_object = Chat.objects.create(etudiant1 = username_externe, etudiant2 = username_interne) # we create a new conv with the usernames of these two
            new_object.save() # we save it in the db
            id_new_object = new_object.id # we get the id of the conv we just checked
            user = User.objects.filter(id = id_interne) # we get our logged in user
            user.update(id_conv = id_new_object) #we update the id of conv with new id of conv
            user = User.objects.filter(id = id_externe) # we search for external user
            user.update(id_conv = id_new_object)# we update the id of conv
    new_message = request.POST.get('new_message', None) # we get a message from the user
    user = User.objects.get(id = id_interne)
    id_conv = user.id_conv # this is the id of conv from logged in user
    print(id_conv)
    if new_message != None :  # if theres a msg     
        conversation = Chat.objects.get(id = id_conv) # we get the conv
        messages = str(conversation.messages) # we get the messages
        messages += new_message + '$$$' + str(username_interne) + '###' # we concatenate the new msg
        conversation = Chat.objects.filter(id = id_conv)
        conversation = conversation.update(messages = messages) # we update the convo
    conversation = Chat.objects.get(id = id_conv) # no msg, we get the conv anyways
    messages = str(conversation.messages).split('###') # we split it
    if messages != '':
        print(messages)
        for message in messages :
            if message != '':
                message = message.split('$$$')
                print(message)
                if str(message[1]) == str(username_interne):
                    current_messages.append(message[0]) # between current user
                else:
                    other_messages.append(message[0]) # and other messages
                
    usertwo = User.objects.exclude(id = int(id_interne)) # user two is not the logged in
    usertwo = usertwo.get(id_conv = id_conv).username # but he has same id for convo
    print(user)
    context = {
        'currentmessages' : current_messages,
        'other_messages' : other_messages,
        "usertwo" : usertwo,
        'userone' : username_interne, # we return everything
    }
    return render(request, 'chat.html',context)
