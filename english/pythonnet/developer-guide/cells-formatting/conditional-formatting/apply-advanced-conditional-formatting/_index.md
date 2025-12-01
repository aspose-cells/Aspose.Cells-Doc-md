---
title: Apply Advanced Conditional Formatting with Python.NET
linktitle: Apply Advanced Conditional Formatting
type: docs
weight: 70
url: /python-net/apply-advanced-conditional-formatting/
description: Learn how to implement Excel's advanced conditional formatting features like data bars, color scales, and icon sets using Aspose.Cells for Python via .NET.
keywords: Python Excel formatting, Conditional formatting Python, Data bars Python, Color scales Python, Icon sets Python, Aspose.Cells Python
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 and later versions (2010/2013/2016) provide advanced conditional formatting features including cell shading, borders, colored icons, arrows, flags, and font formatting.

{{% /alert %}} 

## **Implement Advanced Conditional Formatting in Excel Files**
Aspose.Cells for Python via .NET supports all advanced conditional formatting features including:

- Add shaded data bars to graphically enhance the underlying numbers by embedding a simple bar chart in the cells.
- Automatically shade cells with color scales based on their relation to values in other cells in the range. The default settings shades the lowest value in red moving up to the highest value in green.
- Use icon sets in a similar way to color scales, but rather than shading the cells it adds small icons, such as arrows and traffic lights to the cells.

Aspose.Cells fully supports the conditional formatting provided by Microsoft Excel 2007 and later versions in XLSX format on cells at runtime. This example demonstrates an exercise for advanced conditional formatting types including IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom and other rules with different sets of attributes.

- [**Adding Color Scale Conditional Formattings**](/cells/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/python-net/how-to-add-top10-conditional-formatting/)



### **Calculate Excel's Color Selection for Color Scale Formatting**
This code shows how to determine the color chosen by Excel for ColorScale conditional formatting rules:

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}
