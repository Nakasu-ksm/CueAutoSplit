import mutagen
from mutagen.id3 import APIC, ID3
import glob
from deflacue import deflacue
from mutagen.flac import FLAC, Picture
import os
import chardet

# CUE处理工具箱
bias = "pro_"
count = 0
for k in glob.glob("*"):
    try:
        if os.path.isdir(k):
            os.rename(k, bias + str(count))
            count += 1
    except:
        break

arr = []

for a in glob.glob("*"):
    if os.path.isdir(a):
        arr.append(a)

for k in arr:
    g = glob.glob(k + "/*")
    img = [x for x in g if any(x.endswith(e) for e in ['.png', '.bmp', '.jpg'])]
    cue = list(filter(lambda x: ".cue" in x or ".cue" in x, g))
    music = [x for x in g if any(x.endswith(e) for e in ['.ape', '.tak', '.wav'])]

    for c in cue:
        cuen = os.getcwd() + '\\' + c
        m = magic.Magic(mime_encoding=True)
        encoding = m.from_file(c)
        with open(cuen, 'rb') as f:
            data = f.read()
            encoding = chardet.detect(data)['encoding']

        try:
            process = deflacue.Deflacue(source_path=cuen, encoding=encoding)
            process.process_cue(cue_file=cuen, target_path=k, delete=True, music=music, img=img, needImage=True)
        except:
            print("分割错误：文件来源-" + c)

    # if len(img) == 0:
    #     continue
    # for audiopath in g:
    #     if audiopath.split("\\")[-1].split(".")[-1] != "flac":
    #         continue
    #     audio = FLAC(audiopath)
    #     with open(img[0],'rb') as image:
    #         picture = Picture()
    #         picture.data = image.read()
    #         picture.type = 3
    #         picture.mime = "image/jpeg"
    #         audio.add_picture(picture)
    #     audio.save()
