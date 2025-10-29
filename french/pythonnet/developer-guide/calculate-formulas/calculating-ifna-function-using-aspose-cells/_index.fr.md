---
title: Calcul de la fonction IFNA avec Python.NET en utilisant Aspose.Cells
linktitle: Calcul de la fonction IFNA
type: docs
weight: 40
url: /fr/python-net/calculating-ifna-function-using-aspose-cells/
description: Apprenez comment calculer la fonction IFNA dans les fichiers Excel en utilisant Aspose.Cells pour Python.NET. Gérez les erreurs #N/A et enregistrez efficacement les feuilles de calcul modifiées.
keywords: Python.NET, Excel, fonction IFNA, Aspose.Cells, gestion des erreurs, calcul de feuille de calcul
---

{{% alert color="primary" %}}

Aspose.Cells pour Python.NET supporte le calcul de la fonction Excel IFNA. La fonction IFNA renvoie une valeur spécifiée si une formule aboutit à une erreur #N/A; sinon, elle renvoie le résultat de la formule.

{{% /alert %}}

## **Calcul de la fonction IFNA en Python.NET**

L'exemple de code suivant montre comment calculer la fonction IFNA en utilisant Aspose.Cells pour Python.NET :


## **Sortie console**
Le code ci-dessus produira la sortie suivante dans la console :

```
Not found
Orange
```

## **Explication des étapes clés**
1. Créer une nouvelle instance [`Workbook`](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
2. Accéder à la feuille de calcul et à la collection de cellules
3. Remplir les données source dans la colonne A
4. Définir des formules VLOOKUP pouvant produire des erreurs #N/A
5. Utiliser IFNA pour gérer d’éventuelles erreurs
6. Calculer les formules en utilisant [`calculate_formula()`](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/)
7. Récupérer et afficher les résultats des cellules gérant les erreurs
8. Enregistrer le classeur modifié avec les résultats du calcul

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Add data for VLOOKUP
cells = worksheet.cells
cells.get("A1").put_value("Apple")
cells.get("A2").put_value("Orange")
cells.get("A3").put_value("Banana")

# Access cell A5 and A6
cell_a5 = worksheet.cells.get("A5")
cell_a6 = worksheet.cells.get("A6")

# Assign IFNA formula to A5 and A6
cell_a5.formula = "=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")"
cell_a6.formula = "=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")"

# Calculate the formula of workbook
workbook.calculate_formula()

# Print the values of A5 and A6
print(cell_a5.string_value)
print(cell_a6.string_value)
```
{{< app/cells/assistant language="python-net" >}}
