---
title: Get Cell String Value with and without Formatting with Golang via C++
linktitle: Get Cell String Value
type: docs
weight: 240
url: /go-cpp/get-cell-string-value-with-and-without-formatting/
description: Learn how to Get Cell String Value with and without Formatting through the Aspose.Cells for C++ API.
keywords: Get Cell String Value with and without Formatting, Retrieve Cell String Value with and without Formatting, Obtain Cell String Value with and without Formatting
---

{{% alert color="primary" %}}

Aspose.Cells provides a method [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) which can be used to get the string value of the cell with or without any formatting. Suppose, you have a cell with value 0.012345 and you have formatted it to display two decimal places only. It will then display as 0.01 in Excel. You can retrieve string values both as 0.01 and as 0.012345 using the [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) method. It takes [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) enum as a parameter which has the following values:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

The following sample code explains the use of [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}