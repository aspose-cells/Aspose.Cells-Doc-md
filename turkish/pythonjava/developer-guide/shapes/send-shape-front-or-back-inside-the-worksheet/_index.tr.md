---
title: Şekilleri ön veya arka plana getir
type: docs
weight: 3400
url: /tr/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **Olası Kullanım Senaryoları**

Aynı konumda birden fazla şekil bulunduğunda, bu şekillerin görünür olup olmayacakları, z-sıra konumları tarafından belirlenir. Aspose.Cells, şeklin z-sıra konumunu değiştiren [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) yöntemini sunar. Şekli arkaya göndermek istiyorsanız -1, -2, -3 gibi negatif bir sayı kullanacak ve şekli öne göndermek istiyorsanız 1, 2, 3 gibi pozitif bir sayı kullanacaksınız.

## **Şekli Çalışma Sayfasının İçinde Öne veya Arkaya Getirin**

Aşağıdaki örnek kod, [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) metodunun kullanımını açıklar. Lütfen kodda kullanılan [örnek Excel dosyasını](sampleToFrontOrBack.xlsx) ve bunun tarafından oluşturulan [çıktı Excel dosyasını](50528331.xlsx) gözden geçirin. Ekran görüntüsü, kodun örnek Excel dosyası üzerindeki etkisini gösterir.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}
