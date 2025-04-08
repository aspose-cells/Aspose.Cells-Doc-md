---
title: Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells with Python.NET
linktitle: Implement Custom Calculation Engine
type: docs
weight: 80
url: /python-net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
description: Learn how to extend Excel's calculation engine by implementing custom formulas using Aspose.Cells for Python via .NET. Modify formula results programmatically with Python code examples.
keywords: Python, Aspose.Cells, Excel, custom calculation engine, extend engine, formula calculation
---

## **Implement Custom Calculation Engine**

Aspose.Cells for Python via .NET has a powerful calculation engine that can calculate almost all Microsoft Excel formulas. Additionally, it allows you to extend the default calculation engine for enhanced flexibility.

The following property and classes are used in this implementation:

- [**CalculationOptions.custom_engine**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/#custom_engine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/python-net/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationdata/)

The code below implements a custom calculation engine by subclassing [**AbstractCalculationEngine**](https://reference.aspose.com/cells/python-net/aspose.cells/abstractcalculationengine/). It overrides the [**calculate**](https://reference.aspose.com/cells/python-net/aspose.cells/abstractcalculationengine/calculate/) method to modify the **TODAY** function, adding one day to the system date. For example, if today is 2023-07-27, the custom engine returns 2023-07-28.

### **Python Code Example**

```python
import datetime
from aspose.cells import Workbook, AbstractCalculationEngine, CellsHelper, CalculationOptions

class CustomEngine(AbstractCalculationEngine):
    def calculate(self, data):
        if data.function_name.upper() == "TODAY":
            today = datetime.datetime.today()
            double_value = CellsHelper.get_double_from_date(today) + 1.0
            data.calculated_value = double_value
    
    @property
    def process_built_in_functions(self):
        return True

def run():
    workbook = Workbook()
    sheet = workbook.worksheets[0]
    
    a1 = sheet.cells.get("A1")
    style = a1.get_style()
    style.number = 14
    a1.set_style(style)
    
    a1.formula = "=TODAY()"
    
    workbook.calculate_formula()
    print(f"The value of A1 with default calculation engine: {a1.string_value}")
    
    engine = CustomEngine()
    opts = CalculationOptions()
    opts.custom_engine = engine
    
    workbook.calculate_formula(opts)
    print(f"The value of A1 with custom calculation engine: {a1.string_value}")

if __name__ == "__main__":
    run()
```

### **Result**

When running the code, the value in cell A1 calculated with the custom engine will be one day later than the default calculation result. Check the console output to verify:

```
Value of A1 without custom engine: 07/27/2023 00:00:00
Value of A1 with custom engine: 07/28/2023 00:00:00
```

### **Related Article**

{{% alert color="primary" %}}

[Direct calculation of custom function without writing it in a worksheet](/cells/python-net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}