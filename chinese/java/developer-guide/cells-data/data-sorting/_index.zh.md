---
title: 数据排序
type: docs
weight: 90
url: /zh/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

数据排序是Microsoft Excel的诸多实用功能之一。它允许用户对数据进行排序，以便更容易扫描。

Aspose.Cells允许您按字母顺序或数字顺序对工作表数据进行排序。它与Microsoft Excel以相同方式对数据进行排序。

{{% /alert %}}

## **在Microsoft Excel中对数据进行排序**

在Microsoft Excel中对数据进行排序：

1. 从**排序**菜单中选择**数据**。
   显示排序对话框。
1. 选择一个排序选项。

通常，在列表上执行排序 - 定义为数据的连续组，其中数据以列显示。

**Microsoft Excel中的排序对话框**

![todo:image_alt_text](data-sorting_1.png)

## **使用Aspose.Cells对数据进行排序**

Aspose.Cells提供了用于按升序或降序排序数据的[**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter)类。该类具有一些重要成员，例如方法如[**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1)... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2)... [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1)... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)...。这些成员用于定义排序键并指定键排序顺序。

在实施数据排序之前，您必须定义键并设置排序顺序。该类提供了用于基于工作表中的单元数据执行数据排序的[**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort())方法。

[**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()方法接受以下参数：

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)，工作表的单元格。
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)，单元格范围。 在应用数据排序之前定义单元格区域。

此示例显示如何使用Aspose.Cells API对数据进行排序。该示例使用名称为"Book1.xls"的模板文件，并对第一个工作表中的数据范围（A1:B14）进行排序：

此示例使用在Microsoft Excel中创建的名为"Book1.xls"的模板文件。

**包含数据的模板Excel文件**

![todo:image_alt_text](data-sorting_2.png)

执行下面的代码后，数据将按适当的顺序排序，如输出的Excel文件中所示。

**排序数据后的输出Excel文件**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

要对*从左到右*进行排序，请使用[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight)属性。

{{% /alert %}}

## **根据背景颜色排序数据**

Excel提供了根据背景颜色对数据进行排序的功能。使用Aspose.Cells提供相同功能，其中[**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter)可以在[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int))中使用[**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR)来根据背景颜色对数据进行排序。所有包含指定颜色的单元格都按照SortOrder设置放置在顶部或底部，并且其余单元格的顺序不变。

以下是可以下载用于测试此功能的示例文件：

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **高级主题**
- [对具有自定义排序列表的列进行排序数据](/cells/zh/java/sort-data-in-column-with-custom-sort-list/)
- [在排序数据时指定排序警告](/cells/zh/java/specifying-sort-warning-while-sorting-data/)

