---
title: Specify how to cross a string in output HTML using HtmlCrossType with Golang via C++
linktitle: Specify HtmlCrossType in Output HTML
type: docs
weight: 140
url: /go-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Learn how to control string overflow in HTML output using Aspose.Cells for C++ with HtmlCrossType.
---

## **Possible Usage Scenarios**

When a cell contains text or a string that is larger than the width of the cell, the string overflows if the next cell in the next column is null or empty. When you save your Excel file to HTML, you can control this overflow by specifying the cross type using the [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) enumeration. It has the following values:

- **HtmlCrossType.Default**: Displays like MS Excel; depends on the next cell. If the next cell is null, the string will cross, otherwise it will be truncated.  
- **HtmlCrossType.MSExport**: Displays the string as MS Excel does when exporting to HTML.  
- **HtmlCrossType.Cross**: Displays the string as a cross in HTML; the performance when creating large HTML files is more than ten times faster than using Default or FitToCell.  
- **HtmlCrossType.FitToCell**: Displays only the string within the width of the cell.

## **Specify how to cross a string in output HTML using HtmlCrossType**

The following sample code loads the sample Excel file (`51740732.xlsx`) and saves it to HTML format while specifying different HtmlCrossType values. Please download the output HTML files (`51740734.zip`) generated with this code. The sample Excel file contains an image bordered in red, as shown in the screenshot, which demonstrates the effect of the HtmlCrossType values on the output HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputHtmlUsingHtmlcrosstype.go" >}}