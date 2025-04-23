---
title: Pivot Bağlantısı Ekleme
type: docs
weight: 30
url: /tr/net/add-pivot-connection/
description: Aspose.Cells kütüphanesi ile pivot bağlantısı nasıl ekleneceğini öğrenin.
keywords: Ofis 2013, Ofis 2016, Ofis 2019 ve Ofis 365 olmadan pivot bağlantısı ekleme.
---

## **Olası Kullanım Senaryoları**

Excel'de dilimleyici ve pivot tabloyu ilişkilendirmek istiyorsanız, dilimleyiciye sağ tıklayarak "Rapor Bağlantıları..." öğesini seçmeniz gerekmektedir. Seçenek listesinde onay kutusunda işlem yapabilirsiniz. Benzer şekilde, Aspose.Cells API'sını kullanarak dilimleyici ve pivot tablo ilişkilendirmek istiyorsanız, [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/addpivotconnection/) yöntemini kullanmalısınız. Bu, dilimleyici ve pivot tabloyu ilişkilendirecektir.

## **Dilimleyiciyi ve Pivot Tablosunu İlişkilendir**

Aşağıdaki örnek kod önceden var olan bir dilimleyici içeren [örnek Excel dosyasını](add-pivot-connection.xlsx) yükler. Slicer'a erişir ve sonra Slicer'ı ve PivotTabloyu ilişkilendirir. Son olarak, çalışma kitabını [çıkış Excel dosyası](add-pivot-connection-out.xlsx) olarak kaydeder. 


## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Adding-Pivot-Connection.cs" >}}
{{< app/cells/assistant language="csharp" >}}
