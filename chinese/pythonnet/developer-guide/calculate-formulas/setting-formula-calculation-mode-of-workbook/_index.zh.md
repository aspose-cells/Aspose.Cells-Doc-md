---
title: 使用Python.NET设置Workbook的公式计算模式
linktitle: 设置工作簿的公式计算模式
type: docs
weight: 110
url: /zh/python-net/setting-formula-calculation-mode-of-workbook/
description: 学习如何使用Aspose.Cells for Python via .NET API设置Excel工作簿中的公式计算模式（自动、手动）。逐步指南附代码示例。
keywords: Python、Aspose.Cells、Excel、工作簿、公式计算模式、自动、手动、设置
---

## **在工作簿中设置公式计算模式**

{{% alert color="primary" %}}

 Microsoft Excel提供三种公式计算模式：
- **自动**：每次更改和打开工作簿时重新计算公式
- **除数据表外自动**：在更改时重新计算公式，除数据表外
- **手动**：仅在用户请求（F9/CTRL+ALT+F9）或保存时重新计算

{{% /alert %}}

### **使用Aspose.Cells设置计算模式**

Aspose.Cells for Python via .NET通过[**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/)属性提供[**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/)配置。使用[**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/)属性控制计算行为。

通过[**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/)枚举提供的可用模式：
- `AUTOMATIC`
- `AUTOMATIC_EXCEPT_TABLE`
- `MANUAL`

**实现步骤：**
1. 加载现有工作簿或创建新实例
2. 访问工作簿设置
3. 使用`formula_settings.calculation_mode`设置计算模式
4. 保存修改后的工作簿

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
