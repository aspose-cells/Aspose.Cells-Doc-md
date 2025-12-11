---
title: Specify how to cross string in output HTML using HtmlCrossType
type: docs
weight: 140
url: /net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When a cell contains text or a string that is larger than the width of the cell, the string overflows if the next cell in the next column is null or empty. When you save your Excel file to HTML, you can control this overflow by specifying the cross type using the [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) enumeration. It has the following values:

- **HtmlCrossType.Default**: Displays like MS Excel, depending on the next cell. If the next cell is null, the string will cross; otherwise, it will be truncated.

- **HtmlCrossType.MSExport**: Displays the string as MS Excel does when exporting to HTML.

- **HtmlCrossType.Cross**: Displays an HTML cross string; the performance for creating large HTML files will be more than ten times faster than setting the value to Default or FitToCell.

- **HtmlCrossType.FitToCell**: Displays the string only within the width of the cell.

## **Specify how to cross string in output HTML using HtmlCrossType**

The following sample code loads the [sample Excel file](51740732.xlsx) and saves it to HTML format by specifying different [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) values. Please download the [output HTMLs](51740734.zip) generated with this code. The sample Excel file contains an image bordered with red color, as shown in this screenshot, which demonstrates the effect of the [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) values on the output HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
