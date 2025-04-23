---
title: Çalışma sayfası içindeki Şekil Önüne veya Arkasına Gönderme
type: docs
weight: 3400
url: /tr/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **Olası Kullanım Senaryoları**

Aynı konumda birden fazla şekil bulunduğunda, nasıl görünecekleri z-sıralama pozisyonlarına göre belirlenir. Aspose.Cells for Python via .NET, şeklin z-sıralama pozisyonunu değiştiren [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) metodunu sağlar. Bir şekli arka plana göndermek için negatif sayı like -1, -2, -3 kullanırsınız. Ön plana göndermek için ise pozitif sayı like 1, 2, 3 kullanılır.

## **Çalışma Sayfası İçinde Şekil Önüne veya Arkasına Gönderme**

Aşağıdaki örnek kod, [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) yönteminin kullanımını açıklar. Kod içinde kullanılan [örnek Excel dosyası](50528330.xlsx) ve kod tarafından oluşturulan [çıktı Excel dosyası](50528331.xlsx)'nın etkisini gösteren ekran görüntüsünü göstermektedir.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
