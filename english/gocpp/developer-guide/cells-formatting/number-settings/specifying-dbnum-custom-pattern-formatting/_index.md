---
title: Specifying DBNum Custom Pattern Formatting with Golang via C++
linktitle: Specifying DBNum Custom Pattern Formatting
description: Aspose.Cells is a C++ library for working with spreadsheet files that supports formatting dates and numbers using custom formatting patterns. This article will show you how to use the Aspose.Cells library to specify the 'dbnum' custom format pattern so that users have more control over how numbers are displayed.
keywords: Aspose.Cells, C++ library, electronic spreadsheet, custom format pattern, formatting, 'dbnum', control display
type: docs
weight: 110
url: /go-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Possible Usage Scenarios**

Aspose.Cells supports the *DBNum* custom pattern formatting. For example, if your cell value is 123 and you specify its custom formatting as [DBNum2][$-804]General then it will be displayed like 壹佰贰拾叁. You can specify your custom formatting of the cell using [**Cell.GetStyle()**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) method and [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) property.

## **Sample Code**

The following sample code illustrates how to specify *DBNum* custom pattern formatting. Please check its [output PDF](43352081.pdf) for more help.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-SpecifyingDbnumCustomPatternFormatting.go" >}}