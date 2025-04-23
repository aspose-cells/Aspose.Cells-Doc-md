---
title: 数据排序
type: docs
weight: 90
url: /zh/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

数据排序是 Microsoft Excel 的众多有用功能之一。它允许用户对数据进行排序，使其更容易浏览。

Aspose.Cells 允许您按字母顺序或数字顺序对工作表数据进行排序。它的工作方式与 Microsoft Excel 的数据排序相同。

{{% /alert %}}

## **在 Microsoft Excel 中排序数据**

要在 Microsoft Excel 中排序数据：

1. 从 **排序** 菜单中选择 **数据**。
   显示排序对话框。
1. 选择排序选项。

通常，排序是针对一个列表执行的 - 定义为一组连续的数据，数据以列显示。

Microsoft Excel 中的排序对话框

![todo:image_alt_text](data-sorting_1.png)

## **使用 Aspose.Cells 进行数据排序**

Aspose.Cells 提供了用于按升序或降序对数据进行排序的 [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) 类。该类具有一些重要成员，例如 [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) 和 [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)。这些成员用于定义排序键和指定键排序顺序。

在执行数据排序之前，您必须定义关键字并设置排序顺序。该类提供了 [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) 方法，用于根据工作表中的单元格数据执行数据排序。

[**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) 方法接受以下参数：

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)，工作表的单元格。
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)，单元格范围。在应用数据排序前定义单元格区域。

此示例显示如何使用 Aspose.Cells API 对数据进行排序。 该示例使用模板文件 "Book1.xls" 并对第一个工作表中数据范围 (A1:B14) 进行排序。

此示例使用在 Microsoft Excel 中创建的模板文件 "Book1.xls"。

**带数据的模板Excel文件**

![todo:image_alt_text](data-sorting_2.png)

执行下面的代码后，数据将被适当地排序，如输出的 Excel 文件所示。

**排序数据后的输出Excel文件**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

要进行*LeftToRight*排序，请使用[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight)属性。

{{% /alert %}}

## **以背景颜色排序数据**

Excel提供了根据背景颜色对数据进行排序的功能。使用Aspose.Cells也提供了相同功能，可以使用[**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter)，其中[**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL-COLOR)可以在[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-)中用于根据背景颜色对数据进行排序。包含[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-)函数中指定颜色的所有单元格将根据SortOrder设置放置在顶部或底部，并且其余单元格的顺序不会改变。

以下是可以下载以进行此功能测试的样本文件：

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **高级主题**
- [使用自定义排序列表对列中的数据进行排序](/cells/zh/java/sort-data-in-column-with-custom-sort-list/)
- [在对数据进行排序时指定排序警告](/cells/zh/java/specifying-sort-warning-while-sorting-data/)

{{< app/cells/assistant language="java" >}}
