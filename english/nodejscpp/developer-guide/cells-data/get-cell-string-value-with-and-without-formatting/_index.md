---
title: Get Cell String Value with and without Formatting
type: docs
weight: 240
url: /nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: Learn how to get cell string value with and without formatting through the Aspose.Cells for Node.js via C++ API.
keywords: Get Cell String Value with and without Formatting Node.js via C++, Retrieve Cell String Value with and without Formatting Node.js via C++, Obtain Cell String Value with and without Formatting Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells provides a method [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) which can be used to get the string value of the cell with or without any formatting. Suppose, you have a cell with value 0.012345 and you have formatted it to display two decimal places only. It will then display as 0.01 in Excel. You can retrieve string values both as 0.01 and as 0.012345 using the [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) method. It takes [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) enum as a parameter which has the following values

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

The following sample code explains the use of [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue) method.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

