---
title: Calcul des fonctions MINIFS et MAXIFS de Excel 2016 avec Python.NET
linktitle: Calcul des fonctions MINIFS et MAXIFS d Excel 2016
type: docs
weight: 300
url: /fr/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: Apprenez comment calculer les fonctions MINIFS et MAXIFS de Excel 2016 en utilisant Aspose.Cells pour Python via .NET API avec des exemples de code.
keywords: python excel, minifs maxifs, calcul de formule, aspose.cells
---

## **Scénarios d'utilisation possibles**
Microsoft Excel 2016 supporte les fonctions MINIFS et MAXIFS. Ces fonctions ne sont pas supportées dans Excel 2013 ou versions antérieures. Aspose.Cells supporte également le calcul de ces fonctions. La capture d'écran suivante illustre l'utilisation de ces fonctions. Veuillez lire les commentaires en rouge dans la capture pour comprendre comment ces fonctions fonctionnent.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcul des fonctions MINIFS et MAXIFS d'Excel 2016**
Le code d'échantillon suivant charge le [fichier Excel d'exemple](5115149.xlsx) et appelle la méthode [workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) pour effectuer le calcul des formules via Aspose.Cells, puis enregistre les résultats dans le [PDF de sortie](5115154.pdf).


```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Load your source workbook containing MINIFS and MAXIFS functions
workbook = Workbook(os.path.join(source_dir, "sampleMINIFSAndMAXIFS.xlsx"))

# Perform Aspose.Cells formula calculation
workbook.calculate_formula()

# Save the calculations result in pdf format
options = PdfSaveOptions()
options.one_page_per_sheet = True

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "outputMINIFSAndMAXIFS.pdf"), options)
```
