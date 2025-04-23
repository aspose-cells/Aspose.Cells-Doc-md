---
title: Сортировка данных в электронных таблицах
type: docs
weight: 70
url: /ru/java/sort-data-in-spreadsheets/
---

## **Aspose.Cells - Сортировка данных в электронных таблицах**
{{% alert color="primary" %}} 

Для сортировки данных в электронных таблицах с использованием Aspose.Cells просто вызовите метод DataSorter.sorter() после установки нескольких легко устанавливаемых свойств области ячеек.

Приведен ниже Java-код.

{{% /alert %}} 

Сортировка данных с использованием Aspose.Cells

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
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)

{{% alert color="primary" %}} 

Дополнительные сведения см. в разделе [Сортировка данных](/java/sort-data) или [Сортировка данных](/cells/ru/java/data-sorting)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
