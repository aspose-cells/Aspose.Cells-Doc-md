---
title: Convert Text to Columns using Aspose.Cells
type: docs
weight: 30
url: /python-net/convert-text-to-columns-using-aspose-cells/
description: This article shows how to Convert Text to Columns by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Convert Text to Columns, Convert Text to Columns in Python.
---

## **Possible Usage Scenarios**

You can convert your Text to Columns using Microsoft Excel. This feature is available from *Data Tools* under the *Data* tab. In order to split the contents of a column to multiple columns, the data should contain a specific delimiter such as a comma (or any other character) based on which Microsoft Excel splits the contents of a cell to multiple cells. Aspose.Cells for Python via .NET also provides this feature via [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) method.

## **Convert Text to Columns using Aspose.Cells for Python Excel Library**

The following sample code explains the usage of [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) method. The code first adds some people name in column A of the first worksheet. The first and last name is separated by space character. Then it applies [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) method on column A and save it as output excel file. If you open the [output excel file](25395213.xlsx), you will see, first names are in column A while last names are in column B as shown in this screenshot.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
