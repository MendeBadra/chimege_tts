# Chimege TTS

Энэхүү репо нь текстийг яриа болгон хөрвүүлэх F5-TTS моделийг Монгол хэлэнд тохируулсан туршилт юм.

## 0. Орчин бэлтгэх

Та 

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

## 3. F5-TTS мод



