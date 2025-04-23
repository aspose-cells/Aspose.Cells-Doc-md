---
title: Définir le mode de calcul des formules du classeur avec Python.NET
linktitle: Définir le mode de calcul de formule du classeur
type: docs
weight: 110
url: /fr/python-net/setting-formula-calculation-mode-of-workbook/
description: Apprenez comment configurer le mode de calcul des formules (automatique, manuel) dans les classeurs Excel en utilisant l API Aspose.Cells pour Python via .NET. Guide étape par étape avec des exemples de code.
keywords: Python, Aspose.Cells, Excel, classeur, mode de calcul des formules, automatique, manuel, paramètres
---

## ** Configuration du mode de calcul des formules dans le classeur**

{{% alert color="primary" %}}

 Microsoft Excel propose trois modes de calcul des formules :
- **Automatique** : Recalcule les formules à chaque changement et à l'ouverture du classeur
- **Automatique sauf pour les tables de données** : Recalcule les formules sauf pour les tables de données lors des changements
- **Manuel** : Ne recalcule que sur demande de l’utilisateur (F9/CTRL+ALT+F9) ou lors de l’enregistrement

{{% /alert %}}

### ** Définir le mode de calcul avec Aspose.Cells**

 Aspose.Cells pour Python via .NET offre la configuration [**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/) via la propriété [**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/). Utilisez l’attribut [**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/) pour contrôler le comportement du calcul.

 Modes disponibles via l’énumération [**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/) :
- `AUTOMATIC`
- `AUTOMATIC_EXCEPT_TABLE`
- `MANUAL`

**Étapes de mise en œuvre :**
1. Charger le classeur existant ou créer une nouvelle instance
2. Accéder aux paramètres du classeur
3. Définir le mode de calcul en utilisant `formula_settings.calculation_mode`
4. Enregistrer le classeur modifié

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
