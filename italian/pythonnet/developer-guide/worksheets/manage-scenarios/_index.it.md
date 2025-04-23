---
title: Creare, manipolare o rimuovere scenari dai fogli di lavoro con Python via .NET
linktitle: Gestire gli scenari
type: docs
weight: 190
url: /it/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Impara come creare, modificare e eliminare scenari nei fogli di lavoro di Excel programmaticamente usando le API di Aspose.Cells per Python via .NET.
keywords: Scenari Excel Python, gestire scenari di fogli di lavoro Python, aggiungere scenario Python, rimuovere scenario Excel Python, modificare scenari Python
---

{{% alert color="primary" %}}

 A volte è necessario creare, manipolare o eliminare scenari nei fogli di calcolo. Uno scenario è un modello con nome 'cosa succederebbe?' che include celle di input variabili collegate da una o più formule. Prima di creare uno scenario, progetta il foglio in modo che contenga almeno una formula dipendente da celle che possono accettare valori diversi. Questo esempio dimostra come gestire gli scenari nei fogli di lavoro utilizzando Aspose.Cells per Python via .NET.

{{% /alert %}}

 Aspose.Cells fornisce diverse classi per lavorare con gli scenari:
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

 Usa la proprietà [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/) per accedere agli scenari. Il seguente esempio di codice dimostra come:
1. Aprire un file Excel contenente scenari
2. Rimuovere uno scenario esistente
3. Aggiungere un nuovo scenario

4. Salvare il workbook modificato

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

