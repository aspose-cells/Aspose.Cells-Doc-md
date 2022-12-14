---
title: Pivot Bağlantısını Kaldır
type: docs
weight: 30
url: /tr/java/remove-pivot-connection/
description: Aspose.Cells Java kitaplığı ile pivot bağlantısını nasıl kaldıracağınızı öğrenin.
keywords: Remove pivot connection without office 2013, office 2016, office 2019 and office 365.
---
## **Olası Kullanım Senaryoları**

Excel'de dilimleyici ve pivot tablo ilişkisini kesmek istiyorsanız, dilimleyiciye sağ tıklayıp "Bağlantıları Raporla..." öğesini seçmeniz gerekir. Seçenek listesinde, onay kutusu üzerinde işlem yapabilirsiniz. Benzer şekilde, programlı olarak Aspose.Cells API kullanarak dilimleyici ve pivot tablonun ilişkisini kesmek istiyorsanız, lütfen[**Slicer.removePivotConnection(PivotTable pivotu)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection(com.aspose.cells.PivotTable)) yöntem. Dilimleyici ve pivot tablonun ilişkisini kesecektir.

## **Dilimleyiciyi Çıkarma**

Aşağıdaki örnek kod,[örnek excel dosyası](remove-pivot-connection.xlsx)mevcut bir dilimleyici içerir. Dilimleyicilere erişir ve ardından dilimleyici ile pivot tablonun ilişkisini keser. Son olarak, çalışma kitabını şu şekilde kaydeder:[çıktı excel dosyası](remove-pivot-connection-out.xlsx). 


## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}