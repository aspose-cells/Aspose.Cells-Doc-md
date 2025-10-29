---
title: Calcul de la formule de table de données en tableau avec Python.NET
linktitle: Calcul de la formule de tableau de données
type: docs
weight: 70
url: /fr/python-net/calculation-of-array-formula-of-data-tables/
description: Apprenez comment calculer des formules matricielles pour les tableaux de données Excel en utilisant Aspose.Cells pour Python via .NET API. Modifier et enregistrer les feuilles de calcul de manière programmatique.
keywords: Python Excel Data Tables, Formules matricielles Python, Aspose.Cells Python, Calcul des tableaux de données Python, Automatisation Excel Python
---

{{% alert color="primary" %}}

Vous pouvez créer un tableau de données dans Microsoft Excel en utilisant Données > Analyse de scénarios > Tableau de données.... Aspose.Cells pour Python via .NET vous permet de calculer la formule matricielle d’un tableau de données. Veuillez utiliser [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) comme d'habitude pour calculer tout type de formule.

{{% /alert %}}

Dans l'exemple suivant, nous utilisons le [fichier Excel source](5115535.xlsx). Si vous changez la valeur de la cellule B1 en 100, les valeurs du tableau de données (surlignées en jaune) se mettront à jour à 120 comme le montrent les captures d'écran ci-dessous. Le code Python génère ce [PDF de sortie](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Voici l'implémentation Python démontrant comment générer le [PDF de sortie](5115538.pdf) à partir du [fichier Excel source](5115535.xlsx) :

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook from source excel file
workbook = Workbook(os.path.join(data_dir, "DataTable.xlsx"))

# Access first worksheet
worksheet = workbook.worksheets[0]

# When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.cells.get("B1").put_value(100)

# Calculate formula, now it also calculates Data Table array formula
workbook.calculate_formula()

# Save the workbook in pdf format
workbook.save(os.path.join(data_dir, "output_out.pdf"))
```

**Explication du code Python :**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
{{< app/cells/assistant language="python-net" >}}
