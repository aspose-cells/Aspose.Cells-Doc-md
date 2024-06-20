---
title: Dilimleyici Kaldırma
type: docs
weight: 30
url: /tr/java/removing-slicer/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel'de slicer'ı kaldırmak istiyorsanız, onu seçip *Sil* düğmesini basmanız yeterlidir. Benzer şekilde, Aspose.Cells API'sini kullanarak kaldırmak istiyorsanız, lütfen [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove\(com.aspose.cells.Slicer\)) yöntemini kullanın. Bu, slicer'ı çalışma sayfasından kaldıracaktır. 
## **Süzgeci Kaldırma**
Aşağıdaki örnek kod, mevcut bir slicer içeren [örnek Excel dosyasını](67338504.xlsx) yükler. Slicer'lara erişir ve sonra onu kaldırır. Son olarak, çalışma kitabını [çıkış Excel dosyası](67338502.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun çalıştırılmasından sonra kaldırılacak olan slicer'ı gösteriyor.

![todo:image_alt_text](removing-slicer_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
