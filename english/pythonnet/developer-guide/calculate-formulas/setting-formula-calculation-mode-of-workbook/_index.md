---
title: Setting Formula Calculation Mode of Workbook with Python.NET
linktitle: Setting Formula Calculation Mode of Workbook
type: docs
weight: 110
url: /python-net/setting-formula-calculation-mode-of-workbook/
description: Learn how to set formula calculation mode (automatic, manual) in Excel workbooks using Aspose.Cells for Python via .NET API. Step-by-step guide with code examples.
keywords: Python, Aspose.Cells, Excel, workbook, formula calculation mode, automatic, manual, settings
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Setting Formula Calculation Mode in Workbook**

{{% alert color="primary" %}}

Microsoft Excel provides three formula calculation modes:
- **Automatic**: Recalculates formulas on every change and workbook open
- **Automatic except for data tables**: Recalculates formulas except data tables on changes
- **Manual**: Only recalculates when user requests (F9/CTRL+ALT+F9) or during save

{{% /alert %}}

### **Setting Calculation Mode with Aspose.Cells**

Aspose.Cells for Python via .NET provides the [**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/) configuration through the [**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/) property. Use the [**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/) attribute to control calculation behavior.

Available modes via [**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/) enum:
- `AUTOMATIC`
- `AUTOMATIC_EXCEPT_TABLE`
- `MANUAL`

**Implementation Steps:**
1. Load existing workbook or create new instance
2. Access workbook settings
3. Set calculation mode using `formula_settings.calculation_mode`
4. Save modified workbook

```python
from aspose.cells import Workbook, CalcModeType

# Load source workbook
workbook = Workbook("source.xlsx")

# Configure manual calculation mode
workbook.settings.formula_settings.calculation_mode = CalcModeType.MANUAL

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CalcModeType, SaveFormat

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create a workbook
workbook = Workbook()

# Set the Formula Calculation Mode to Manual
workbook.settings.formula_settings.calculation_mode = CalcModeType.MANUAL

# Save the workbook
output_path = os.path.join(data_dir, "output_out.xlsx")
workbook.save(output_path, SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}
