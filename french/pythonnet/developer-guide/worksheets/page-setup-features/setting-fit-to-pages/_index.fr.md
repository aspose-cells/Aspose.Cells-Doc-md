---
title: Comment imprimer Excel en pages ajustées en largeur et en hauteur avec Python.NET
linktitle: Comment imprimer Excel en pages adaptées en largeur et en hauteur
type: docs
weight: 200
url: /fr/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Apprenez à définir les propriétés fit_to_pages_wide et fit_to_pages_tall pour l impression Excel en utilisant Aspose.Cells pour API Python via .NET.
keywords: Impression Excel avec Python, Paramètres de mise à l échelle pour Python, FitToPagesWide pour Python, FitToPagesTall pour Python, Impression de feuille de calcul en une seule page Python, Impression de toutes les colonnes en une seule page Python
---

## **Introduction**

Les réglages fit_to_pages_wide et fit_to_pages_tall contrôlent la mise à l'échelle de la feuille de calcul lors de l'impression. Ces réglages garantissent que la sortie imprimée s'adapte aux dimensions de page spécifiées :

1. **fit_to_pages_wide** : Spécifie le nombre de pages horizontales pour l'impression
1. **fit_to_pages_tall** : Spécifie le nombre de pages verticales pour l'impression

## **Pourquoi utiliser FitToPagesWide et FitToPagesTall**
Les principaux avantages incluent :
1. Contrôle précis de la mise en page d'impression
1. Formatage cohérent de plusieurs feuilles
1. Présentation professionnelle du document

## **Comment imprimer un fichier en pages adaptées en largeur et en hauteur dans Excel**
Pour configurer dans Microsoft Excel :
1. Ouvrir le classeur et sélectionner la feuille de calcul
1. Naviguer vers le dialog **Mise en page** → **Configuration de la page**
1. Dans l'onglet **Page** sous **Échelle :**
   - Sélectionner « Fit to »
   - Spécifier le nombre de pages en largeur (horizontale) et en hauteur (verticale)

<br>
<img src="2.png" width=60% />

## **Comment imprimer Excel en pages adaptées en largeur et en hauteur en utilisant Aspose.Cells**
Pour configurer par programmation :
1. Charger le [fichier d'exemple](input.xlsx)
1. Accéder à l'objet [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) de la feuille de calcul
1. Définir les propriétés [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) et [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/)

```python
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("input.xlsx")

# Accessing the first worksheet in the Excel file
worksheet = workbook.worksheets[0]

# Setting the number of pages to which the length of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_tall = 1

# Setting the number of pages to which the width of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_wide = 1

# Save the workbook
workbook.save("out_net.pdf")
```

Résultat de la sortie :
<br>
<img src="1.png" width=60% />

## **Comment imprimer une feuille comme une seule page**
Pour forcer la sortie sur une seule page :
1. Utiliser [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Définir la propriété [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting OnePagePerSheet option
options.one_page_per_sheet = True

# Save the workbook with options
workbook.save("OnePagePerSheet.pdf", options)
```

Résultat de la sortie :
<br>
<img src="3.png" width=60% />

## **Comment imprimer toutes les colonnes en une seule page**
Pour consolider les colonnes horizontalement :
1. Configurer [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Activer la propriété [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting all columns in one page per sheet
options.all_columns_in_one_page_per_sheet = True

# Save the workbook
workbook.save("AllColumnsInOnePagePerSheet.pdf", options)
```

Résultat de la sortie :
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="python-net" >}}
