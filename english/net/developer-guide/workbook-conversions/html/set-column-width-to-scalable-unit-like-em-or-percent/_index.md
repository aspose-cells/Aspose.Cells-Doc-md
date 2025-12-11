---
title: Set column width to scalable unit like em or percent
type: docs
weight: 130
url: /net/set-column-width-to-scalable-unit-like-em-or-percent/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Generating an HTML file from a spreadsheet is very common. The size of the columns is defined in **pt**, which works in many cases. However, there may be a case where this fixed size is not required. For example, if the container panel width is 600 px where this HTML page is displayed, you may get a horizontal scrollbar if the generated table width is larger. It is required that this fixed size be changed to a scalable unit such as **em** or **percent** for better presentation. The following sample code can be used where [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) is set to **true** for creating scalable width.

Sample source file and output files can be downloaded from the following links:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
