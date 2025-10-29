---
title: Создавать, редактировать или удалять сценарии в листах с помощью Python via .NET
linktitle: Управление сценариями
type: docs
weight: 190
url: /ru/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Узнайте, как создавать, изменять и удалять сценарии в листах Excel программным способом, используя API Aspose.Cells для Python via .NET.
keywords: Сценарии Excel на Python, управление сценариями листов в Python, добавление сценария в Python, удаление сценария Excel в Python, изменение сценариев Python
---

{{% alert color="primary" %}}

Иногда необходимо создавать, Man manipulating or deleting scenarios in spreadsheets. A scenario is a named 'what if?' model that includes variable input cells linked by one or more formulas. Before creating a scenario, design the worksheet so it contains at least one formula that depends on cells which can accept different values. This example demonstrates how to manage scenarios in worksheets using Aspose.Cells for Python via .NET.

{{% /alert %}}

Aspose.Cells предоставляет несколько классов для работы с сценариями:
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

Используйте свойство [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/) для доступа к сценариям. Следующий код показывает как:
1. Открыть Excel файл с сценариями
2. Удалить существующий сценарий
3. Добавить новый сценарий

4. Сохранить изменённую рабочую книгу

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

{{< app/cells/assistant language="python-net" >}}
