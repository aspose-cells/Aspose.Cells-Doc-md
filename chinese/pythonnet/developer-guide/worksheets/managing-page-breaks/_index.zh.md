---
title: 管理分页
type: docs
weight: 30
url: /zh/python-net/managing-page-breaks/
description: 本文提供了示例代码并说明了如何使用Aspose.Cells for Python via .NET API以编程方式向Excel工作表中添加分页符、清除分页符或删除特定分页符。
keywords: Python Excel库，Python页面分页符，Python中的Excel页面分页符，Python中清除页面分页。
---

{{% alert color="primary" %}}

根据定义，分页是文本流中一页结束并另一页开始的地方。 Microsoft Excel允许用户在工作表的任何选定单元格中添加分页。 

添加页面分页符的单元格位置，分页结束并在页面分页后将其余数据打印到下一页。简单来说，页面分页符根据您的规格将工作表分成多个页面。你也可以使用Aspose.Cells for Python via .NET在运行时向你的工作表添加页面分页符。Aspose.Cells for Python via .NET允许开发者添加两种页面分页符。

- 水平分页
- 垂直分页

在讨论的其余部分，我们将描述如何使用Aspose.Cells for Python via .NET向您的工作表中添加水平或垂直页面分页符。

{{% /alert %}}

## **分页**

Aspose.Cells for Python via .NET提供了一个[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类，表示一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供了用于管理工作表的广泛的属性和方法。

要添加分页符，使用 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类的 [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) 和 [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) 属性。

[**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) 和 [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) 属性是可能包含多个分页符的集合。每个集合都包含用于管理水平和垂直分页符的几种方法。

## **如何添加分页符**

要在工作表中添加分页符，请通过调用[**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str)和[**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str)方法在指定单元格处插入垂直和水平分页符。每个**add**方法都需要添加分页符的单元格名称。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

在分页预览或打印预览模式下，您可以看到这些分页符的工作方式。

{{% /alert %}}


## **重要提示**

当您在页面设置中设置 **FitToPages** 属性（即 [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) 和 [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)）时，分页符设置会受影响，因此，如果您打印工作表，分页符设置不会考虑，尽管它们仍然被设置。
