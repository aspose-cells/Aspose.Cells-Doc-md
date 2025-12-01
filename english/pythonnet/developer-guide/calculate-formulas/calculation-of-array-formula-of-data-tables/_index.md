---
title: Calculation of Array Formula of Data Tables with Python.NET
linktitle: Calculation of Array Formula of Data Tables
type: docs
weight: 70
url: /python-net/calculation-of-array-formula-of-data-tables/
description: Learn how to calculate array formulas for Excel data tables using Aspose.Cells for Python via .NET API. Modify and save spreadsheets programmatically.
keywords: Python Excel Data Tables, Python Array Formulas, Aspose.Cells Python, Calculate Data Tables Python, Excel Automation Python
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can create Data Table in Microsoft Excel using Data > What-If Analysis > Data Table.... Aspose.Cells for Python via .NET allows you to calculate the array formula of a data table. Please use [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) as normal for calculating any type of formulas.

{{% /alert %}}

In the following example, we use the [source excel file](5115535.xlsx). If you change the value of cell B1 to 100, the values of the Data Table (highlighted in yellow) will update to 120 as shown in the screenshots below. The Python code generates this [output PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Below is the Python implementation demonstrating how to generate the [output PDF](5115538.pdf) from the [source excel file](5115535.xlsx):

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook from source excel file
workbook = Workbook(os.path.join(data_dir, "DataTable.xlsx"))

# Access first worksheet
worksheet = workbook.worksheets[0]

# When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.cells.get("B1").put_value(100)

# Calculate formula, now it also calculates Data Table array formula
workbook.calculate_formula()

# Save the workbook in pdf format
workbook.save(os.path.join(data_dir, "output_out.pdf"))
```

**Python Code Explanation:**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
{{< app/cells/assistant language="python-net" >}}
