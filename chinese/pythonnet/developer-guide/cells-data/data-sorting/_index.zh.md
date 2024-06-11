---
title: 数据排序
type: docs
weight: 130
url: /zh/python-net/sort-data-of-excel/
description: 通过使用Aspose.Cells for for Python通过.NET API学习如何排序数据。
keywords: Python Excel库，Python按升序或降序排序数据，Python根据背景颜色排序数据。
---

{{% alert color="primary" %}}

数据排序是Microsoft Excel的许多有用功能之一。它允许用户对数据进行排序，以便更容易浏览。Aspose.Cells for for Python通过.NET允许开发人员按字母顺序或数字顺序对工作表数据进行排序，这与Microsoft Excel对数据进行排序的方式相同。

{{% /alert %}}

## **在Microsoft Excel中对数据进行排序**

在Microsoft Excel中对数据进行排序：

1. 从**排序**菜单中选择**数据**。将显示排序对话框。
1. 选择一个排序选项。

通常，在列表上执行排序 - 定义为数据的连续组，其中数据以列显示。

## **使用Aspose.Cells for Python Excel库对数据进行排序**

Aspose.Cells for for Python通过.NET提供了[**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter)类用于按升序或降序对数据进行排序。该类具有一些重要成员，例如Key1 ... Key3和Order1 ... Order3等属性。这些成员用于定义排序键并指定键排序顺序。

在执行数据排序之前，您必须定义键并设置排序顺序。 该类提供了用于根据工作表中的单元格数据执行数据排序的[**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea)方法。

[**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea)方法接受以下参数：

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)，基础工作表的单元格。
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea)，单元格范围。 在应用数据排序之前定义单元格区域。

此示例使用Microsoft Excel中创建的模板文件"Book1.xls"。 在执行以下代码后，数据将被适当排序。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

如果要进行*从左到右*的排序，请使用[**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/)属性。

{{% /alert %}}

### **使用Aspose.Cells for Python Excel库基于背景颜色对数据进行排序**

Excel提供了基于背景颜色对数据进行排序的功能。使用Aspose.Cells for for Python通过.NET提供相同功能，使用DataSorter中的[**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/). CellColor可以在[**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any)中使用以根据背景颜色对数据进行排序。所有包含指定颜色的单元格在[**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any)函数中根据SortOrder设置放置在顶部或底部，并且其余单元格的顺序不会发生任何变化。

以下是可以下载用于测试此功能的示例文件：

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **高级主题**
- [对具有自定义排序列表的列进行排序数据](/cells/zh/python-net/sort-data-in-column-with-custom-sort-list/)
- [在排序数据时指定排序警告](/cells/zh/python-net/specifying-sort-warning-while-sorting-data/)
