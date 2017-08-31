import shutil
import youtube_dl
import urllib
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                           video=raw_input('Enter video url:')
ydl.download([video])
source_file='C:\Users\Donna\Desktop\Python'
dest_folder='C:\Users\Donna\Desktop'
shutil.move(source_file,dest_folder)
print 'Check desktop for the file created'
