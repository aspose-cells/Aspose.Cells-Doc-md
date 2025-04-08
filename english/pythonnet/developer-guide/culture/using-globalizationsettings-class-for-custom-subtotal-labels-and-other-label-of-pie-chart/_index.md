---
title: Using GlobalizationSettings Class for Custom Subtotal Labels and Pie Chart Labels with Python.NET
linktitle: Using GlobalizationSettings Class for Custom Labels
type: docs
weight: 70
url: /python-net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Learn how to customize subtotal labels and pie chart 'Other' labels using Aspose.Cells for Python via .NET's GlobalizationSettings class.
---

## **Possible Usage Scenarios**

Aspose.Cells API provides the [**GlobalizationSettings**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings) class to handle scenarios requiring custom subtotal labels in spreadsheets. This class also allows modification of the **Other** label in Pie charts during rendering.

## **Introduction to GlobalizationSettings Class**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings) class offers these key methods to override for label customization:

1. [**get_total_name**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings/get_total_name/): Gets the total name of the function
2. [**get_grand_total_name**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings/get_grand_total_name/): Gets the grand total name
3. [**get_other_name**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings/get_other_name/): Gets the "Other" label text for Pie charts

### **Custom Subtotal Labels**

Customize subtotal labels by overriding methods in a **GlobalizationSettings** subclass:

```python
from aspose.cells import GlobalizationSettings, ConsolidationFunction

class CustomSettings(GlobalizationSettings):
    def get_total_name(self, function_type):
        if function_type == ConsolidationFunction.AVERAGE:
            return "AVG"
        else:
            return super().get_total_name(function_type)
    
    def get_grand_total_name(self, function_type):
        if function_type == ConsolidationFunction.AVERAGE:
            return "GRD AVG"
        else:
            return super().get_grand_total_name(function_type)
```

Set the custom settings before adding subtotals:

```python
import os
from aspose.cells import Workbook, CellArea, ConsolidationFunction
from aspose.cells import GlobalizationSettings

# Define CustomSettings class inheriting from GlobalizationSettings
class CustomSettings(GlobalizationSettings):
    def get_sub_total_name(self, sub_total_type):
        return "Average"  # Simplified implementation for demonstration
    
    # Override other required methods from GlobalizationSettings here

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Loads an existing spreadsheet containing some data
book = Workbook(os.path.join(data_dir, "sample.xlsx"))

# Assigns the GlobalizationSettings property of the WorkbookSettings class
book.settings.globalization_settings = CustomSettings()

# Accesses the 1st worksheet from the collection
sheet = book.worksheets[0]

# Adds Subtotal of type Average to the worksheet
sheet.cells.subtotal(CellArea.create_cell_area("A2", "B9"), 0, ConsolidationFunction.AVERAGE, [1])

# Calculates Formulas
book.calculate_formula()

# Auto fits all columns
sheet.auto_fit_columns()

# Saves the workbook on disc
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

book.save(os.path.join(output_dir, "output_out.xlsx"))
```

{{% alert color="primary" %}} 
The [**GlobalizationSettings**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings) class only affects new subtotals. Existing subtotal labels cannot be modified.
{{% /alert %}}

### **Custom 'Other' Label for Pie Charts**

Override **get_other_name** to customize Pie chart labels:

```python
import locale
from aspose.cells.charts import ChartGlobalizationSettings

class GlobalCustomSettings(ChartGlobalizationSettings):
    def get_other_name(self) -> str:
        current_lang, _ = locale.getlocale()
        if current_lang is None:
            current_lang = ""
        if current_lang.startswith('en'):
            return "Other"
        elif current_lang.startswith('fr'):
            return "Autre"
        elif current_lang.startswith('de'):
            return "Andere"
        else:
            return super().get_other_name()
```

Apply custom settings when rendering charts:

```python
import os
from aspose.cells import Workbook, ImageOrPrintOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Loads an existing spreadsheet containing a pie chart
book = Workbook(os.path.join(data_dir, "sample.xlsx"))

# Assigns the GlobalizationSettings property of the WorkbookSettings class to the class created in first step
book.settings.globalization_settings.chart_settings = GlobalCustomSettings()

# Accesses the 1st worksheet from the collection which contains pie chart
sheet = book.worksheets[0]

# Accesses the 1st chart from the collection
chart = sheet.charts[0]

# Refreshes the chart
chart.calculate()

# Renders the chart to image
chart.to_image(os.path.join(data_dir, "output_out.png"), ImageOrPrintOptions())
```