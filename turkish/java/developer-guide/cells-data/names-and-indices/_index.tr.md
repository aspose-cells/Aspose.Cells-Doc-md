---
title: Hücre adı ve satır/sütun dizini arasında dönüştürme işlemi
linktitle: Hücre Adı ve Dizin Dönüştürme
type: docs
weight: 5
url: /tr/java/names-and-indices/
description: Aspose.Cells for Java API larını kullanarak hücre adı ile satır/sütun indeksi arasındaki dönüşüm sonucunu nasıl alacağınızı öğrenin.
keywords: Java, hücre indeksini ada dönüştürme, hücre adını satır/sütun indeksine dönüştürme işlemlerini java apileri kullanarak nasıl yapılır, Java ile Hücre Adını Satır ve Sütun İndekslerine Nasıl Alınır.
---

## **Satır ve Sütun İndekslerinden Hücre Adını Nasıl Alınır**
Bir hücrenin adını bulmak mümkündür, verilen satır ve sütun dizini. Bu makale açıklar.

Aspose.Cells, geliştiricilere satır ve sütun indeksini sağladıklarında hücre adını alabilmelerini sağlayan [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) metodunu sağlar.

{{% alert color="primary" %}} 

Microsoft Excel'de satır ve sütun indislerinin 1'den başladığına karşın, Aspose.Cells satır ve sütun indislerini 0'dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod, [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) kullanımını gösterir. Bilinen bir satır ve sütun indeksindeki hücre adını erişmek için bu kod, aşağıdaki çıktıyı üretir.



[0, 0] Konumundaki Hücre Adı: A1

[4, 0] Konumundaki Hücre Adı: A5

[0, 4] Konumundaki Hücre Adı: E1

[2, 2] Konumundaki Hücre Adı: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Hücre Adından Satır ve Sütun İndekslerini Nasıl Alınır**
Bir hücrenin adından satır ve sütun dizinini bulmak mümkündür. Bu makale açıklar.

Aspose.Cells, geliştiricilere hücre adından satır ve sütun indeksini alabilmelerini sağlayan [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) metodunu sağlar.

{{% alert color="primary" %}} 

Microsoft Excel'de satır ve sütun indislerinin 1'den başladığına karşın, Aspose.Cells satır ve sütun indislerini 0'dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod, [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) kullanımını gösterir. Hücre adından satır ve sütun indeksini almak için bu kod, aşağıdaki çıktıyı üretir.



C6 Hücresinin Satır İndeksi: 5

C6 Hücresinin Sütun İndeksi: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Güvenli sayfa adları nasıl oluşturulur**
Bazı durumlarda çalışma zamanında sayfa adı atanması gerekebilir. Bu senaryoda, sayfa adında <>+(?” gibi bazı ek karakterleri içerebilecek sayfa adları olabilir. Sayfa adı olarak izin verilmeyen herhangi bir karakterin, kullanıcı tarafından belirtilen önceden belirlenmiş bir karakterle değiştirilmesi gerekmektedir. Benzer şekilde, uzunluk 31 karakterden fazla olabilir ve kısaltılması gerekmektedir. Apache POI, güvenli adlar oluşturmanın belirli özelliklerini sağlar, dolayısıyla Aspose.Cells tarafından tüm bu sorunları ele almak için benzer özellik sağlanmıştır. Aşağıdaki örnek kod, bu özelliği de gösterir:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Konsol Çıktısı**

Bu, oluşturulmuş ilk adın kısaltıldığı ad

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
