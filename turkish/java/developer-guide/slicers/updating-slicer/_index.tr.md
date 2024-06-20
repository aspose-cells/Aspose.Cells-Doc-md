---
title: Süzgeci Güncelleme
type: docs
weight: 50
url: /tr/java/updating-slicer/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel'de dilimleyiciyi güncellemek istiyorsanız, öğelerini seçin veya bırakın, ardından Aspose.Cells ile dilimleyici öğelerini seçmek veya bırakmak için [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems) kullanın ve ardından dilimleyici tablosunu veya özet tabloyu güncellemek için [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh\(\)) yöntemini çağırın. 
## **Dilimleyici Güncelleme**
Aşağıdaki örnek kod, mevcut bir dilimleyici içeren [örnek Excel dosyasını](67338506.xlsx) yükler. Dilimleyicinin 2. ve 3. öğelerini seçmez ve dilimleyiciyi günceller. Daha sonra çalışma kitabını [çıkış Excel dosyası](67338505.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde, seçili öğelerle dilimleyiciyi yenilemenin özet tabloyu da uygun bir şekilde güncellediğini görebilirsiniz.

![todo:image_alt_text](updating-slicer_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
