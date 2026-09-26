---
title: Convert Text to Columns using Aspose.Cells with Golang via C++
linktitle: Convert Text to Columns
type: docs
weight: 30
url: /go-cpp/convert-text-to-columns-using-aspose-cells/
description: Learn how to convert text to columns in Excel files using Aspose.Cells for Go via C++.
---

## **Possible Usage Scenarios**

You can convert your text to columns using Microsoft Excel. This feature is available from *Data Tools* under the *Data* tab. In order to split the contents of a column into multiple columns, the data should contain a specific delimiter such as a comma (or any other character) based on which Microsoft Excel splits the contents of a cell into multiple cells. Aspose.Cells also provides this feature via the [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/go-cpp/cells/texttocolumns/) method.

## **Convert Text to Columns using Aspose.Cells**

The following sample code explains the usage of the [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/go-cpp/cells/texttocolumns/) method. The code first adds some people's names in column A of the first worksheet. The first and last names are separated by a space character. Then it applies the [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/go-cpp/cells/texttocolumns/) method on column A and saves the result as an output Excel file. If you open the [output Excel file](25395213.xlsx), you will see that the first names are in column A while the last names are in column B, as shown in this screenshot.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertTextToColumnsUsingAsposeCells.go" >}}
{{< app/cells/assistant language="go" >}}
