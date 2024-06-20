---
title: Süzgeci Güncelleme
type: docs
weight: 50
url: /tr/net/updating-slicer/
description: Bu makale, süzgeci Aspose.Cells for .NET API ile güncelleyerek bağlantılı özet tabloları nasıl güncelleyeceğinizi göstermektedir.
keywords: Aspose.Cells C# Süzgeç güncelleme, C# süzgeci nasıl değiştirilir, C# de süzgeci ayarlama, C# de süzgeci seçme veya seçmeme.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel'de süzgeci güncellemek, öğelerini seçmek veya seçmemek istiyorsanız, Ardından Aspose.Cells ile süzgeç öğelerini seçmek veya seçmemek için [**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems) kullanın ve ardından süzgeç tablosunu veya özet tabloyu güncellemek için [**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh) yöntemini çağırın.

## **Süzgeci Nasıl Güncellenir**

Aşağıdaki örnek kod, mevcut bir süzgeç içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Süzgecin 2. ve 3. öğelerini seçmez ve süzgeci yeniler. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Ekran görüntüsünde, örnek kodun örnek Excel dosyasındaki etkisini görebilirsiniz. Ekran görüntüsünde, seçili öğelerle süzgeci yenilemenin aynı zamanda özet tabloyu da yenilediğini görebilirsiniz.

![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
