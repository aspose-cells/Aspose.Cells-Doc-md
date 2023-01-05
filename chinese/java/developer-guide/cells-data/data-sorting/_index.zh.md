---
title: 资料整理
type: docs
weight: 90
url: /zh/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

数据排序是 Microsoft Excel 众多有用的功能之一。它允许用户订购数据以使其更容易扫描。

Aspose.Cells 允许您按字母顺序或数字顺序对工作表数据进行排序。它的工作方式与 Microsoft Excel 对数据进行排序的方式相同。

{{% /alert %}}

## **在 Microsoft Excel 中对数据进行排序**

对 Microsoft Excel 中的数据进行排序：

1. 选择**数据**来自**种类**菜单。
显示排序对话框。
1. 选择一个排序选项。

通常，排序是在列表上执行的 - 定义为一组连续的数据，其中数据显示在列中。

**Microsoft Excel 中的排序对话框**

![待办事项：图片_替代_文本](data-sorting_1.png)

## **使用 Aspose.Cells 对数据进行排序**

Aspose.Cells 提供了[**数据分类器**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter)用于按升序或降序对数据进行排序的类。该类有一些重要的成员，例如，像这样的方法[**设置键1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**设置密钥2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2)和[**设置订单1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2).这些成员用于定义排序键并指定键排序顺序。

在实现数据排序之前，您必须定义键并设置排序顺序。该类提供[**种类**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()方法，用于根据工作表中的单元格数据执行数据排序。

这[**种类**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) 方法接受以下参数：

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), 工作表的单元格。
- [**单元格区域**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)单元格范围。在应用数据排序之前定义单元格区域。

此示例显示如何使用 Aspose.Cells API 对数据进行排序。该示例使用模板文件“Book1.xls”并在第一个工作表中对数据范围 (A1:B14) 的数据进行排序：

此示例使用在 Microsoft Excel 中创建的模板文件“Book1.xls”。

**包含数据的模板 Excel 文件**

![待办事项：图片_替代_文本](data-sorting_2.png)

执行下面的代码后，数据被适当地排序，正如您从输出的 Excel 文件中看到的那样。

**数据排序后输出Excel文件**

![待办事项：图片_替代_文本](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

排序*左到右*， 使用[**数据排序器.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight)属性。

{{% /alert %}}

## **使用背景颜色对数据进行排序**

Excel 提供了根据背景颜色对数据进行排序的功能。使用 Aspose.Cells 使用提供相同的功能[**数据分类器**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter)在哪里[**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR)可用于[**添加密钥()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ) 根据背景颜色对数据进行排序。包含指定颜色的所有单元格[**添加密钥()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), 函数根据 SortOrder 设置放置在顶部或底部，其余单元格的顺序根本没有改变。

以下是可以下载以测试此功能的示例文件：

[样本背景文件.xlsx](sampleBackGroundFile.xlsx)

[输出样本背景文件.xlsx](outputsampleBackGroundFile.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **推进主题**
- [使用自定义排序列表对列中的数据进行排序](/cells/zh/java/sort-data-in-column-with-custom-sort-list/)
- [排序数据时指定排序警告](/cells/zh/java/specifying-sort-warning-while-sorting-data/)

