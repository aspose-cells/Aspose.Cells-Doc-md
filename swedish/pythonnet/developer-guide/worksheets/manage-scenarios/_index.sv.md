---
title: Skapa, manipulera eller ta bort scenarier från arken med Python via .NET
linktitle: Hantera scenarier
type: docs
weight: 190
url: /sv/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Lär dig att skapa, modifiera och ta bort scenarier i Excel ark programmässigt med Aspose.Cells för Python via .NET API.
keywords: Python Excel scenarier, hantera scenarier i arket med Python, lägga till scenario Python, ta bort scenario Excel Python, ändra scenarier Python
---

{{% alert color="primary" %}}

Ibland behöver du skapa, manipulera eller ta bort scenarier i kalkylblad. Ett scenario är en namngiven 'tänk om?'-modell som inkluderar variabla inmatningsceller kopplade via en eller flera formler. Innan du skapar ett scenario, designa arket så att det innehåller minst en formel som beror på celler som kan acceptera olika värden. Detta exempel visar hur man hanterar scenarier i kalkylblad med Aspose.Cells för Python via .NET.

{{% /alert %}}

Aspose.Cells tillhandahåller flera klasser för att arbeta med scenarier:
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

Använd [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/)-egenskapen för att komma åt scenarier. Följande kod visar hur man:
1. Öppnar en Excel-fil med scenarier
2. Tar bort ett befintligt scenario
3. Lägger till ett nytt scenario

4. Sparar den modifierade arbetsboken

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

