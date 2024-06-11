---
title: 在电子表格中对数据进行排序
type: docs
weight: 70
url: /zh/java/sort-data-in-spreadsheets/
---

## **Aspose.Cells - 对电子表格中的数据进行排序**
{{% alert color="primary" %}} 

要使用Aspose.Cells在电子表格中对数据进行排序，只需在设置单元格区域的一些易设置属性后调用DataSorter.sorter()方法。

以下是Java代码。

{{% /alert %}} 

使用Aspose.Cells对数据进行排序

Java

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)

{{% alert color="primary" %}} 

要了解更多详情，请访问[数据排序](/java/sort-data)，或[数据排序](/cells/zh/java/data-sorting)。

{{% /alert %}}
