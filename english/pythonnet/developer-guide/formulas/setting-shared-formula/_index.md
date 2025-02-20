---
title: Setting Shared Formula
type: docs
weight: 10
url: /python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

If you want to add a function in worksheet which will do some calculations. This article explains how to achieve this task using Aspose.Cells for Python via .NET.

{{% /alert %}}

## Setting Shared Formula using Aspose.Cells for Python via .NET

Suppose you have a worksheet filled with data in the format that looks like the following sample worksheet.

|**Input file with one column or data**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

You want to add a function in B2 that will calculate the sales tax for the first row of data. The tax is **9%**. The formula that calculates the sales tax is: **"=A2*0.09"**. This article explains how to apply this formula with Aspose.Cells for Python via .NET.

Aspose.Cells for Python via .NET lets you specify a formula using the [**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) property. There are two options for adding formulas to the other cells (B3, B4, B5, and so on) in the column.

Either do what you did for the first cell, effectively setting the formula for each cell, updating the cell reference accordingly (A3*0.09, A4*0.09, A5*0.09 and so on). This requires the cell references for each row to be updated. It also requires Aspose.Cells for Python via .NET to parse each formula individually, which can be time-consuming for large spreadsheets and complex formulas. It also adds extra lines of codes although loops can cut them down somewhat.

Another approach is to use a **shared formula**. With a shared formula, the formulas are automatically updated for the cell references in each row so that the tax would be calculated properly. The [**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) method is more efficient than the first method.

The following example demonstrates how to use it.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

