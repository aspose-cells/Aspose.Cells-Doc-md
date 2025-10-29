---
title: 数据排序
type: docs
weight: 130
url: /zh/python-net/sort-data-of-excel/
description: 了解如何使用 Aspose.Cells for for Python via .NET API 进行数据排序。
keywords: Python Excel 库，Python 根据背景颜色对数据进行升序或降序排序，Python 根据背景颜色对数据进行排序。
---

{{% alert color="primary" %}}

数据排序是微软 Excel 的众多有用功能之一。它允许用户对数据进行排序以便于扫描。Aspose.Cells for Python via .NET 允许开发人员按字母顺序或数字顺序对工作表数据进行排序，其方式与微软 Excel 一样。

{{% /alert %}}

## **在 Microsoft Excel 中排序数据**

要在 Microsoft Excel 中排序数据：

1. 从“排序”菜单中选择“数据”。将显示“排序”对话框。
1. 选择排序选项。

通常，排序是针对一个列表执行的 - 定义为一组连续的数据，数据以列显示。

## **使用 Aspose.Cells for Python Excel 库对数据进行排序**

Aspose.Cells for for Python via .NET 提供了 [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter) 类用于对数据按升序或降序进行排序。该类具有一些重要成员，例如 Key1 ... Key3 和 Order1 ... Order3 等属性。这些成员用于定义排序关键字并指定关键字排序顺序。

在执行数据排序之前，您必须定义关键字并设置排序顺序。该类提供了 [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) 方法，用于根据工作表中的单元格数据执行数据排序。

[**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) 方法接受以下参数：

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)，基础工作表的单元格。
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea)，单元格范围。在应用数据排序前定义单元格区域。

此示例使用在Microsoft Excel中创建的模板文件"Book1.xls"。在执行下面的代码后，数据将被适当地排序。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

如果要进行*由左至右*的排序，请使用[**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/)属性。

{{% /alert %}}

### **使用Aspose.Cells for Python Excel Library对带有背景颜色的数据进行排序**

Excel提供了根据背景颜色对数据进行排序的功能。使用Aspose.Cells for for Python via .NET，可以使用DataSorter在[**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/)中使用CellColor来根据背景颜色对数据进行排序。在函数中包含指定颜色的所有单元格将根据SortOrder设置放在顶部或底部，其余单元格的顺序不会改变。

以下是可以下载以进行此功能测试的样本文件：

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **高级主题**
- [使用自定义排序列表对列中的数据进行排序](/cells/zh/python-net/sort-data-in-column-with-custom-sort-list/)
- [在对数据进行排序时指定排序警告](/cells/zh/python-net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="python-net" >}}
