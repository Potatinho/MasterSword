import os
from cryptography.fernet import Fernet

print("\033[36m __  __         _           _  __\n"
      "|  \/  |__ _ __| |_ ___ _ _| |/ /___ _  _ \n"
      "| |\/| / _` (_-<  _/ -_) '_| ' </ -_) || |\n"
      "|_|  |_\__,_/__/\__\___|_| |_|\_\___|\_, |\n"
      "-9.9.7                                |__/\n")

currentPath = os.path.dirname(__file__)
a = True
while a == True:
    files = []
    comando = input("\033[31m[+]Command:")
    comandoL = comando.split()
    try:
        #Sem Chave
        if "/ulck" == comandoL[0]:
            try:
                if comandoL[1] == "-d":
                    for file in os.listdir():
                        if file == "MasterSword.py" or file == "chave.key":
                            continue
                        if os.path.isfile(file):
                            files.append(file)
                else:
                    for file in os.listdir(comandoL[1]):
                        if file == "MasterSword.py" or file == "chave.key":
                            continue
                        if os.path.isfile(comandoL[1]+"\\"+file):
                            files.append(file)

                try:
                    try:
                        if comandoL[2] == "-kpath":
                            with open(comandoL[3]+"\\"+"chave.key", "rb") as chave:
                                chave_segredo = chave.read()
                                if chave_segredo == "":
                                    print("[-]No Key")
                    except:
                        with open("chave.key", "rb") as chave:
                            chave_segredo = chave.read()
                            if chave_segredo == "":
                                print("[-]No Key")
                    senha = "1,618033988749"
                    login = input("[+]Pass:")

                    if login == senha:
                        try:
                            for file in files:
                                with open(comandoL[1]+"\\"+file, "rb") as arquivos:
                                    dentro = arquivos.read()
                                dentro_nao_segredo = Fernet(chave_segredo).decrypt(dentro)
                                with open(comandoL[1]+"\\"+file, "wb") as arquivos:
                                    arquivos.write(dentro_nao_segredo)
                            print("[-]Decrypt Succesfull")
                        except:
                            print("[-]Decrypt Succesfull")
                    else:
                        print("[-]Wrong Login")
                except:
                    print("[-]No key")
            except:
                print("[-]Error on decrypt")
        elif "/lck" == comandoL[0]:
            try:
                if comandoL[1] == "-d":
                    for file in os.listdir():
                        if file == "MasterSword.py" or file == "chave.key" or file == "desktop.ini":
                            continue
                        if os.path.isfile(file):
                            files.append(file)

                    key = Fernet.generate_key()
                    try:
                        with open("chave.key", "wb") as chaveF:
                            chaveF.write(key)
                    except:
                        print("[-]Error on key creation")
                    try:
                        for file in files:
                            with open(file, "rb") as arquivos:
                                dentro = arquivos.read()
                            dentro_segredo = Fernet(key).encrypt(dentro)
                            with open(file, "wb") as arquivos:
                                arquivos.write(dentro_segredo)

                        print("[-]Encrypt Succesfull")
                    except:
                        print("[-]Error on Encrypt")
                else:
                    for file in os.listdir(comandoL[1]):
                        if file == "MasterSword.py" or file == "chave.key" or file == "desktop.ini":
                            continue
                        if os.path.isfile(comandoL[1]+"\\"+file):
                            files.append(file)

                    key = Fernet.generate_key()
                    try:
                        try:
                            if comandoL[2] == "-kpath":
                                with open(comandoL[3]+"\\"+"chave.key", "wb") as chaveF:
                                    chaveF.write(key)
                        except:
                            with open("chave.key", "wb") as chaveF:
                                chaveF.write(key)
                    except:
                        print("[-]Error on key creation")
                    try:
                        for file in files:
                            with open(comandoL[1]+"\\"+file, "rb") as arquivos:
                                dentro = arquivos.read()
                            dentro_segredo = Fernet(key).encrypt(dentro)
                            with open(comandoL[1]+"\\"+file, "wb") as arquivos:
                                arquivos.write(dentro_segredo)

                        print("[-]Encrypt Succesfull")
                    except:
                        print("[-]Error on Encrypt")
            except:
                print("[-]Error on file select")
        #Others
        elif "/fldr" == comandoL[0]:
            try:
                folders = []
                foldersF = []
                if comandoL[1] == "-d":
                    for folder in os.listdir():
                        folders.append(folder)
                        if os.path.isdir(folder):
                            foldersF.append(folder)

                    print(f"[-]Folders in DEFAULT:")
                    for pastaP in foldersF:
                        print(f"\033[32m {pastaP}")
                else:
                    for folder in os.listdir(comandoL[1]):
                        folders.append(comandoL[1]+"\\"+folder)
                        if os.path.isdir(comandoL[1]+"\\"+folder):
                            foldersF.append(folder)

                    print(f"[-]Folders in {comandoL[1]}:")
                    for pastaP in foldersF:
                        print(f"\033[32m {pastaP}")
            except:
                print(f"[-]No directory called: {comandoL[1]}")
        elif "/file" == comandoL[0]:
            try:
                if comandoL[1] == "-d":
                    for file in os.listdir():
                        if os.path.isfile(file):
                            files.append(file)

                    print(f"[-]Files in DEFAULT")
                    for filesP in files:
                        print(f"\033[32m {filesP}")
                else:
                    for file in os.listdir(comandoL[1]):
                        if os.path.isfile(comandoL[1]+"\\"+file):
                            files.append(file)

                    print(f"[-]Files in {comandoL[1]}")
                    for filesP in files:
                        print(f"\033[32m {filesP}")
            except:
                print(f'[-]No directory called {comandoL[1]}')
        elif "/help" == comandoL[0]:
            print()
            print("\033[30mHelp command for to help you to use commands\n\n"
                  "\033[34mCommands:\n"
                  "\033[31m /lck                           \033[30mEncrypt command, default parameters(empty) create a new file for the key on the CWD\n"
                  "\033[31m /ulck                          \033[30mDecrypt command, default parameters(empty) read the key.key file on the CWD\n"
                  "\033[31m /fldr                          \033[30mPrint all folders in a directory\n"
                  "\033[31m /file                          \033[30mPrint all files in a directory\n"
                  "\033[31m /help                          \033[30mPrint this list\n\n"
                  "\033[34mParameters:\n"
                  "\033[31m -d                             \033[30mDefault parameter\n"
                  "\033[31m -key                           \033[30mUsed after directory in /ulck and /lck Choose your own key, word to Fernet key\n"
                  "\033[31m -kpath                         \033[30mChoose the key.key file path works with /ulck and /lck")
            print()
        #Com Chave
        try:
            if "/ulck" == comandoL[0] and "-key" == comandoL[2]:
                try:
                    if comandoL[1] == "-d":
                        for file in os.listdir():
                            if file == "MasterSword.exe" or file == "chave.key":
                                continue
                            if os.path.isfile(file):
                                files.append(file)
                    else:
                        for file in os.listdir(comandoL[1]):
                            if file == "MasterSword.exe" or file == "chave.key":
                                continue
                            if os.path.isfile(comandoL[1]+"\\"+file):
                                files.append(comandoL[1]+"\\"+file)

                    senha = "1,618033988749"
                    login = input("[+]Pass:")

                    bkey = b'sgn8iYm49l5CXq8xi-H9mhN6O4dFXw2VAqZla6rreDU='
                    key = comandoL[3]
                    Fernet(bkey).encrypt(b'key')

                    if login == senha:
                        chave_segredo = key
                        try:
                            for file in files:
                                with open(comandoL[1]+"\\"+file, "rb") as arquivos:
                                    dentro = arquivos.read()
                                dentro_nao_segredo = Fernet(chave_segredo).decrypt(dentro)
                                with open(comandoL[1]+"\\"+file, "wb") as arquivos:
                                    arquivos.write(dentro_nao_segredo)
                            print("[-]Decrypt Succesfull")
                        except:
                            print("[-]Error on decrypt")
                    else:
                        print("[-]Wrong Login")
                except:
                    print("[-]Error on file select")
            elif "/lck" == comandoL[0] and "-key" == comandoL[2]:
                try:
                    if comandoL[1] == "-d":
                        for file in os.listdir():
                            if file == "MasterSword.py" or file == "chave.key":
                                continue
                            if os.path.isfile(file):
                                files.append(file)
                    else:
                        for file in os.listdir(comandoL[1]):
                            if file == "MasterSword.py" or file == "chave.key":
                                continue
                            if os.path.isfile(comandoL[1]+"\\"+file):
                                files.append(comandoL[1]+"\\"+file)

                    bkey = b'sgn8iYm49l5CXq8xi-H9mhN6O4dFXw2VAqZla6rreDU='
                    key = comandoL[3]
                    Fernet(bkey).encrypt(b'key')

                    try:
                        for file in files:
                            with open(comandoL[1]+"\\"+file, "rb") as arquivos:
                                dentro = arquivos.read()
                            dentro_segredo = Fernet(key).encrypt(dentro)
                            with open(comandoL[1]+"\\"+file, "wb") as arquivos:
                                arquivos.write(dentro_segredo)
                        print("[-]Encrypt Succesfull")
                    except:
                        print("[-]Error on Encrypt")
                except:
                    print("[-]Error on file select")
        except:
            print()
    except:
        print(f"[-]No command called: {comando}")
    if "quit" == comandoL[0]:
        a = False