---
title: 数据排序
type: docs
weight: 130
url: /zh/net/sort-data-of-excel/
description: 了解如何使用 Aspose.Cells for .NET API 对数据进行排序。
keywords: Sort data in ascending or descending order, Sort data based on the background color
---
{{% alert color="primary" %}}

数据排序是 Microsoft Excel 的众多有用功能之一。它允许用户对数据进行排序以使其更容易扫描。 Aspose.Cells 允许开发人员按字母或数字对工作表数据进行排序，其工作方式与 Microsoft Excel 对数据进行排序的方式相同。

{{% /alert %}}

##  **在 Microsoft Excel 中对数据进行排序**

要对 Microsoft Excel 中的数据进行排序：

1. 选择**数据**来自**种类**菜单。将显示排序对话框。
1. 选择排序选项。

通常，排序是在列表上执行的 - 列表定义为连续的数据组，其中数据显示在列中。

##  **使用 Aspose.Cells 对数据进行排序**

 Aspose.Cells 提供[**数据分类器**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)用于按升序或降序对数据进行排序的类。该类有一些重要的成员，例如 Key1 ... Key3 和 Order1 ... Order3 等属性。这些成员用于定义排序键并指定键排序顺序。

在实现数据排序之前，您必须定义键并设置排序顺序。该类提供了[**种类**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)用于根据工作表中的单元格数据执行数据排序的方法。

这[**种类**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)方法接受以下参数：

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)，基础工作表的单元格。
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)，单元格范围。在应用数据排序之前定义单元格区域。

本示例使用在 Microsoft Excel 中创建的模板文件“Book1.xls”。执行以下代码后，数据将被适当排序。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

如果您想对 *LeftToRight* 进行排序，请使用[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright)属性。

{{% /alert %}}

###  **使用背景颜色对数据进行排序**

Excel 提供了根据背景颜色对数据进行排序的功能。使用 Aspose.Cells 使用 DataSorter 提供了相同的功能，其中[**按类型排序**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor 可用于[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)根据背景颜色对数据进行排序。包含指定颜色的所有单元格[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)、函数根据 SortOrder 设置放置在顶部或底部，其余单元格的顺序根本不改变。

以下是可下载用于测试此功能的示例文件：

[样本背景文件.xlsx](81920906.xlsx)

[输出样本BackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

##  **高级主题**
- [使用自定义排序列表对列中的数据进行排序](/cells/zh/net/sort-data-in-column-with-custom-sort-list/)
- [指定数据排序时的排序警告](/cells/zh/net/specifying-sort-warning-while-sorting-data/)
