import pytube
import os
import subprocess


address = input(" 다운 및 변환 할 유튜브 동영상 주소를 압력해주세요: ")
yt = pytube.YouTube(address) # 다운 받을 동영상 URL 지정
videos = yt.streams.all()

#print('videos',videos)
for i in range(len(videos)) :
    print(i,',',videos[i])#화질 리스트 출력


cNum = int(input(" 다운 받을 화질을 입력해주세요 :"))

down_dir = "C:\youtube"

videos[cNum].download(down_dir)
newFileName = input(" 변환 할 mp3 파일명을 입력해주세요: ")
oriFileName= videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
 os.path.join(down_dir, oriFileName),
 os.path.join(down_dir, newFileName)
])
print("동영상 다운로드 및 mp3 변환 완료")
