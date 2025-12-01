---
title: Set column width to scalable unit like em or percent
type: docs
weight: 130
url: /python-net/set-column-width-to-scalable-unit-like-em-or-percent/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Generating an HTML file from a spreadsheet is very common. The size of the columns is defined in "pt" which works in many cases. However, there can be a case where this fixed size may not be required. For example, if a container panel width is 600px where this HTML page is being displayed. In this case, you may get a horizontal scrollbar if the generated table width is bigger. It was required that this fixed size shall be changed into a scalable unit like em or percent to get a better presentation. Following sample code can be used where [**HtmlSaveOptions.width_scalable**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/width_scalable) is set to **true** for creating scalable width.

Sample source file and output files can be downloaded from the following links:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetScalableColumnWidth-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
