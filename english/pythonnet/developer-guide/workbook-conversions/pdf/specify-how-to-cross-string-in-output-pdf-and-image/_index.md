---
title: Specify How to Cross Strings in Output PDF and Image
type: docs
weight: 120
url: /python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Learn how to cross strings in output PDF and image with Aspose.Cells for Python via .NET API.
keywords: Python Cross String in output PDF and image
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When a cell contains text or a string that is larger than the width of the cell, the string overflows if the next cell in the next column is null or empty. When you save your Excel file into PDF/Image, you can control this overflow by specifying the cross type using the **[TextCrossType](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)** enumeration. It has the following values:

- **TextCrossType.DEFAULT**: Display text like MS Excel, which depends on the next cell. If the next cell is null, the string will cross; otherwise, it will be truncated.

- **TextCrossType.CROSS_KEEP**: Display the string as MS Excel does when exporting to PDF/Image.

- **TextCrossType.CROSS_OVERRIDE**: Display all the text by crossing other cells and overriding the text of crossed cells.

- **TextCrossType.STRICT_IN_CELL**: Only display the string within the width of the cell.

## **Specify How to Cross Strings in Output PDF/Image Using TextCrossType**

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different **[TextCrossType](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)** values. The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Sample Code

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
