#  EX1
from youtube_dl import YoutubeDL
#1: Tải 1 video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=i1IKnWDecwA']) 

#2: Tải 1 audio
options = {'format': 'bestaudio/audio'}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=z5Jc7KiTLbs'])

#3: Tìm và tải video
options = {
    'default_search': 'ytsearch', 'max_downloads': 1 }
dl = YoutubeDL(options)
dl.download(['Có tất cả nhưng thiếu anh'])

#4: Tìm và tải audio
options = {'default_search': 'ytsearch','max_downloads': 1,'format': 'bestaudio/audio'}
dl = YoutubeDL(options)
dl.download(['Đi đu đưa đi'])
