---
title: Çalışma sayfası içindeki Şekil Önüne veya Arkasına Gönderme
type: docs
weight: 3400
url: /tr/net/send-shape-front-or-back-inside-the-worksheet/
---

## **Olası Kullanım Senaryoları**

Aynı konumda birden fazla şekil bulunduğunda, bu şekillerin görünür olup olmayacakları, z-sıra konumları tarafından belirlenir. Aspose.Cells, şeklin z-sıra konumunu değiştiren [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback) yöntemini sunar. Şekli arkaya göndermek istiyorsanız -1, -2, -3 gibi negatif bir sayı kullanacak ve şekli öne göndermek istiyorsanız 1, 2, 3 gibi pozitif bir sayı kullanacaksınız.

## **Çalışma Sayfası İçinde Şekil Önüne veya Arkasına Gönderme**

Aşağıdaki örnek kod, [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback) yönteminin kullanımını açıklar. Kod içinde kullanılan [örnek Excel dosyası](50528330.xlsx) ve kod tarafından oluşturulan [çıktı Excel dosyası](50528331.xlsx)'nın etkisini gösteren ekran görüntüsünü göstermektedir.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-SendShapeFrontOrBackInWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
