---
title: Implement Subtotal or Grand Total Labels in Other Languages with Python.NET
linktitle: Implement Subtotal or Grand Total Labels in Other Languages
type: docs
weight: 50
url: /python-net/implement-subtotal-or-grand-total-labels-in-other-languages/
description: Learn how to customize subtotal and grand total labels in various languages using Aspose.Cells for Python via .NET.
---

## **Possible Usage Scenarios**

You may need to display subtotal and grand total labels in non-English languages like Chinese, Japanese, Arabic, or Hindi. Aspose.Cells for Python via .NET enables this through the [**GlobalizationSettings**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings) class and [**Workbook.settings.globalization_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/#globalization_settings) property. For related implementations, see:

- [Using GlobalizationSettings Class for Custom Subtotal Labels and Other Label of Pie Chart](/cells/python-net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implement Subtotal or Grand Total Labels in Other Languages**

The following example demonstrates how to load a [sample Excel file](5115151.xlsx) and implement subtotal/grand total labels in Chinese. The resulting [output Excel file](5115152.xlsx) shows the localized labels.

### **Custom GlobalizationSettings Implementation**
Create a custom class inheriting from `GlobalizationSettings` to override label formatting:

```python
from aspose.cells import GlobalizationSettings, ConsolidationFunction

class GlobalizationSettingsImp(GlobalizationSettings):
    # This function will return the sub total name
    def get_total_name(self, function_type: ConsolidationFunction) -> str:
        return "Chinese Total - 可能的用法"
    
    # This function will return the grand total name
    def get_grand_total_name(self, function_type: ConsolidationFunction) -> str:
        return "Chinese Grand Total - 可能的用法"
```

### **Applying Custom Localization**
Use the custom settings in your workbook processing:

```python
import os
from aspose.cells import Workbook, GlobalizationSettings, CellArea, ConsolidationFunction

class GlobalizationSettingsImp(GlobalizationSettings):
    def get_sub_total_name(self, sub_total_type):
        return "My SubTotal"
    
    def get_grand_total_name(self, function_type):
        return "My Grand Total"

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Load source workbook
wb = Workbook(os.path.join(data_dir, "sample.xlsx"))

# Set globalization settings for custom subtotal/grand total names
gsi = GlobalizationSettingsImp()
wb.settings.globalization_settings = gsi

# Access first worksheet
ws = wb.worksheets[0]

# Apply subtotal on A1:B10
ca = CellArea.create_cell_area("A1", "B10")
ws.cells.subtotal(ca, 0, ConsolidationFunction.SUM, [2, 3, 4])

# Set first column width
ws.cells.set_column_width(0, 40)

# Save output file
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb.save(os.path.join(output_dir, "output_out.xlsx"))
```