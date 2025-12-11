---
title: Convert Excel to HTML with tooltip
type: docs
weight: 200
url: /python-net/convert-excel-to-html-with-tooltip/
description: This topic shows you how to convert Excel to HTML with tooltip using Aspose.Cells for Python via .NET.
keywords: Python Convert Excel to HTML with tooltip, Convert Excel to HTML with tooltip Python via NET, Python via NET Excel to HTML with tooltip, Python Workbook to HTML with tooltip.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Convert Excel to HTML with tooltip**

There might be cases where the text is cut off in the generated HTML and you want to display the complete text as a tooltip on hover. Aspose.Cells supports this by providing the **HtmlSaveOptions.add_tooltip_text** property. Setting the **HtmlSaveOptions.add_tooltip_text** property to **true** will add the complete text as a tooltip in the generated HTML.

The following image shows the tooltip in the generated HTML file.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

The following code sample loads the [source Excel file](98107416.xlsx) and generates the [output HTML file](98107417.zip) with the tooltip.

Sample Code

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
