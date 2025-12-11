---
title: Set column width to scalable unit like em or percent
type: docs
weight: 130
url: /python-net/set-column-width-to-scalable-unit-like-em-or-percent/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Generating an HTML file from a spreadsheet is very common. The size of the columns is defined in "pt", which works in many cases. However, there can be a case where this fixed size is not suitable. For example, if a container panel width is 600 px where this HTML page is displayed, you may get a horizontal scrollbar if the generated table width is larger. It is required that this fixed size be changed to a scalable unit such as em or percent to achieve a better presentation. The following sample code can be used, where **HtmlSaveOptions.width_scalable** is set to **true** to create a scalable width.

Sample source file and output files can be downloaded from the following links:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetScalableColumnWidth-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
