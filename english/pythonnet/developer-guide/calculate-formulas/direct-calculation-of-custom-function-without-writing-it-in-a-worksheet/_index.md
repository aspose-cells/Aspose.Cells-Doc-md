---
title: Direct Calculation of Custom Function without Writing in Worksheet with Python.NET
linktitle: Direct Calculation of Custom Function
type: docs
weight: 90
url: /python-net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
description: Learn how to calculate custom Excel functions programmatically using Python.NET without worksheet implementation. Leverage Aspose.Cells for direct formula evaluation.
keywords: python excel custom functions, python calculate formula, aspose.cells python calculation, python spreadsheet automation
---

## **Direct Calculation of Custom Function Without Writing in Worksheet**

This topic explains how to directly calculate custom functions without first writing them in a worksheet using the [**Worksheet.calculate_formula(formula, opts)**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/calculate_formula/) method.

### **Implementation Example**

The following sample demonstrates calculating a custom `MyCompany.custom_function()` that returns "Aspose.Cells.". This value is concatenated with cell A1's value ("Welcome to ") to produce "Welcome to Aspose.Cells." without writing the function in the worksheet.

```python
from aspose.cells import Workbook, CalculationOptions, AbstractCalculationEngine

class ICustomEngine(AbstractCalculationEngine):
    # Override the Calculate method with custom logic
    def calculate(self, data):
        # Check the forumla name and calculate it yourself
        if data.function_name == "MyCompany.CustomFunction":
            # This is our calculated value
            data.calculated_value = "Aspose.Cells."

def run():
    # Create a workbook
    wb = Workbook()

    # Access first worksheet
    ws = wb.worksheets[0]

    # Add some text in cell A1
    ws.cells.get("A1").put_value("Welcome to ")

    # Create calculation options with custom engine
    opts = CalculationOptions()
    opts.custom_engine = ICustomEngine()

    # Calculate custom formula directly
    ret = ws.calculate_formula("=A1 & MyCompany.CustomFunction()", opts)

    # Print the calculated value
    print("Calculated Value:", ret)
```

### **Console Output**

{{< highlight python >}}
Calculated Value: Welcome to Aspose.Cells.
{{< /highlight >}}

### **Related Article**

{{% alert color="primary" %}}
[Implement Custom Calculation Engine to Extend Default Engine in Python](/cells/python-net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
{{% /alert %}}