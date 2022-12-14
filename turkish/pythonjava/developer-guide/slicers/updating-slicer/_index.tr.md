---
title: Dilimleyici güncelleniyor
type: docs
weight: 60
url: /tr/python-java/updating-slicer/
---
## **Dilimleyici güncelleniyor**
Java aracılığıyla Python için Aspose.Cells, dilimleyicilerin güncellenmesini destekler. Bunun için API, dilimleyici öğelerini seçmek veya seçimini kaldırmak için kullanılan Slicer.SlicerCache.SlicerCacheItems özelliğini sağlar. Aşağıdaki kod parçacığı,[örnek excel dosyası](106365050.xlsx)bir dilimleyici içerir. Dilimleyicinin 2. ve 3. öğelerinin seçimini kaldırır ve Slicer.refresh() yöntemini kullanarak dilimleyiciyi yeniler. Daha sonra çalışma kitabını şu şekilde kaydeder:[çıktı excel dosyası](106365051.xlsx). Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini gösterir. Ekran görüntüsünde görebileceğiniz gibi, dilimleyiciyi seçili öğelerle yenilemek, pivot tabloyu da buna göre yeniledi.

![yapılacaklar:resim_alternatif_Metin](Updating-Slicer-using-Aspose.Cells.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
