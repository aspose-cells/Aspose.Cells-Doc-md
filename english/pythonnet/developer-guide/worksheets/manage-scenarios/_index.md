---
title: Create, Manipulate, or Remove Scenarios from Worksheets with Python via .NET
linktitle: Manage Scenarios
type: docs
weight: 190
url: /python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Learn how to create, modify, and delete scenarios in Excel worksheets programmatically using Aspose.Cells for Python via .NET API.
keywords: Python Excel scenarios, manage worksheet scenarios Python, add scenario Python, remove scenario Excel Python, modify scenarios Python
---

{{% alert color="primary" %}}

Sometimes you need to create, manipulate, or delete scenarios in spreadsheets. A scenario is a named 'what if?' model that includes variable input cells linked by one or more formulas. Before creating a scenario, design the worksheet so it contains at least one formula that depends on cells which can accept different values. This example demonstrates how to manage scenarios in worksheets using Aspose.Cells for Python via .NET.

{{% /alert %}}

Aspose.Cells provides several classes for working with scenarios:
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

Use the [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/) property to access scenarios. The following code demonstrates how to:
1. Open an Excel file containing scenarios
2. Remove an existing scenario
3. Add a new scenario
4. Save the modified workbook

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate the Workbook and load an Excel file
workbook = Workbook(os.path.join(data_dir, "aspose-sample.xlsx"))
# Access first worksheet
worksheet = workbook.worksheets[0]

if len(worksheet.scenarios) > 0:
    # Remove the existing first scenario from the sheet
    worksheet.scenarios.remove_at(0)

    # Create a scenario
    i = worksheet.scenarios.add("MyScenario")
    # Get the scenario
    scenario = worksheet.scenarios[i]
    # Add comment to it
    scenario.comment = "Test sceanrio is created."
    # Get the input cells for the scenario
    sic = scenario.input_cells
    # Add the scenario on B4 (as changing cell) with default value
    sic.add(3, 1, "1100000")

    output_path = os.path.join(data_dir, "outBk_scenarios1.out.xlsx")

    # Save the Excel file
    workbook.save(output_path)
    print(f"\nProcess completed successfully.\nFile saved at {output_path}")
```

```python
import clr
clr.AddReference("Aspose.Cells")
from Aspose.Cells import Workbook, SaveFormat

# Load source workbook
workbook = Workbook("scenarios.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Remove existing scenario by index
worksheet.scenarios.remove_at(0)

# Add new scenario
scenario_index = worksheet.scenarios.add("New Scenario")
scenario = worksheet.scenarios[scenario_index]

# Set scenario input cells
scenario.input_cells.add(0, 0, "B1")
scenario.input_cells.add(0, 1, "B2")

# Save modified workbook
workbook.save("output.xlsx", SaveFormat.XLSX)
```

**Key modifications:**
- Method names converted to snake_case (RemoveAt → remove_at)
- Property access using Python-style dot notation
- Added Python.NET assembly reference
- Used Python import statements
- Maintained original functionality with Python syntax
- Updated documentation links to Python.NET references

**Note:** When working with scenarios in Python.NET:
- Scenario indices are zero-based
- Input cells are specified using (row, column) coordinates
- Always validate scenario existence before removal
- Use SaveFormat enum for output file format specification