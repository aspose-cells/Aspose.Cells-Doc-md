---
title: Comment mettre à l échelle une feuille de calcul avec Python.NET
linktitle: Comment mettre à l échelle une feuille de calcul
type: docs
weight: 130
url: /fr/python-net/how-to-scale-a-worksheet/
description: Cet article explique comment mettre à l’échelle une feuille de calcul en utilisant Aspose.Cells pour Python.NET.
keywords: Mettre à l’échelle une feuille avec Python, Mise à l’échelle d’une feuille avec Python.NET, Ajuster à la page en Python, Pourcentage de mise à l’échelle avec Python, Aspose.Cells mise à l’échelle d’une feuille Python.
---

## **Scénarios d'utilisation possibles**
Mettre à l'échelle une feuille de calcul peut être utile pour diverses raisons, en fonction du contexte dans lequel vous travaillez. Voici quelques raisons courantes :
1. **Adapter à la page** : pour que tout le contenu tienne sur une seule page ou un nombre spécifique de pages lors de l'impression.
1. **Présentation** : pour créer des feuilles organisées et professionnelles à partager.
1. **Lisibilité** : pour ajuster la taille du texte et des éléments pour une meilleure accessibilité visuelle.
1. **Gestion de l'espace** : pour optimiser la disposition de la feuille et minimiser l’espace blanc inutile.
1. **Visualisation des données** : pour dimensionner correctement les graphiques et diagrammes dans l’espace disponible.
1. **Cohérence** : pour maintenir une apparence uniforme à travers plusieurs feuilles ou documents.

## **Comment mettre à l'échelle une feuille de calcul dans Excel**
Mettre à l’échelle une feuille dans Excel permet d’adapter le contenu sur des pages spécifiques lors de l’impression. Suivez ces étapes :

1. Ouvrez votre feuille dans Excel
1. Naviguez vers **Mise en page** > groupe **Adapter à la mise en page**
1. Ajustez **Largeur** et **Hauteur** en fonction des exigences de nombre de pages
1. Définissez un pourcentage de mise à l’échelle personnalisé si nécessaire
<br>
<img src="1.png" width=60% />

## **Comment mettre à l’échelle une feuille en utilisant Python.NET**
Aspose.Cells pour Python.NET offre des capacités complètes de mise à l'échelle des feuilles de calcul. Utilisez ces approches pour mettre à l'échelle les feuilles de calcul de manière programmatique :

### **Exemple d'ajustement à la page**
Ajustez les paramètres d'impression pour faire tenir le contenu sur les pages spécifiées :
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the worksheet to fit to 1 page wide and 1 page tall
page_setup.fit_to_pages_wide = 1
page_setup.fit_to_pages_tall = 1

# Save the modified workbook
workbook.save("output_fit_to_page.xlsx")
```
<br>
<img src="3.png" width=60% />

### **Exemple de mise à l'échelle en pourcentage**
Appliquez un pourcentage de mise à l'échelle personnalisé au contenu de la feuille de calcul :
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the scaling to a specific percentage (e.g., 75%)
page_setup.zoom = 75

# Save the modified workbook
workbook.save("output_scaled_percentage.xlsx")
```
<br>
<img src="2.png" width=60% />

**Références API clés :**
- [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) classe
- [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) classe
- Configuration [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)
{{< app/cells/assistant language="python-net" >}}
