---
title: Créer, manipuler ou supprimer des scénarios dans les feuilles de calcul avec Python via .NET
linktitle: Gérer des scénarios
type: docs
weight: 190
url: /fr/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Apprenez comment créer, modifier et supprimer des scénarios dans les feuilles Excel de manière programmée en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Scénarios Excel Python, gérer les scénarios dans les feuilles de calcul Python, ajouter un scénario Python, supprimer un scénario Excel Python, modifier les scénarios Python
---

{{% alert color="primary" %}}

Parfois, vous devez créer, manipuler ou supprimer des scénarios dans des tableaux. Un scénario est un modèle nommé 'que faire si ?' qui inclut des cellules variables liées par une ou plusieurs formules. Avant de créer un scénario, concevez la feuille de calcul pour qu'elle contienne au moins une formule dépendant de cellules pouvant accepter différentes valeurs. Cet exemple montre comment gérer les scénarios dans les feuilles de calcul en utilisant Aspose.Cells pour Python via .NET.

{{% /alert %}}

Aspose.Cells fournit plusieurs classes pour travailler avec des scénarios :
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

Utilisez la propriété [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/) pour accéder aux scénarios. Le code suivant montre comment :
1. Ouvrir un fichier Excel contenant des scénarios
2. Supprimer un scénario existant
3. Ajouter un nouveau scénario

4. Enregistrer le classeur modifié

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

