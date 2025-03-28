---
title: Insert Hyperlinks into Excel or OpenOffice
linktitle: Managing Hyperlinks
type: docs
weight: 45
url: /nodejs-cpp/insert-hyperlinks-to-excel/
description: How to insert hyperlinks into Excel file with Aspose.Cells library without MS Excel using Node.js via C++.
keywords: Insert Hyperlinks into Excel Node.js via C++, Add or Insert Hyperlinks Node.js via C++, Add or Insert link to a URL Node.js via C++, Add or Insert a Link to a Cell Node.js via C++, Add a Link to an External File Node.js via C++
---

{{% alert color="primary" %}} 

A hyperlink is used to create a link between two entities. Everybody is familiar with the use of hyperlinks, especially on websites.
Using Aspose.Cells, developers can create different kinds of hyperlinks in Microsoft Excel files. This topic discusses what types of hyperlinks are supported by Aspose.Cells and how they can be used in our Excel files.

{{% /alert %}} 

## **Adding Hyperlinks**
Aspose.Cells allows developers to add hyperlinks to Excel files either using the API or designer spreadsheets (spreadsheets where hyperlinks are created manually and Aspose.Cells is used to import them into other spreadsheets).

Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides different methods for adding different hyperlinks to Excel files.
## **Adding Link to a URL**
The [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class contains a [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) collection. Each item in the [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) collection represents a [Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink). Add hyperlinks to URLs by calling the [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) collection's [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) method. The [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) method takes the following parameters:

- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the URL address.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

In the above example, a hyperlink is added to a URL in an empty cell, **A1**. In such cases, if a cell is empty then the URL address is also added to that empty cell as its value. If the cell is not empty and a hyperlink is added, the value of the cell looks like plain text. To make it look like a hyperlink, apply the appropriate formatting settings on that cell.

{{% /alert %}} 
## **Adding a Link to a Cell in the Same File**
It is possible to add hyperlinks to cells in the same Excel file by calling the [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) collection's [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) method. The [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) method works for both internal and external hyperlinks. One version of the overloaded method takes the following parameters:

- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target cell.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **Adding a Link to an External File**
It is possible to add hyperlinks to external Excel files by calling the [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) collection's [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) method. The [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) method takes the following parameters:

- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target, external Excel file.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **Advance topics**
- [Add Image Hyperlinks](/cells/nodejs-cpp/add-image-hyperlinks/)
- [Detect Hyperlink Type](/cells/nodejs-cpp/detect-hyperlink-type/)
- [Editing Hyperlinks of Worksheet](/cells/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [Get Hyperlinks in Range](/cells/nodejs-cpp/get-hyperlinks-in-range/)

