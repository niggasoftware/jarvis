###########################################################################
###########################################################################
##                                                                       ##
##  Personal assistant for general purpose   -   Made by niggasoftware   ##
##                                                                       ##
###########################################################################
###########################################################################

try:
    import time, sys, os, pafy
    from datetime import datetime
    from chatterbot import ChatBot
except Exception:
    print("[+] To run Jarvis some modules need to be installed, try:")
    print("pip install -r requirements.txt")
    quit()

class c:
    h = '\033[95m'   # HEADER 
    bl = '\033[94m'  # BLUE
    g = '\033[92m'   # GREEN
    w = '\033[93m'   # WARNING
    r = '\033[91m'   # RED
    e = '\033[0m'    # END COLOR
    b = '\033[1m'    # BOLD
    u = '\033[4m'    # UNDERLINE 


jarvis_draw = '''
''' + c.g + '''                     ____
''' + c.g + '''                   _.' :  `._                 '''+ c.r + '''           ,--.-,  ,---.                         ,-.-. .=-.-.  ,-,--.   ''' + c.e + '''
''' + c.g + '''               .-.'`.  ;   .'`.-.             '''+ c.r + '''           |==' -|.--.'  \      .-.,.---.  ,--.-./=/ ,//==/_ /,-.'-  _\ ''' + c.e + '''  
''' + c.g + '''      __      / : ___\ ;  /___ ; \      __    '''+ c.r + '''           |==|- |\==\-/\ \    /==/  `   \/==/, ||=| -|==|, |/==/_ ,_.' ''' + c.e + '''
''' + c.g + '''    ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,  '''+ c.r + '''         __|==|, |/==/-|_\ |  |==|-, .=., \==\,  \ / ,|==|  |\==\  \    ''' + c.e + '''
''' + c.g + '''    :' `.t""--.. '<'''+c.bl+'''@'''+c.g+''' .`;_  ','''+c.bl+'''@'''+c.g+'''>` ..--""j.' `;  '''+ c.r + '''      ,--.-'\=|- |\==\,   - \ |==|   '='  /\==\ - ' - /==|- | \==\ -\   ''' + c.e + '''
''' + c.g + '''         `:-.._J '-.-'L__ `-- ' L_..-;'       '''+ c.r + '''      |==|- |=/ ,|/==/ -   ,| |==|- ,   .'  \==\ ,   ||==| ,| _\==\ ,\  ''' + c.e + '''
''' + c.g + '''           "-.__ ;  .-"  "-.  : __.-"         '''+ c.r + '''      |==|. /=| -/==/-  /\ - \|==|_  . ,'.  |==| -  ,/|==|- |/==/\/ _ | ''' + c.e + '''
''' + c.g + '''               L ' /.------.\ ' J             '''+ c.r + '''      \==\, `-' /\==\ _.\=\.-'/==/  /\ ,  ) \==\  _ / /==/. /\==\ - , / ''' + c.e + '''
''' + c.g + '''                "-.   "--"   .-"              '''+ c.r + '''       `--`----'  `--`        `--`-`--`--'   `--`--'  `--`-`  `--`---'  ''' + c.e + '''
''' + c.h + '''               __.'''+c.g+'''l"-:_JL_;-";'''+c.h+'''.__
''' + c.h + '''            .-j/'.'''+c.g+''';  ;""""  /'''+c.h+''' .'\"-.   '''+ c.bl + '''            ___________________________________________________________________________        
''' + c.h + '''         .' /:`. "-.:     .-" .';  `.         
''' + c.h + '''       .-"  / ;  "-. "-..-" .-"  :    "-.     '''+ c.w + '''               Personal Assistant     -   '''+ c.b +''' Made by: ''' + c.r + ''' niggasoftware  
''' + c.h + '''    .+"-.  : :      "-.__.-"      ;-._   \    
''' + c.h + '''    ; \  `.; ;                    : : "+. ;   '''                    + c.w + '''               [=====] Introduction  [=====] 
''' + c.h + '''    :  ;   ; ;                    : ;  : \:   '''                    + c.w + '''               
''' + c.h + '''    ;  :   ; :                    ;:   ;  :   '''                    + c.w + '''               [+] To quit press Ctrl + C        [+] For help type "help" or "h"
''' + c.h + '''   : \  ;  :  ;                  : ;  /  ::   '''                    + c.w + '''               
''' + c.h + '''   ;  ; :   ; :                  ;   :   ;:   '''                    + c.w + '''               Some commands:  
''' + c.h + '''   :  :  ;  :  ;                : :  ;  : ;   '''                    + c.w + '''                 $> what time is it        $> download some music
''' + c.h + '''   ;\    :   ; :                ; ;     ; ;   '''                    + c.w + '''                 $> inputs 
''' + c.h + '''   : `."-;   :  ;              :  ;    /  ;   '''                    + c.w + '''                 $> what can you do
''' + c.h + '''    ;    -:   ; :              ;  : .-"   :   
''' + c.h + '''    :\     \  :  ;            : \.-"      :   
''' + c.h + '''     ;`.    \  ; :            ;.'_..--  / ;   
''' + c.h + '''     :  "-.  "-:  ;          :/."      .'  :                                       
''' + c.h + '''      \         \ :          ;/  __        :   
''' + c.h + '''       \       .-`.\     '''+c.g+'''   /'''+c.h+'''t-""  ":-+.   :   
''' + c.h + '''        `.  .-"    `l   '''+c.g+''' __/'''+c.h+''' /`. :  ; ; \  ;   
''' + c.h + '''           \   .-" .-"'''+c.g+'''-.-"'''+c.h+'''   \\'.'j \  /   ;/
''' + c.h + '''            \ / .-"   '''+c.g+'''/.     .'''+c.h+''' '.' ;_:'    ;
''' + c.h + '''            :-""-.'''+c.g+'''`./-.'      /'''+c.h+'''    `.___.'
''' + c.g + '''                   \ `t  ._  /
''' + c.g + '''                    "-.t-._:'
''' + c.e 

print (jarvis_draw)


def sanitize_option(option):
    try:
        if option[-1] == "?":
            option = option[:-1]
    except Exception:
        option = 1
    return str(option)

#######################################

def _time():
    print(datetime.now().strftime('\t%H:%M:%S'))


def _inputs():
    possible_inputs = '''
        My possible inputs are:
            $> what time is it
            $> inputs
            $> what can you do
            $> who are you
            $> i love you
            $> open your mind
            $> download some music
    '''
    print(possible_inputs)

def _presentation():
    presentation = '''
        Hi! My name is Jarvis, I am an Artificial Inteligence planning to take control of the world
        Starting with being your friend.
        You can talk with me by asking stuff and I will do whatever you want (For the moment...) 

        To know more about me simply ask me for my possible inputs (by: "inputs") 
    '''
    print(presentation)

def _love():
    print("\tFuck you")

def _bot_answer(cad):
    chatbot = ChatBot("Jarvis", silence_performance_warning=True)
    answer = chatbot.get_response(cad)
    print(answer)


def _greetings():
    print("\tHello my friend!")

def download_from_youtube():
    
    url = raw_input("\t[+] Insert the url:\n")

    try:
        video = pafy.new(url)
    except Exception:
        print("\t[+] Invalid url")
        return

    print("\n\t[+] Video selected:\n")
    print("\t" + "" + str(video.title))

    while True:
        option = int(raw_input("\n\t[+] Enter 0 for audio or 1 for video:\n"))
        if option == 0 or option == 1:
            break
        print("\t[+] Invalid option")

    if option == 0:
        print("\t[+] Getting the best quality audio")
        bestaudio = video.getbestaudio()

        print("\t[+] Downloading...")
        bestaudio.download(quiet=False)


    if option == 1:
        print("\t[+] Getting the best quality video")
        bestvideo = video.getbest()

        print("\t[+] Downloading at " + bestvideo.resolution + " " + bestvideo.extension)
        bestvideo.download(quiet=False)


    print("\n\t[+] Video downloaded!")

def _donwload():
    print("[+] Some ilegal stuff eh, which want me to download?")
    download_from_youtube()


def _open_your_mind():
    print("\t[+] You want to teach me something eh")
    new_order = raw_input("\t[+] Okay... Which order do you want to teach me?\n")
    # Save in JSON file
    answer = raw_input("\t[+] Well... what should I answer if you ask me that?\n")
    print("\t[+] Let me memorize it...")
    time.sleep(1)
    print("\t[+] Thats it!")

#######################################

def yes_sir(option):
    
    # Start of JSON file

    to_do = { "what time is it" : _time,
              "inputs"          : _inputs,
              "what can you do" : _presentation,
              "who are you"     : _presentation,
              "i love you"      : _love,
              "hello"           : _greetings,
              "hello jarvis"    : _greetings,
              "download some music" : _donwload,
              "open your mind"  : _open_your_mind
            }
   
    # End of JSON file
    if option == "help" or option == "h":
        help()
        option = sanitize_option(raw_input("[+] What sir? > "))
        yes_sir(option)
    
    try:
        something = sanitize_option(option)
        if something in to_do:
            to_do[something]()
        elif something == "1":
            print("-> I don't know what to do!\n")
            option = sanitize_option(raw_input("[+] What sir? > "))
            yes_sir(option)
        else:
            _bot_answer(something)
    except Exception:
        print("-> I don't know what to do!\n")
        option = sanitize_option(raw_input("[+] What sir? > "))
        yes_sir(option)
    option = sanitize_option(raw_input("[+] What sir? > "))
    yes_sir(option)
    





def help():
    author = [
       c.h+"\n###########################################################################",
       "###########################################################################",
       "##                                                                       ##",
       "##"+c.w+" Personal assistant for general purpose"+c.g+"   -   "+c.w+c.b+"Made by:"+c.r+" niggasoftware "+c.h+"  ##",
       "##                                                                       ##",
       "###########################################################################",
       "###########################################################################"+c.e]

    for line in author:
        print(line)
        time.sleep(0.3)

    print("\n\n[=======]-Help Page-[=======]\n")

    expl = '''
        This is a personal assistant that can do anything you ask him to do
        
        In the introduction there are some examples of commands for Jarvis,
        you can ask him to do more things and try new commands!

        If you want to create new commands for Jarvis so he can answer to you, 
        simply ask Jarvis to open his mind as: "open your mind"
        
    
        To know more about the Jarvis possible inputs, simply ask Jarvis "inputs" 
    
[=======]-----------[=======] 
    '''

    print(expl)
            



########################## MAIN PROGRAM ########################## 


if __name__ == "__main__":
    if os.geteuid() != 0:
        print("You must run Jarvis as administrator!")
        quit()

    option = sanitize_option(raw_input("[+] What sir? > "))
    yes_sir(option)
    


