---
title: 数据排序
type: docs
weight: 130
url: /zh/net/sort-data-of-excel/
description: 学习如何使用Aspose.Cells for .NET API对数据进行排序。
keywords: 按升序或降序排序数据，根据背景颜色排序数据
---

{{% alert color="primary" %}}

数据排序是Microsoft Excel的许多有用功能之一。它允许用户对数据进行排序以便更易于扫描。Aspose.Cells让开发人员可以按字母顺序或数字顺序对工作表数据进行排序，这与Microsoft Excel对数据进行排序的方式相同。

{{% /alert %}}

## **在Microsoft Excel中对数据进行排序**

在Microsoft Excel中对数据进行排序：

1. 从**排序**菜单中选择**数据**。将显示排序对话框。
1. 选择一个排序选项。

通常，在列表上执行排序 - 定义为数据的连续组，其中数据以列显示。

## **使用Aspose.Cells对数据进行排序**

Aspose.Cells提供了用于按升序或降序对数据进行排序的[**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)类。 该类具有一些重要成员，例如Key1 ... Key3和Order1 ... Order3等属性。 这些成员用于定义排序键并指定键排序顺序。

在执行数据排序之前，您必须定义键并设置排序顺序。 该类提供了用于根据工作表中的单元格数据执行数据排序的[**Sort**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)方法。

[**Sort**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)方法接受以下参数：

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)，基础工作表的单元格。
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)，单元格范围。 在应用数据排序之前定义单元格区域。

此示例使用Microsoft Excel中创建的模板文件"Book1.xls"。 在执行以下代码后，数据将被适当排序。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

如果要进行*从左到右*的排序，请使用[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright)属性。

{{% /alert %}}

### **根据背景颜色排序数据**

Excel提供了根据背景颜色排序数据的功能。 使用Aspose.Cells的DataSorter提供相同的功能，其中[**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor可用于[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)中根据背景颜色对数据进行排序。 包含指定颜色的所有单元格都根据SortOrder设置放在顶部或底部，其余单元格的顺序保持不变。

以下是可以下载用于测试此功能的示例文件：

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **高级主题**
- [对具有自定义排序列表的列进行排序数据](/cells/zh/net/sort-data-in-column-with-custom-sort-list/)
- [在排序数据时指定排序警告](/cells/zh/net/specifying-sort-warning-while-sorting-data/)
