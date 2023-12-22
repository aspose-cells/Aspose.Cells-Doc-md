---
title: Dilimleyici Güncelleniyor
type: docs
weight: 50
url: /tr/net/updating-slicer/
description: Bu makalede, dilimleyiciyi Aspose.Cells for .NET API ile güncelleyerek bağlantılı pivot tabloların nasıl güncelleneceği gösterilmektedir.
keywords: Aspose.Cells C# Update slicer, C# how to change the slicer, how to adjust the slicer in C#, how to select or unselect he slicer items.
---
##  **Olası Kullanım Senaryoları**

Microsoft Excel'de dilimleyiciyi güncellemek istiyorsanız öğelerini seçin veya seçimini kaldırın, ardından dilimleyici tablosunu veya pivot tabloyu buna göre güncelleyecektir. Lütfen kullan[**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)Aspose.Cells ile dilimleyici öğelerini seçmek veya seçimini kaldırmak ve ardından aramak için[**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)dilimleyici tablosunu veya pivot tabloyu güncelleme yöntemi.

##  **Dilimleyici Nasıl Güncellenir**

 Aşağıdaki örnek kod,[örnek Excel dosyası](67338475.xlsx) mevcut bir dilimleyiciyi içerir. Dilimleyicinin 2. ve 3. öğelerinin seçimini kaldırır ve dilimleyiciyi yeniler. Daha sonra çalışma kitabını şu şekilde kaydeder:[Excel dosyasının çıktısı](67338476.xlsx)Aşağıdaki ekran görüntüsü örnek kodun örnek Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde görebileceğiniz gibi, dilimleyicinin seçilen öğelerle yenilenmesi pivot tablonun da buna uygun şekilde yenilenmesini sağlamıştır.

![yapılacak şey:image_alt_text](updating-slicer_1.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
