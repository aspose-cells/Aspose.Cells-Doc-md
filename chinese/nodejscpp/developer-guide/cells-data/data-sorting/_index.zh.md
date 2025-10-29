---
title: 数据排序
type: docs
weight: 130
url: /zh/nodejs-cpp/sort-data-of-excel/
description: 学习如何使用Aspose.Cells for Node.js via C++ API进行数据排序。
keywords: 按升序或降序对数据进行排序，根据背景颜色对数据进行排序
---

{{% alert color="primary" %}}

数据排序是微软Excel的众多实用功能之一。它允许用户对数据进行排序以便于浏览。Aspose.Cells for Node.js via C++允许开发者对工作表中的数据按字母或数字排序，操作方式与微软Excel相同。

{{% /alert %}}

## **在 Microsoft Excel 中排序数据**

要在 Microsoft Excel 中排序数据：

1. 从“排序”菜单中选择“数据”。将显示“排序”对话框。
1. 选择排序选项。

通常，排序是针对一个列表执行的 - 定义为一组连续的数据，数据以列显示。

## **使用 Aspose.Cells 进行数据排序**

Aspose.Cells for Node.js via C++提供[**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter)类，用于按升序或降序排序数据。该类具有一些重要成员，例如Key1 ... Key3和Order1 ... Order3属性，用于定义排序键和值的排序顺序。

在执行数据排序之前，您必须定义关键字并设置排序顺序。该类提供了 [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) 方法，用于根据工作表中的单元格数据执行数据排序。

[**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) 方法接受以下参数：

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)，基础工作表的单元格。
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea)，单元格范围。在应用数据排序前定义单元格区域。

此示例使用在Microsoft Excel中创建的模板文件"Book1.xls"。在执行下面的代码后，数据将被适当地排序。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

如果要进行*由左至右*的排序，请使用[**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-)属性。

{{% /alert %}}

### **以背景颜色排序数据**

Excel提供基于背景色排序数据的功能。通过Aspose.Cells for Node.js via C++中的DataSorter实现相同功能，可以使用[**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/).CellColor在[**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-)中对数据进行背景色排序。所有包含指定颜色的单元格（一系列函数）按照SortOrder设置放在顶部或底部，其余单元格的顺序不变。

以下是可以下载以进行此功能测试的样本文件：

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **高级主题**
- [使用自定义排序列表对列中的数据进行排序](/cells/zh/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [在对数据进行排序时指定排序警告](/cells/zh/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

{{< app/cells/assistant language="nodejs-cpp" >}}
