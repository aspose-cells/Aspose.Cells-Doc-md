---
title: Çalışma Sayfası İçindeki Şekil ile Metni Döndürme
type: docs
weight: 110
url: /tr/java/rotate-text-with-shape-inside-the-worksheet/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel kullanarak herhangi bir şekil içine metin ekleyebilirsiniz. Eğer çok eski Microsoft Excel 2003 kullanarak şekil eklerseniz, o zaman metin şekille birlikte dönmeyecektir. Ancak daha yeni sürümlerini kullanarak şekil eklerseniz, örneğin 2007, 2010, 2013 veya 2016, vb. o zaman metin şekille birlikte döner. Metnin şekille birlikte dönüp dönmemesi kontrol edilebilir. Varsayılan değeri **true** olup metin şekille birlikte döner ancak **false** olarak ayarlarsanız, metin şekille birlikte dönmeyecektir.

## **Çalışma Sayfası İçindeki Şekil ile Metni Döndürme**

Aşağıdaki örnek kod, metni şekille birlikte dönen üçgen şekilli bir örnek Excel dosyasını yükler. Örnek Excel dosyasını Microsoft Excel'de açarsanız ve üçgen şeklini döndürürseniz, metin de onunla birlikte döner. Kod daha sonra **false** olarak `TextDirection` özelliğini ayarlar ve bunu [çıktı Excel dosyası](64716917.xlsx) olarak kaydeder. Şimdi çıktı Excel dosyasını Microsoft Excel'de açarsanız ve üçgen şeklini döndürürseniz, metin onunla birlikte dönmeyecektir. Bu, kodun örnek Excel dosyası üzerindeki etkisini gösteren bir ekran görüntüsü için lütfen aşağıdaki ekran görüntüsüne bakınız.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
