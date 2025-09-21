---
title: Set column width to scalable unit like em or percent with Golang via C++
linktitle: Set column width to scalable unit like em or percent
type: docs
weight: 130
url: /go-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Learn how to set column width to scalable units like em or percent using Aspose.Cells for C++.
---

Generating an HTML file from a spreadsheet is very common. The size of the columns is defined in "pt" which works in many cases. However, there can be a case where this fixed size may not be required. For example, if a container panel width is 600px where this HTML page is being displayed. In this case, you may get a horizontal scrollbar if the generated table width is bigger. It was required that this fixed size shall be changed into a scalable unit like em or percent to get a better presentation. Following sample code can be used where [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getwidthscalable/) is set to **true** for creating scalable width.

Sample source file and output files can be downloaded from the following links:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetColumnWidthToScalableUnitLikeEmOrPercent.go" >}}