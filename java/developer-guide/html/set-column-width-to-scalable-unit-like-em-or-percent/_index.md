---
title: Set column width to scalable unit like em or percent
type: docs
weight: 130
url: /java/set-column-width-to-scalable-unit-like-em-or-percent/
---

Generating an HTML file from a spreadsheet is very common. The size of the columns is defined in "pt" which works in many cases. However, there can be a case where this fixed size may not be required. For example, if the container panel width is 600px where this HTML page is being displayed. In this case, you may get a horizontal scrollbar if the generated table width is bigger. It was required that this fixed size shall be changed into a scalable unit like em or percent to get a better presentation. Following sample code can be used where [HtmlSaveOptions.WidthScalable](https://apireference.aspose.com/javascript/cells/aspose.cells/htmlsaveoptions#WidthScalable) is set to **true** for creating scalable width.

Sample source file and output files can be downloaded from the following links:

[sampleForScalableColumns.xlsx](attachments/74580174/74776596.xlsx)

[outsampleForScalableColumns.zip](attachments/74580174/74776597.zip)

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "HTML-SetScalableColumnWidth.java" >}}
