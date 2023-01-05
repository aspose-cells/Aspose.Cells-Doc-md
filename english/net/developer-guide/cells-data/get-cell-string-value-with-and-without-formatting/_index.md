---
title: Get Cell String Value with and without Formatting
type: docs
weight: 240
url: /net/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells provides a method [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) which can be used to get the string value of the cell with or without any formatting. Suppose, you have a cell with value 0.012345 and you have formatted it to display two decimal places only. It will then display as 0.01 in Excel. You can retrieve string values both as 0.01 and as 0.012345 using the [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) method. It takes [**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) enum as a parameter which has the following values

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

The following sample code explains the use of [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) method.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
