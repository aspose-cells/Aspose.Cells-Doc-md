---
title: Set column width to scalable unit like em or percent
type: docs
weight: 130
url: /net/set-column-width-to-scalable-unit-like-em-or-percent/
---

Generating an HTML file from a spreadsheet is very common. The size of the columns is defined in "pt" which works in many cases. However, there can be a case where this fixed size may not be required. For example, if a container panel width is 600px where this HTML page is being displayed. In this case, you may get a horizontal scrollbar if the generated table width is bigger. It was required that this fixed size shall be changed into a scalable unit like em or percent to get a better presentation. Following sample code can be used where [**HtmlSaveOptions.WidthScalable**](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) is set to **true** for creating scalable width.

Sample source file and output files can be downloaded from the following links:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
