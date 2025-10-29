---
title: Appliquer une mise en forme conditionnelle avancée avec Python.NET
linktitle: Appliquer le formatage conditionnel avancé
type: docs
weight: 70
url: /fr/python-net/apply-advanced-conditional-formatting/
description: Apprenez à implémenter les fonctionnalités avancées de mise en forme conditionnelle d Excel comme les barres de données, les échelles de couleurs et les ensembles d icônes en utilisant Aspose.Cells pour Python via .NET.
keywords: Mise en forme Excel en Python, Mise en forme conditionnelle Python, Barres de données Python, Échelles de couleurs Python, Ensembles d icônes Python, Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 et versions ultérieures (2010/2013/2016) offrent des fonctionnalités avancées de mise en forme conditionnelle, y compris la coloration des cellules, les bordures, les icônes colorées, les flèches, les drapeaux et la mise en forme de la police.

{{% /alert %}} 

## **Mettre en œuvre une mise en forme conditionnelle avancée dans les fichiers Excel**
Aspose.Cells pour Python via .NET prend en charge toutes les fonctionnalités avancées de mise en forme conditionnelle, y compris :

- Ajouter des barres de données ombrées pour améliorer graphiquement les chiffres sous-jacents en intégrant un simple graphique à barres dans les cellules.
- Ombrer automatiquement les cellules avec des échelles de couleurs en fonction de leur relation avec les valeurs des autres cellules de la plage. Les paramètres par défaut ombragent la plus faible valeur en rouge jusqu'à la plus élevée en vert.
- Utiliser des ensembles d'icônes de manière similaire aux échelles de couleurs, mais au lieu d'ombrer les cellules, il ajoute de petites icônes, telles que des flèches et des feux de signalisation, aux cellules.

Aspose.Cells prend en charge pleinement le formatage conditionnel fourni par Microsoft Excel 2007 et les versions ultérieures au format XLSX sur les cellules en cours d'exécution. Cet exemple montre un exercice pour les types de formatage conditionnel avancé, y compris IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom et d'autres règles avec différents ensembles d'attributs.

- [**Adding Color Scale Conditional Formattings**](/cells/fr/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/fr/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/fr/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/fr/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/fr/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/fr/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/fr/python-net/how-to-add-top10-conditional-formatting/)



### **Calculer la sélection de couleur d'Excel pour la mise en forme par échelle de couleurs**
Ce code montre comment déterminer la couleur choisie par Excel pour les règles de mise en forme conditionnelle par échelle de couleurs :

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}
