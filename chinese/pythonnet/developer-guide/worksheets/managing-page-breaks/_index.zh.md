---
title: 管理分页
type: docs
weight: 30
url: /zh/python-net/managing-page-breaks/
description: 本文提供示例代码，介绍如何使用 Aspose.Cells for Python via .NET API 编程方式在Excel工作表中添加分页符、清除分页符或删除特定分页符。
keywords: Python Excel 库，Python 分页符，Python 中的Excel分页符，清除分页符。
---

{{% alert color="primary" %}}

根据定义，分页是文本流中一页结束并另一页开始的地方。 Microsoft Excel允许用户在工作表的任何选定单元格中添加分页。 

分页符的位置在添加分页符的单元格，分页在打印时会结束该页面，其后数据打印到下一页。简单来说，分页符将工作表分成多个页面，按照您的要求。您还可以在运行时使用 Aspose.Cells for Python via .NET 添加分页符。Aspose.Cells for Python via .NET 允许开发者添加两种类型的分页符：

- 水平分页
- 垂直分页

在以下讨论中，我们将介绍如何使用 Aspose.Cells for Python via .NET 在工作表中添加水平或垂直分页符。

{{% /alert %}}

## **分页**

Aspose.Cells for Python via .NET 提供了一个 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类，代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，可以访问Excel文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供了用于管理工作表的广泛的属性和方法。

要添加分页符，使用 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类的 [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) 和 [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) 属性。

[**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) 和 [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) 属性是可能包含多个分页符的集合。每个集合都包含用于管理水平和垂直分页符的几种方法。

## **如何添加分页符**

要在工作表中添加分页符，在指定的单元格插入水平和垂直分页符，调用 [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) 和 [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str) 方法。每个 **add** 方法都接受要添加分页符的单元格名称。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

在分页预览或打印预览模式下，您可以看到这些分页符的工作方式。

{{% /alert %}}


## **重要提示**

当您在页面设置中设置 **FitToPages** 属性（即 [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) 和 [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)）时，分页符设置会受影响，因此，如果您打印工作表，分页符设置不会考虑，尽管它们仍然被设置。
{{< app/cells/assistant language="python-net" >}}
