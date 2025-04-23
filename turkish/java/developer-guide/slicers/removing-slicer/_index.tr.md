---
title: Dilimleyici Kaldırma
type: docs
weight: 30
url: /tr/java/removing-slicer/
---

## **Olası Kullanım Senaryoları**
Eğer Microsoft Excel'de dilimleyiciyi kaldırmak istiyorsanız, onu seçin ve *Delete* tuşuna basın. Benzer şekilde, Aspose.Cells API kullanarak programlı olarak kaldırmak için, lütfen [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove-com.aspose.cells.Slicer-) yöntemini kullanın. Bu, dilimleyiciyi çalışma sayfasından kaldıracaktır. 
## **Süzgeci Kaldırma**
Aşağıdaki örnek kod, mevcut bir slicer içeren [örnek Excel dosyasını](67338504.xlsx) yükler. Slicer'lara erişir ve sonra onu kaldırır. Son olarak, çalışma kitabını [çıkış Excel dosyası](67338502.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun çalıştırılmasından sonra kaldırılacak olan slicer'ı gösteriyor.

![todo:image_alt_text](removing-slicer_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
