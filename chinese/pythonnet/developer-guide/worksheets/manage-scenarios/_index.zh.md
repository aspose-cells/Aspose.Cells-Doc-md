---
title: 使用Python创建、操作或删除工作表中的场景 via .NET
linktitle: 管理场景
type: docs
weight: 190
url: /zh/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: 学习如何使用 Aspose.Cells for Python via .NET API 编程方式创建、修改和删除Excel工作表中的场景。
keywords: Python Excel 场景，管理工作表场景（Scenario），添加场景，删除场景，修改场景。
---

{{% alert color="primary" %}}

有时您需要在电子表格中创建、操作或删除场景。场景是一个命名的“假设？”模型，包括变量输入单元格，链接到一个或多个公式。在创建场景之前，设计工作表，确保其包含至少一个依赖于可接受不同值的单元格的公式。本文演示如何使用 Aspose.Cells for Python via .NET 管理工作表中的场景。

{{% /alert %}}

Aspose.Cells 提供多种类来处理场景：
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

使用 [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/) 属性访问场景。以下代码演示了如何：
1. 打开包含场景的Excel文件
2. 删除现有场景
3. 添加新场景

4. 保存修改后的工作簿

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

