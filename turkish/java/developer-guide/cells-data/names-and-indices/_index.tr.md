---
title: Hücre adı ile satır/sütun dizini arasındaki dönüşüm
linktitle: Cell İsim ve Dizin Dönüşümü
type: docs
weight: 5
url: /tr/java/names-and-indices/
description: Aspose.Cells for Java API'leri ile hücre adı ile satır/sütun dizini arasındaki Dönüşüm sonucunu nasıl alacağınızı öğrenin.
keywords: Java Convert cell index to name, Convert cell name to row/column index using java apis, How to Get Cell Name from Row and Column Indices with java, Java How to Get Row and Column Indices from Cell Name.
---
##  **Satır ve Sütun İndekslerinden Cell Adı Nasıl Alınır?**
Satır ve sütun indeksine göre bir hücrenin adını bulmak mümkündür. Bu makalede bunun nasıl yapılacağı açıklanmaktadır.

 Aspose.Cells şunları sağlar[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) geliştiricilerin satır ve sütun dizinini sağlamaları durumunda hücrenin adını almalarına olanak tanıyan yöntem.

{{% alert color="primary" %}} 

Satır ve sütun dizinlerinin 1'den başladığı Microsoft Excel'in aksine, Aspose.Cells, satır ve sütun dizinlerini 0'dan saymaya başlar.

{{% /alert %}} 

 Aşağıdaki örnek kod nasıl kullanılacağını gösterir[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) bilinen bir satır ve sütun dizininde verilen hücre adına erişmek için. Kod aşağıdaki çıktıyı üretir.



Cell [0, 0]'daki ad: A1

Cell [4, 0]'daki ad: A5

Cell [0, 4]'teki ad: E1

Cell [2, 2]'deki ad: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
##  **Cell Adından Satır ve Sütun İndeksleri Nasıl Alınır?**
Adından hücrenin satır ve sütun indeksini bulmak mümkündür. Bu makalede bunun nasıl yapılacağı açıklanmaktadır.

 Aspose.Cells şunları sağlar[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) geliştiricilerin hücrenin adından satır ve sütun dizini almasına olanak tanıyan yöntem.

{{% alert color="primary" %}} 

Satır ve sütun dizinlerinin 1'den başladığı Microsoft Excel'in aksine, Aspose.Cells, satır ve sütun dizinlerini 0'dan saymaya başlar.

{{% /alert %}} 

 Aşağıdaki örnek kod nasıl kullanılacağını gösterir[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) hücrenin adından satır ve sütun dizinini almak için. Kod aşağıdaki çıktıyı üretir.



Cell C6 Satır Dizini: 5

Cell C6 Sütun Dizini: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
##  **Güvenli sayfa adları nasıl oluşturulur**
 Bazen çalışma zamanında sayfa adını atamaya ihtiyaç duyulur. Bu senaryoda, aşağıdaki gibi bazı ek karakterleri içerebilecek sayfa adları olabilir:<>+(?”. Sayfa adı olarak kullanılmasına izin verilmeyen herhangi bir karakterin, kullanıcı tarafından sağlanan önceden belirlenmiş bir karakterle değiştirilmesine ihtiyaç vardır. Benzer şekilde, uzunluk, kesilmesi gereken 31 karakterden fazla artabilir. Apache POI, güvenli adlar oluşturmanın belirli özelliklerini sağlar, dolayısıyla tüm bu sorunları çözmek için Aspose.Cells tarafından benzer özellik sağlanmıştır. Aşağıdaki örnek kod bu özelliği göstermektedir:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Konsol Çıkışı**

bu cre olan ilk isim

` `<> + (adj.Özel _ " Özel"
