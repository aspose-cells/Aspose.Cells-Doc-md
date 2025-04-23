---
title: Utilisation de la fonction FormulaText dans Aspose.Cells avec Python.NET
linktitle: Utiliser la fonction FormulaText
type: docs
weight: 60
url: /fr/python-net/using-formulatext-function-in-aspose-cells/
description: Apprenez à utiliser la fonction FORMULATEXT d Excel avec Aspose.Cells pour Python via .NET. Obtenez et définissez les formules des cellules de manière programmatique tout en conservant l intégrité de la feuille de calcul.
keywords: Aspose.Cells, Python, Excel, FORMULATEXT, gestion des formules, automatisation de feuilles de calcul
---

{{% alert color="primary" %}} 

FORMULATEXT est une fonction d'Excel 2013 et versions ultérieures. Elle n'est pas prise en charge par les versions précédentes comme Excel 2010 ou 2007, etc. Comme son nom l'indique, elle affiche le texte de la formule contenue dans une cellule spécifiée. Cet article montre comment utiliser cette fonction avec Aspose.Cells pour Python via .NET.

{{% /alert %}} 

Le code d'exemple suivant illustre l'utilisation de FORMULATEXT avec Aspose.Cells. Le code écrit d'abord une formule dans la cellule A1, puis affiche le texte de la formule en utilisant FORMULATEXT dans la cellule A2.

```python
from aspose.cells import Workbook

# Create a workbook object
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Put some formula in cell A1
cell_a1 = worksheet.cells.get("A1")
cell_a1.formula = "=Sum(B1:B10)"

# Get the text of the formula in cell A2 using FORMULATEXT function
cell_a2 = worksheet.cells.get("A2")
cell_a2.formula = "=FormulaText(A1)"

# Calculate the workbook
workbook.calculate_formula()

# Print the results of A2, It will now print the text of the formula inside cell A1
print(cell_a2.string_value)
```

## **Sortie console**
Voici la sortie de la console pour le code ci-dessus :

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
