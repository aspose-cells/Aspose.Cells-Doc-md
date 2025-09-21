---
title: Set Default Font while rendering spreadsheet to HTML with Golang via C++
linktitle: Set Default Font while rendering spreadsheet to HTML
type: docs
weight: 370
url: /go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: Learn how to set default font while rendering spreadsheet to HTML using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to set the default font while rendering a spreadsheet to HTML. Please use the [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) for this purpose. This property is useful when there are some cells in a spreadsheet that have invalid or non-existing fonts. Then those cells will be rendered in a font specified with the [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) property.

{{% /alert %}}

## Set Default Font while rendering spreadsheet to HTML

The following sample code creates a workbook and adds some text in cell B4 of the first worksheet and sets its font to some unknown/non-existing font. Then it saves the workbook in HTML by setting different default font names like Courier New, Arial, Times New Roman, etc.

The screenshot shows the effect of setting different default font names via [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) property.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

The code generates the [output HTML file with Courier New](5115516), the [output HTML with Arial](5115518), and the [output HTML file with Times New Roman](5115517).

## Sample Code

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}