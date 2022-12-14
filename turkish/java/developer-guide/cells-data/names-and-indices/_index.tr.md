---
title: Hücre adı ile satır/sütun dizini arasında dönüştürme
linktitle: Cell Ad ve Dizin Dönüştürme
type: docs
weight: 5
url: /tr/java/names-and-indices/
---
## **Satır ve Sütun İndekslerinden Cell Adını Alın**
Satır ve sütun dizini verilen bir hücrenin adını bulmak mümkündür. Bu makale nasıl yapılacağını açıklıyor.

 Aspose.Cells şunları sağlar:[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) geliştiricilerin satır ve sütun indeksini sağlamaları halinde bir hücrenin adını almalarına olanak sağlayan yöntem.

{{% alert color="primary" %}} 

Satır ve sütun indekslerinin 1'den başladığı Microsoft Excel'in aksine Aspose.Cells, satır ve sütun indekslerini 0'dan saymaya başlar.

{{% /alert %}} 

 Aşağıdaki örnek kod, nasıl kullanılacağını gösterir[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) bilinen bir satır ve sütun dizininde verilen hücre adına erişmek için. Kod aşağıdaki çıktıyı üretir.



Cell [0, 0]'daki ad: A1

Cell [4, 0]'daki ad: A5

Cell [0, 4]'teki ad: E1

Cell [2, 2]'deki ad: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Cell Adından Satır ve Sütun İndekslerini Alın**
Adından hücrenin satır ve sütun indeksini bulmak mümkündür. Bu makale nasıl yapılacağını açıklıyor.

 Aspose.Cells şunları sağlar:[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) geliştiricilerin hücrenin adından bir satır ve sütun dizini almasına izin veren yöntem.

{{% alert color="primary" %}} 

Satır ve sütun indekslerinin 1'den başladığı Microsoft Excel'in aksine Aspose.Cells, satır ve sütun indekslerini 0'dan saymaya başlar.

{{% /alert %}} 

 Aşağıdaki örnek kod, nasıl kullanılacağını gösterir[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) hücrenin adından satır ve sütun indeksini almak için. Kod aşağıdaki çıktıyı üretir.



Cell C6 Satır Dizini: 5

Cell C6 Sütun Dizini: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Güvenli sayfa adları oluşturun**
Bazen çalışma zamanında sayfa adının atanması gerekebilir. Bu senaryoda, bazı ek karakterler içerebilen sayfa adları olabilir.<>+(?”. Sayfa adı olarak izin verilmeyen bu tür herhangi bir karakteri, kullanıcı tarafından sağlanan önceden ayarlanmış bir karakterle değiştirmeye ihtiyaç vardır. Benzer şekilde, uzunluk, kesilmesi gereken 31 karakteri aşabilir. Apache POI, güvenli adlar oluşturmak için belirli özellikler sağlar, dolayısıyla benzer özellik, tüm bu sorunların üstesinden gelmek için Aspose.Cells tarafından sağlanır. Aşağıdaki örnek kod, bu özelliği gösterir:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Konsol Çıkışı**

bu ilk isim olan cre

` `<> + (adj.Özel _ " Özel"
