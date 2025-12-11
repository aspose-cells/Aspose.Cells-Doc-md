---
title: Using FormulaText Function in Aspose.Cells with Python.NET
linktitle: Using FormulaText Function
type: docs
weight: 60
url: /python-net/using-formulatext-function-in-aspose-cells/
description: Learn how to work with Excel's FORMULATEXT function using Aspose.Cells for Python via .NET. Get and set cell formulas programmatically while maintaining spreadsheet integrity.
keywords: Aspose.Cells, Python, Excel, FORMULATEXT, formula handling, spreadsheet automation
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

FORMULATEXT is an Excel 2013 and later function. It is not supported by previous versions such as Excel 2010 or 2007, etc. As its name suggests, it displays the formula text contained in a specified cell. This article demonstrates how to use this function with Aspose.Cells for Python via .NET.

{{% /alert %}} 

The following sample code demonstrates using FORMULATEXT with Aspose.Cells. The code first writes a formula in cell A1 and then displays the formula text using FORMULATEXT in cell A2.

```python
from aspose.cells import Workbook

# Create a workbook object
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Put a formula in cell A1
cell_a1 = worksheet.cells.get("A1")
cell_a1.formula = "=Sum(B1:B10)"

# Get the text of the formula in cell A2 using the FORMULATEXT function
cell_a2 = worksheet.cells.get("A2")
cell_a2.formula = "=FormulaText(A1)"

# Calculate the workbook
workbook.calculate_formula()

# Print the results of A2. It will now print the text of the formula inside cell A1
print(cell_a2.string_value)
```

## **Console Output**
Here is the console output of the above sample code:

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
