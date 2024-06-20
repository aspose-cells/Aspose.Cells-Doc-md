---
title: スプレッドシートでのデータのソート
type: docs
weight: 70
url: /ja/java/sort-data-in-spreadsheets/
---

## **Aspose.Cells - スプレッドシートでのデータのソート**
{{% alert color="primary" %}} 

Aspose.Cellsを使用してスプレッドシートのデータをソートするには、cell areaのいくつかの簡単に設定できるプロパティを設定した後、DataSorter.sorter()メソッドを単に呼び出します。

以下にJavaコードが記載されています。

{{% /alert %}} 

Aspose.Cellsを使用してデータをソート

**Java**

{{< highlight java >}}

 //Obtain the DataSorter object in the workbook

DataSorter sorter = workbook.getDataSorter();

//Set the first order

sorter.setOrder1(SortOrder.ASCENDING);

//Define the first key.

sorter.setKey1(0);

//Set the second order

sorter.setOrder2(SortOrder.ASCENDING);

//Define the second key

sorter.setKey2(1);

//Create a cells area (range).

CellArea ca = new CellArea();

//Specify the start row index.

ca.StartRow = 1;

//Specify the start column index.

ca.StartColumn = 0;

//Specify the last row index.

ca.EndRow = 9;

//Specify the last column index.

ca.EndColumn = 2;

//Sort data in the specified data range (A2:C10)

sorter.sort(cells, ca);

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)

{{% alert color="primary" %}} 

[データのソート](/java/sort-data)または[データのソート](/cells/ja/java/data-sorting)の詳細については

{{% /alert %}}
