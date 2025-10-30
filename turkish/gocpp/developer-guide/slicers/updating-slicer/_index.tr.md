---
title: C++ ile Golang kullanarak Dilimleyici Güncelleme
linktitle: Süzgeci Güncelleme
type: docs
weight: 50
url: /tr/go-cpp/updating-slicer/
description: Bu makale, Aspose.Cells for C++ API sini kullanarak dilimleyici güncelleyerek bağlı pivot tablolarını nasıl güncelleyeceğinizi gösterir.
keywords: Aspose.Cells C++ kullanarak dilimleyiciyi güncelleyin, C++ dilimleyiciyi nasıl değiştirilir, C++ kullanarak dilimleyiciyi nasıl ayarlarsınız, dilimleyici öğelerini seçip kaldırmak nasıl yapılır.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel'de bir dilimleyiciyi güncellemek istiyorsanız, öğelerini seçin veya kaldırın, ardından dilimleyici tablosunu veya pivot tablosunu buna göre günceller. Lütfen Aspose.Cells ile dilimleyici öğelerini seçip kaldırmak için [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/go-cpp/slicercache/getslicercacheitems/) kullanın ve ardından [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) yöntemini çağırarak dilimleyici tablosunu veya pivot tablosunu güncelleyin.

## **Süzgeci Nasıl Güncellenir**

Aşağıdaki örnek kod, mevcut bir süzgeç içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Süzgecin 2. ve 3. öğelerini seçmez ve süzgeci yeniler. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Ekran görüntüsünde, örnek kodun örnek Excel dosyasındaki etkisini görebilirsiniz. Ekran görüntüsünde, seçili öğelerle süzgeci yenilemenin aynı zamanda özet tabloyu da yenilediğini görebilirsiniz.

![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdatingSlicer.go" >}}
