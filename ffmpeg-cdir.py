#!/usr/bin/env python3
import os,shutil,sys
import telegram             # require python-telegram-bot module

def ffmpeg_encoding():
    myToken = <token>
    myChatId = <ChatId>
    if not os.path.isdir('encoded'):
        os.mkdir('encoded')

    for cdir in os.listdir():
        extension = os.path.splitext(cdir)[1]
        if extension in ('.mkv','.mp4','.avi'):
            os.system('ffmpeg -i "{0}" -c:v libx264 -vf format=yuv420p -c:a copy "encoded/{0}"'.format(cdir))
        elif extension in ('.smi','.ass','.srt'):
            shutil.copy(cdir,'encoded')
    bot = telegram.Bot(token = myToken)
    message = os.getcwd().split(os.path.sep)[-1] + " encoding complete!"
    bot.sendMessage(chat_id = myChatId,text = message)

if len(sys.argv) > 1 and sys.argv[1] == '-a':
    for fdir in os.listdir():
        if os.path.isdir(fdir):
            os.chdir(fdir)
            ffmpeg_encoding()
            os.chdir('..')
else:
    ffmpeg_encoding()
