---
title: Propagate Formula in Table or List Object automatically while entering data in new rows
type: docs
weight: 260
url: /net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Possible Usage Scenarios**
Sometimes, you want a formula in your Table or List Object automatically propagates to new rows while entering new data. This is the default behavior of Microsoft Excel. In order to achieve the same thing with Aspose.Cells, please use [ListColumn.Formula](https://apireference.aspose.com/net/cells/aspose.cells.tables/listcolumn/properties/formula) property.
## **Propagate Formula in Table or List Object automatically while entering data in new rows**
The following sample code creates a Table or List Object in such a way that the formula in column B will automatically propagate to new rows when you will enter new data. Please check the [output excel file](5115469.xlsx) generated with this code. If you enter any number in cell A3, you will see, the formula in cell B2 automatically propagates to cell B3.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
