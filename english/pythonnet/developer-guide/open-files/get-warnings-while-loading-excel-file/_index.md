---
title: Get Warnings while Loading Excel File with Python.NET
linktitle: Get Warnings while Loading Excel File
type: docs
weight: 110
url: /python-net/get-warnings-while-loading-excel-file/
description: Learn how to handle spreadsheet loading warnings programmatically using Aspose.Cells for Python via .NET with code examples.
---

## **Possible Usage Scenarios**

Sometimes the user tries to load a workbook that is somewhat corrupt but still loadable. In such cases, Aspose.Cells throws warnings while loading the workbook. You can catch these warnings by implementing the [**IWarningCallback**](https://reference.aspose.com/cells/python-net/aspose.cells/iwarningcallback) abstract base class and setting the [**LoadOptions.warning_callback**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/warning_callback/) property.

## **Get Warnings while Loading Excel File**

The following sample code explains how to get warnings while loading an Excel file. The code loads the [sample excel file](sampleDuplicateDefinedName.xlsx) which throws a [**DUPLICATE_DEFINED_NAME**](https://reference.aspose.com/cells/python-net/aspose.cells/warningtype/) warning on loading. This warning is then caught by the [**IWarningCallback.warning()**](https://reference.aspose.com/cells/python-net/aspose.cells/iwarningcallback/warning/) method that prints the warning messages to the console. The code then saves the workbook as an [output excel file](outputDuplicateDefinedName.xlsx). If you open the sample Excel file in Microsoft Excel, it will also display this warning as shown in the screenshot below.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Sample Code**

```python
import aspose.cells as cells

class WarningCallback(cells.IWarningCallback):
    def warning(self, warning_info):
        if warning_info.warning_type == cells.WarningType.DUPLICATE_DEFINED_NAME:
            print(f"Duplicate Defined Name Warning: {warning_info.description}")

# Create load options and set warning callback
load_options = cells.LoadOptions()
load_options.warning_callback = WarningCallback()

# Load workbook with warnings
workbook = cells.Workbook("sampleDuplicateDefinedName.xlsx", load_options)

# Save output file
workbook.save("outputDuplicateDefinedName.xlsx")
```

```python
import os
from aspose.cells import IWarningCallback, WarningType, LoadOptions, Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

class WarningCallback(IWarningCallback):
    def warning(self, warning_info):
        if warning_info.warning_type == WarningType.DUPLICATE_DEFINED_NAME:
            print("Duplicate Defined Name Warning: " + warning_info.description)

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create load options and set the warning_callback property
options = LoadOptions()
options.warning_callback = WarningCallback()

# Load the source excel file
book = Workbook(os.path.join(data_dir, "sampleDuplicateDefinedName.xlsx"), options)

# Save the workbook
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
book.save(os.path.join(output_dir, "outputDuplicateDefinedName.xlsx"))
```

## **Console Output**

Here is the console output of the above code when executed with the provided [sample excel file](sampleDuplicateDefinedName.xlsx).

```text
Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17
Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228
Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16
```