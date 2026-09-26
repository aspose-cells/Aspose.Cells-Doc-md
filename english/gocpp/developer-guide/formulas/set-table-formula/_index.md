---
title: Propagate Formula in Table or List Object automatically while entering data in new rows with Golang via C++
linktitle: Sets Table Formula
type: docs
weight: 260
url: /go-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Learn how to propagate formulas in tables or list objects automatically when entering new data using Aspose.Cells for Go via C++.
---

## **Possible Usage Scenarios**
Sometimes, you want a formula in your Table or List Object to automatically propagate to new rows while entering new data. This is the default behavior of Microsoft Excel. To achieve the same functionality with Aspose.Cells, use the [ListColumn::GetFormula](https://reference.aspose.com/cells/go-cpp/listcolumn/getformula/) method.

## **Propagate Formula in Table or List Object automatically while entering data in new rows**
The following sample code creates a Table or List Object in such a way that the formula in column B will automatically propagate to new rows when you enter new data. Please check the [output Excel file](5115469.xlsx) generated with this code. If you enter any number in cell A3, you will see that the formula in cell B2 automatically propagates to cell B3.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTableFormula.go" >}}
{{< app/cells/assistant language="go" >}}
