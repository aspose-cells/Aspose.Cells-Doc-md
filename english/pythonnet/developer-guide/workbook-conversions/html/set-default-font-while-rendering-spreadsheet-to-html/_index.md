---
title: Set Default Font while rendering spreadsheet to HTML
type: docs
weight: 370
url: /python-net/set-default-font-while-rendering-spreadsheet-to/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to set default font while rendering spreadsheet to HTML. Please use the [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name) for this purpose. This property is useful when there are some cells in a spreadsheet that have invalid or non-existing fonts. Then those cells will be rendered in a font specified with the [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name) property.

{{% /alert %}}

## Set Default Font while rendering spreadsheet to HTML

The following sample code creates a workbook and adds some text in cell B4 of the first worksheet and sets its font to some unknown/non-existing font. Then it saves the workbook in HTML by setting different default font names like Courier New, Arial, Times New Roman, etc.

The screenshot shows the effect of setting different default font names via [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name) property.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

The code generates the [output HTML file with Courier New](5115516), the [output HTML with Arial](5115518), and the [output HTML file with Times New Roman](5115517).

## Sample Code

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetDefaultFontWhileRendering-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
