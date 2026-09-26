---
title: Setting Shared Formula with Golang via C++
linktitle: Setting Shared Formula
type: docs
weight: 10
url: /go-cpp/setting-shared-formula/
description: Learn how to set shared formulas in Excel worksheets using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

If you want to add a function in a worksheet that will perform calculations, this article explains how to achieve this task using Aspose.Cells.

{{% /alert %}}

## Setting Shared Formula using Aspose.Cells

Suppose you have a worksheet filled with data in a format that looks like the following sample worksheet.

|**Input file with one column of data**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

You want to add a function in B2 that will calculate the sales tax for the first row of data. The tax is **9%**. The formula that calculates the sales tax is: **"=A2*0.09"**. This article explains how to apply this formula with Aspose.Cells.

Aspose.Cells lets you specify a formula using the [**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/) property. There are two options for adding formulas to the other cells (B3, B4, B5, and so on) in the column.

Either repeat what you did for the first cell, effectively setting the formula for each cell and updating the cell reference accordingly (A3*0.09, A4*0.09, A5*0.09, and so on). This requires the cell references for each row to be updated. It also requires Aspose.Cells to parse each formula individually, which can be time‑consuming for large spreadsheets and complex formulas. It also adds extra lines of code, although loops can cut them down somewhat.

Another approach is to use a **shared formula**. With a shared formula, the formulas are automatically updated for the cell references in each row so that the tax is calculated properly. The [**SetSharedFormula**](https://reference.aspose.com/cells/go-cpp/cell/setsharedformula_string_int_int/) method is more efficient than the first method.

The following example demonstrates how to use it.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingSharedFormula.go" >}}
{{< app/cells/assistant language="go" >}}
