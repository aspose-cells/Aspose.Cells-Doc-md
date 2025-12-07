---
title: Set column width to scalable unit like em or percent
type: docs
weight: 130
url: /java/set-column-width-to-scalable-unit-like-em-or-percent/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Generating an HTML file from a spreadsheet is very common. The size of the columns is defined in "pt" which works in many cases. However, there can be a case where this fixed size may not be required. For example, if the container panel width is 600px where this HTML page is being displayed. In this case, you may get a horizontal scrollbar if the generated table width is bigger. It was required that this fixed size shall be changed into a scalable unit like em or percent to get a better presentation. Following sample code can be used where [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#setWidthScalable-boolean-) is set to **true** for creating scalable width.

Sample source file and output files can be downloaded from the following links:

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
{{< app/cells/assistant language="java" >}}
