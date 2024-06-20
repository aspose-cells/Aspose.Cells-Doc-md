---
title: Süzgeci Güncelleme
type: docs
weight: 60
url: /tr/python-java/updating-slicer/
---

## **Dilimleyici Güncelleme**
Aspose.Cells for Python via Java, dilimleyicilerin güncellenmesini destekler. Bunun için, API, Slicer.SlicerCache.SlicerCacheItems özelliğini sağlar, bu özellik dilimleyici öğelerini seçmek veya seçmemek için kullanılır. Aşağıdaki kod parçası, bir dilimleyici içeren [örnek Excel dosyasını](106365050.xlsx) yükler. Dilimleyicinin 2. ve 3. öğelerini seçmez ve Slicer.refresh() yöntemi kullanarak dilimleyiciyi yeniler. Daha sonra çalışma kitabını [çıktı Excel dosyası olarak](106365051.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini gösterir. Ekran görüntüsünde, seçili öğelerle dilimleyiciyi yenilemenin, pivot tabloyu da ona göre yenilediğini görebilirsiniz.

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
