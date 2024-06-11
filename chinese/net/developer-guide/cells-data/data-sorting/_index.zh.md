---
title: 数据排序
type: docs
weight: 130
url: /zh/net/sort-data-of-excel/
description: 学习如何通过 Aspose.Cells for .NET API 对数据进行排序。
keywords: 按升序或降序对数据进行排序，根据背景颜色对数据进行排序
---

{{% alert color="primary" %}}

数据排序是 Microsoft Excel 的许多有用功能之一。它允许用户对数据进行排序，以便更容易扫描。Aspose.Cells 允许开发人员按字母顺序或数字顺序对工作表数据进行排序，这与 Microsoft Excel 的数据排序方式相同。

{{% /alert %}}

## **在 Microsoft Excel 中排序数据**

要在 Microsoft Excel 中排序数据：

1. 从“排序”菜单中选择“数据”。将显示“排序”对话框。
1. 选择排序选项。

通常，排序是针对一个列表执行的 - 定义为一组连续的数据，数据以列显示。

## **使用 Aspose.Cells 进行数据排序**

Aspose.Cells 提供了用于按升序或降序对数据进行排序的 [**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter) 类。该类具有一些重要成员，例如 Key1 … Key3 和 Order1 … Order3 等属性。这些成员用于定义排序键并指定键排序顺序。

在执行数据排序之前，您必须定义关键字并设置排序顺序。该类提供了 [**Sort**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index) 方法，用于根据工作表中的单元格数据执行数据排序。

[**Sort**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1) 方法接受以下参数：

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)，基础工作表的单元格。
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)，单元格范围。在应用数据排序前定义单元格区域。

此示例使用在Microsoft Excel中创建的模板文件"Book1.xls"。在执行下面的代码后，数据将被适当地排序。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

如果要进行*由左至右*的排序，请使用[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright)属性。

{{% /alert %}}

### **以背景颜色排序数据**

Excel提供了根据背景颜色对数据进行排序的功能。使用Aspose.Cells的DataSorter，可以使用[**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor在[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)中对基于背景颜色的数据进行排序。[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)中包含指定颜色的所有单元格，按照SortOrder设置的方式放置在顶部或底部，其余单元格的顺序保持不变。

以下是可以下载以进行此功能测试的样本文件：

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **高级主题**
- [使用自定义排序列表对列中的数据进行排序](/cells/zh/net/sort-data-in-column-with-custom-sort-list/)
- [在对数据进行排序时指定排序警告](/cells/zh/net/specifying-sort-warning-while-sorting-data/)
