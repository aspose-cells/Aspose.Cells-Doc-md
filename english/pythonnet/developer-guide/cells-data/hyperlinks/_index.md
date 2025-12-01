---
title: Insert Hyperlinks into Excel or OpenOffice
linktitle: Managing Hyperlinks
type: docs
weight: 45
url: /python-net/insert-hyperlinks-to-excel/
description: How to insert hyperlinks into Excel file with Aspose.Cells for Python via .NET library without MS Excel.
keywords: Python Excel Library, Python Insert Hyperlinks into Excel, Python Add or Insert Hyperlinks, Python Add or Insert a link to a URL, Python Add or Insert a Link to a Cell, Python Add a Link to an External File
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

A hyperlink is used to create a link between two entities. Everybody is familiar with the use of hyperlinks, especially on websites.
Using Aspose.Cells for Python via .NET, developers can create different kinds of hyperlinks in Microsoft Excel files. This topic discusses what types of hyperlinks are supported by Aspose.Cells for Python via .NET and how they can be used in our Excel files.

{{% /alert %}} 
## **How to Add Hyperlinks**
Aspose.Cells for Python via .NET allows developers to add hyperlinks to Excel files either using the API or designer spreadsheets(spreadsheets where hyperlinks are created manually and Aspose.Cells for Python via .NET is used to import them into other spreadsheets).

Aspose.Cells for Python via .NET provides a class, [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides different methods for adding different hyperlinks to Excel files.

## **How to Add a Link to a URL**
The [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class contains a [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) collection. Each item in the [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) collection represents a [Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink). Add hyperlinks to URLs by calling the [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) collection's [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) method. The [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) method takes the following parameters:

- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range
- URL, the URL address.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

In the above example, a hyperlink is added to a URL in an empty cell, **A1**. In such cases, if a cell is empty then the URL address is also added to that empty cell as its value. If the cell is not empty and a hyperlink is added, the value of the cell looks like plain text. To make it look like a hyperlink, apply the appropriate formatting settings on that cell.

{{% /alert %}} 

## **How to Add a Link to a Cell in the Same File**
It is possible to add hyperlinks to cells in the same Excel file by calling the [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) collection's [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) method. The [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) method works for both internal and external hyperlinks. One version of the overloaded method takes the following parameters:

- Cell name,the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target cell.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **How to Add a Link to an External File**
It is possible to add hyperlinks to external Excel files by calling the [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) collection's [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) method. The [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) method takes the following parameters:

- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target, external Excel file.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **Advance topics**
- [Add Image Hyperlinks](/cells/python-net/add-image-hyperlinks/)
- [Detect Hyperlink Type](/cells/python-net/detect-hyperlink-type/)
- [Editing Hyperlinks of Worksheet](/cells/python-net/editing-hyperlinks-of-worksheet/)
- [Get Hyperlinks in Range](/cells/python-net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="python-net" >}}
