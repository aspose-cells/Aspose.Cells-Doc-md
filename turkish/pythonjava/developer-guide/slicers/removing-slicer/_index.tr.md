---
title: Dilimleyici Kaldırma
type: docs
weight: 40
url: /tr/python-java/removing-slicer/
---

## **Süzgeci Kaldırma**
Microsoft Excel'de bir dilimleyiciyi kaldırmak için dilimleyiciyi seçip *Sil* düğmesine basmanız yeterlidir. Aspose.Cells for Python via Java kullanarak bunu yapmak için Worksheet.getSlicers().remove() yöntemini kullanın. Bu, çalışma sayfasından dilimleyiciyi kaldıracaktır. 

Aşağıdaki kod parçası, mevcut bir dilimleyici içeren [örnek Excel dosyasını](106364970.xlsx) yükler. Dilimleyiciye erişir, onu kaldırır ve [çıktı Excel dosyası](106364971.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, kaldırılacak dilimleyiciyi gösterir.

![todo:image_alt_text](Removing-Slicer-using-Aspose.Cells.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-RemovingSlicer.py" >}}
