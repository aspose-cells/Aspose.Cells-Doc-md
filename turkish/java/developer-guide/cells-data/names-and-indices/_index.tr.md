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

Aspose.Cells, geliştiricilerin satır ve sütun indekslerini sağladıklarında hücrenin adını almasına izin veren [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-)  metodunu sağlar.

{{% alert color="primary" %}} 

Microsoft Excel satır ve sütun indekslerini 1’den başlatır. Aspose.Cells ise satır ve sütun indekslerini 0’dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod, [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) kullanarak bilinen bir satır ve sütun indeksine göre hücrenin adını nasıl alacağınızı gösterir. Kod, aşağıdaki çıktıyı üretir.

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Hücre Adından Satır ve Sütun İndekslerini Nasıl Alınır**
Bir hücrenin adından satır ve sütun dizinini bulmak mümkündür. Bu makale açıklar.

Aspose.Cells, geliştiricilerin hücrenin adından satır ve sütun indekslerini almalarına olanak tanıyan [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-)  metodunu sağlar.

{{% alert color="primary" %}} 

Microsoft Excel satır ve sütun indekslerini 1’den başlatır. Aspose.Cells ise satır ve sütun indekslerini 0’dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod, [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) kullanarak hücrenin adından satır ve sütun indekslerini nasıl alacağınızı gösterir. Kod, aşağıdaki çıktıyı üretir.

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Güvenli sayfa adları nasıl oluşturulur**
Bazı durumlarda çalışma zamanında sayfa adı atanması gerekebilir. Bu senaryoda, sayfa adında <>+(?” gibi bazı ek karakterleri içerebilecek sayfa adları olabilir. Sayfa adı olarak izin verilmeyen herhangi bir karakterin, kullanıcı tarafından belirtilen önceden belirlenmiş bir karakterle değiştirilmesi gerekmektedir. Benzer şekilde, uzunluk 31 karakterden fazla olabilir ve kısaltılması gerekmektedir. Apache POI, güvenli adlar oluşturmanın belirli özelliklerini sağlar, dolayısıyla Aspose.Cells tarafından tüm bu sorunları ele almak için benzer özellik sağlanmıştır. Aşağıdaki örnek kod, bu özelliği de gösterir:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Konsol Çıktısı**

Bu, oluşturulmuş ilk adın kısaltıldığı ad

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
