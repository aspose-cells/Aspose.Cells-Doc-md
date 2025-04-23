---
title: 设置边距
type: docs
weight: 20
url: /zh/python-net/setting-margins/
description: 本文将介绍如何使用示例代码设置Excel工作表的边距。你还将学习如何使用Aspose.Cells for Python via .NET API以编程方式设置页面中心、页眉和页脚边距。
keywords: Python Excel 库，Python 设置Excel工作表边距居中，使用Python设置工作表页眉和页脚边距。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 完全支持Microsoft Excel的页面设置选项。开发者可能需要配置工作表的页面设置以控制打印过程。本主题讨论如何使用 Aspose.Cells for Python via .NET 设置页面边距。

{{% /alert %}}

## **如何设置边距**

Aspose.Cells for Python via .NET 提供一个类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，表示一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，可以访问Excel文件中的每个工作表。一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了[**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup/)属性，用于设置工作表的页面设置选项。[**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup)属性是[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)类的一个对象，使开发人员能够为打印的工作表设置不同的页面布局选项。[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)类提供了用于设置页面设置选项的各种属性和方法。

## **如何设置页面边距**

使用[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)类的成员设置页面边距（左、右、上、下）。下面列出了一些用于指定页面边距的方法：

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **如何页面居中**

可以在页面上水平和垂直居中某物。为此，[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)类的一些有用的成员是[**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/)和[**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **如何设置页眉和页脚边距**

使用[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)类的成员（如[**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin)和[**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin)）设置页眉和页脚边距。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
