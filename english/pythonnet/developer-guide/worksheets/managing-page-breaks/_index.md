---
title: Managing Page Breaks
type: docs
weight: 30
url: /python-net/managing-page-breaks/
description: This article provides sample code and explains how to add page breaks, clear page breaks, or delete specific page breaks in Excel worksheets programmatically using Aspose.Cells for Python via .NET APIs.
keywords: Python Excel Library, Python page breaks, excel page breaks in Python, clear page break in Python.
---

{{% alert color="primary" %}}

According to the definition, a page break is a place in a flow of text where one page ends and the next begins. Microsoft Excel lets users add page breaks into any selected cell of a worksheet.

The location of the cell where the page break is added, the page is ended and the rest of the data after the page break is printed on the next page while printing. In simple words, page breaks divide your worksheet into multiple pages according to your specifications. You can also add page breaks to your worksheets at runtime using Aspose.Cells for Python via .NET. Aspose.Cells for Python via .NET allows developers to add two kinds of page breaks:

- Horizontal page break
- Vertical page break

In the rest of the discussion, we will describe how can you add horizontal or vertical page breaks into your worksheets using Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Page Breaks**

Aspose.Cells for Python via .NET provides a [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a wide range of properties and methods used to manage a worksheet.

To add the page breaks, use the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class' [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) and [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) properties.

The [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) and [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) properties are collections that may contain several page breaks. Each collection contains several methods for managing horizontal and vertical page breaks.

## **How to Add Page Breaks**

To add a page break in a worksheet, insert vertical and horizontal page breaks at the specified cell by calling the [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) and [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str) methods. Each **add** method takes the name of the cell where the break should be added.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

In page break preview or print preview modes, you can see how these page breaks work.

{{% /alert %}}


## **Important to know**

When you set **FitToPages** properties (that is [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) and [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) in page setup settings, the page break settings are affected, so, if you print the worksheet, the page break settings are not considered although they are still set.
