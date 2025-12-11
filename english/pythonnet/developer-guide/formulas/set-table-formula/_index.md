---
title: Propagate Formula in Table or List Object automatically while entering data in new rows
linktitle: Sets Table Formula
type: docs
weight: 260
url: /python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Sometimes, you want a formula in your Table or List Object to automatically propagate to new rows while entering new data. This is the default behavior of Microsoft Excel. In order to achieve the same thing with Aspose.Cells for Python via .NET, please use [**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula) property.

## **Propagate Formula in Table or List Object automatically while entering data in new rows**
The following sample code creates a Table or List Object in such a way that the formula in column B will automatically propagate to new rows when you enter new data. Please check the [output Excel file](5115469.xlsx) generated with this code. If you enter any number in cell A3, you will see the formula in cell B2 automatically propagates to cell B3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
