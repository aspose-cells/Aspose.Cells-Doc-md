---
title: Returning a Range of Values using AbstractCalculationEngine with Python.NET
linktitle: Returning a Range of Values using AbstractCalculationEngine
description: Learn how to implement custom Excel calculations returning value ranges using Aspose.Cells for Python via .NET API.
type: docs
weight: 55
url: /python-net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells provides [**AbstractCalculationEngine**](https://reference.aspose.com/cells/python-net/aspose.cells/abstractcalculationengine) class which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

This article will explain how to return the range of values from [**AbstractCalculationEngine**](https://reference.aspose.com/cells/python-net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

The following code demonstrates the use of the [**AbstractCalculationEngine**](https://reference.aspose.com/cells/python-net/aspose.cells/abstractcalculationengine) class and returns the range of values via its method.

Create a class with a function *calculate_custom_function*. This class implements [**AbstractCalculationEngine**](https://reference.aspose.com/cells/python-net/aspose.cells/abstractcalculationengine).

```python
from aspose.cells import AbstractCalculationEngine
from datetime import datetime

class CustomFunctionStaticValue(AbstractCalculationEngine):
    def calculate(self, data):
        data.calculated_value = [
            [datetime(2015, 6, 12, 10, 6, 30), 2],
            [3.0, "Test"]
        ]
```

Now use above function in your Python program:


```python
import os
from aspose.cells import Workbook, CalcModeType, CalculationOptions, CustomFunctionStaticValue

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook
workbook = Workbook()
cells = workbook.worksheets[0].cells

# Set formula
cell = cells.get(0, 0)
cell.set_array_formula("=MYFUNC()", 2, 2)

style = cell.get_style()
style.number = 14
cell.set_style(style)

# Set calculation options for formula
calculation_options = CalculationOptions()
calculation_options.custom_engine = CustomFunctionStaticValue()
workbook.calculate_formula(calculation_options)

# Save to xlsx by setting the calc mode to manual
workbook.settings.formula_settings.calculation_mode = CalcModeType.MANUAL
workbook.save(os.path.join(data_dir, "output_out.xlsx"))

# Save to pdf
workbook.save(os.path.join(data_dir, "output_out.pdf"))
```