---
title: Golang ve C++ ile Pivot Bağlantısı Ekle
linktitle: Pivot Bağlantısı Ekleme
type: docs
weight: 30
url: /tr/go-cpp/add-pivot-connection/
description: Aspose.Cells kütüphanesini kullanarak pivot bağlantısı eklemeyi öğrenin.
keywords: Ofis 2013, Ofis 2016, Ofis 2019 ve Ofis 365 olmadan pivot bağlantısı ekleme.
---

## **Olası Kullanım Senaryoları**

Excel'de dilimleyici ve pivot tabloyu ilişkilendirmek istiyorsanız, dilimleyiciye sağ tıklayarak "Rapor Bağlantıları..." öğesini seçmeniz gerekmektedir. Seçenek listesinde onay kutusunda işlem yapabilirsiniz. Benzer şekilde, Aspose.Cells API'sını kullanarak dilimleyici ve pivot tablo ilişkilendirmek istiyorsanız, [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/addpivotconnection/) yöntemini kullanmalısınız. Bu, dilimleyici ve pivot tabloyu ilişkilendirecektir.

## **Dilimleyiciyi ve Pivot Tablosunu İlişkilendir**

Aşağıdaki örnek kod önceden var olan bir dilimleyici içeren [örnek Excel dosyasını](add-pivot-connection.xlsx) yükler. Slicer'a erişir ve sonra Slicer'ı ve PivotTabloyu ilişkilendirir. Son olarak, çalışma kitabını [çıkış Excel dosyası](add-pivot-connection-out.xlsx) olarak kaydeder. 

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPivotConnection.go" >}}
