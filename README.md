# Chimege TTS

Энэхүү репо нь текстийг яриа болгон хөрвүүлэх F5-TTS моделийг Монгол хэлэнд тохируулахыг оролдсон туршилт юм. Ингэхдээ `MBSpeech-1.0` өгөгдлийг ашигласан бөгөөд монгол текст -ийг хэрвээ сургалтад ашигласан аудиог reference болгож өгсөн тохиолдолд яриа болгон унших чадвартай. Текстийг яриа болгосон туршилтуудийн үр дүнг `demo` хавтаст оруулсан болно.

## 0. Орчин бэлтгэх

Эхлээд энэхүү репог хуулах хэрэгтэй.

```
git clone https://github.com/MendeBadra/chimege_tts.git
cd chimege_tts
```


Орчин бэлдэхдээ `uv` ашиглах хэрэгтэй. Хэрэв `uv` суулгаагүй бол [энд дар](https://docs.astral.sh/uv/getting-started/installation/)

```
uv sync
```



## 1. Өгөгдөл бэлтгэх

Өгөгдлийг tugstugi/mongolian-nlp дээр дурдагдсан Монгол Библийн аудио буюу MBSpeech-1.0 -ийг ашигласан. Уг өгөгдлийг бэлтгэхэд [mongolian_nlp](https://github.com/tugstugi/mongolian-nlp?tab=readme-ov-file#:~:text=dl_and_preprop_dataset.py%20to) GitHub репо дээрх зааврын дагуу `dl_and_preprop_dataset.py` -ийг ашиглан татах гэсэн боловч линк ажиллахгүй байсан.

Тиймээс `download_mbspeech.py` нэмэлт python script ашиглан татсан бөгөөд линкийг нь `davarbibles.org` -оос шинэчлэн татах боломжтой болсон боловч, библийн номууд (Genesis, Exodus г.м) -ыг тус тусад нь татаж болохгүй тул бүтэн библээр нь татаж зөвхөн эхний гурван номыг салгаж авсан. Энэхүү script -ийн үр дүнд `01_Genesis.zip` гэх мэтчилэн zip файлууд гарч ирэх ёстой.


## 2. Шаардлагатай репонуудийг хуулах

Git ашиглан `SWivid/F5-TTS` болон `tugstugi/pytorch-dc-tts` репонуудийг хуулах хэрэгтэй.

`F5-TTS` -ийг хуулах:
```
git clone https://github.com/MendeBadra/F5-TTS.git

```

Мөн `pytorch-dc-tts` -ийг хуулах:
```
git clone https://github.com/tugstugi/pytorch-dc-tts.git
```


Үүний дараа өмнөх алхмын бэлтгэсэн `.zip` файлуудийг `pytorch-dc-tss/datasets` хавтасд хуулах хэрэгтэй.
Ингэснээр `dl_and_prop_dataset.py` -ийг ажиллуулах боломжтой болох юм.

```
python pytorch-dc-tts/dl_and_preprop_dataset.py --dataset mbspeech
```

Үр дүнд нь `pytorch-dc-tss/datasets` -ийн хавтасд `MBSpeech-1.0` гэсэн хавтас үүссэн байх ёстой. 
Уг хавтасийг үндсэн репогийн `chimege_tts/data` -д хадгалах хэрэгтэй.


## 3. F5-TTS fine-tuning

Fine tune буюу тохируулахад `ffmpeg` програм суулгасан байх шаардлагатай. Мөн өмнөх алхамд бэлтгэсэн өгөгдлийг бэлтгэх кодийг ажиллуулах хэрэгтэй юм.

```
cd F5-TTS
python src/f5_tts/train/datasets/prepare_ljspeech.py 
```

Ингэж өгөгдөл бэлтгэсний дараа fine tune хийхдээ:

```
python src/f5_tts/train/finetune_gradio.py 
``` 
коммандийг ажиллуулж веб орчинд finetune хийсэн. Зааврыг дараах [линкээс](https://github.com/SWivid/F5-TTS/discussions/143) үзэх боломжтой.

Сургалтын параметрүүд:

![Зураг](<settings.png>)







