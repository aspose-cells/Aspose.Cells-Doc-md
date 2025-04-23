---
title: Szenarien in Arbeitsblättern erstellen, manipulieren oder entfernen mit Python via .NET
linktitle: Szenarien verwalten
type: docs
weight: 190
url: /de/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Lernen Sie, wie man Szenarien in Excel Arbeitsblättern mit Aspose.Cells für Python via .NET API programmatisch erstellt, ändert und löscht.
keywords: Python Excel Szenarien, Szenarien in Arbeitsblättern mit Python verwalten, Szenario hinzufügen Python, Szenario entfernen Excel Python, Szenarien modifizieren Python.
---

{{% alert color="primary" %}}

Manchmal müssen Sie Szenarien in Tabellenkalkulationen erstellen, manipulieren oder löschen. Ein Szenario ist ein benanntes „Was-wäre-wenn“-Modell, das variable Eingabezellen umfasst, die durch eine oder mehrere Formeln verbunden sind. Bevor Sie ein Szenario erstellen, gestalten Sie das Arbeitsblatt so, dass es mindestens eine Formel enthält, die von Zellen abhängt, die unterschiedliche Werte annehmen können. Dieses Beispiel zeigt, wie Sie Szenarien mit Aspose.Cells für Python via .NET verwalten.

{{% /alert %}}

Aspose.Cells stellt mehrere Klassen für die Arbeit mit Szenarien bereit:
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

Verwenden Sie die Eigenschaft [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/), um auf Szenarien zuzugreifen. Das folgende Beispiel zeigt, wie man:
1. Eine Excel-Datei mit Szenarien öffnet
2. Ein bestehendes Szenario entfernt
3. Ein neues Szenario hinzufügt

4. Die modifizierte Arbeitsmappe speichert

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

