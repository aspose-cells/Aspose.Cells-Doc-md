---
title: Load Specific Worksheets in a Workbook with Python.NET
linktitle: Load Specific Worksheets in a Workbook
type: docs
weight: 100
url: /python-net/load-specific-worksheets-in-a-workbook/
description: Learn how to optimize Excel workbook loading by loading specific worksheets using Aspose.Cells for Python via .NET. Improve performance and reduce memory usage.
---

{{% alert color="primary" %}}

By default, Aspose.Cells loads the whole spreadsheet into memory. Developers can load only specific sheets to improve performance and reduce memory consumption. This approach is particularly useful when working with large workbooks containing many worksheets.

{{% /alert %}}

```python
import os
from aspose.cells import Workbook, LoadOptions, LoadFormat, LoadFilter

class CustomLoad(LoadFilter):
    def __init__(self):
        super().__init__()
        self.sheets_in_loading_order = [0]  # Load first worksheet only

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Load the workbook with the specified worksheet only.
load_options = LoadOptions(LoadFormat.XLSX)
load_options.load_filter = CustomLoad()

# Create the workbook
workbook = Workbook(os.path.join(data_dir, "TestData.xlsx"), load_options)

# Perform your desired task

# Save the workbook
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "outputFile.out.xlsx"))
```

The following Python.NET code demonstrates how to implement the `CustomLoad` class:

```python
import aspose.cells as ac

class CustomLoad(ac.LoadFilter):
    def start_sheet(self, sheet):
        # Only load sheets named "Sheet1" or "Sheet2"
        if sheet.name in ["Sheet1", "Sheet2"]:
            return True
        return False

# Create load options with custom filter
load_options = ac.LoadOptions()
load_options.load_filter = CustomLoad()
load_options.load_data_filter_options = ac.LoadDataFilter.STRUCTURE

# Load workbook with filtered worksheets
workbook = ac.Workbook("large_workbook.xlsx", load_options)

# Access loaded worksheet
print(f"First loaded sheet: {workbook.worksheets[0].name}")
```

```python
from aspose.cells import LoadFilter, LoadDataFilterOptions, Worksheet

class CustomLoad(LoadFilter):
    def start_sheet(self, sheet: Worksheet):
        if sheet.name == "Sheet2":
            # Load everything from worksheet "Sheet2"
            self.load_data_filter_options = LoadDataFilterOptions.ALL
        else:
            # Load nothing
            self.load_data_filter_options = LoadDataFilterOptions.STRUCTURE
```

Key implementation details:
1. Inherit from `LoadFilter` abstract base class
2. Override `start_sheet` method with Python's snake_case naming
3. Use `LoadDataFilter.STRUCTURE` enum for data filtering
4. Implement conditional loading based on worksheet names
5. Use Python-style path handling and string comparisons

This approach significantly reduces memory usage when working with large Excel files by only loading specified worksheets while maintaining access to the workbook's structure.