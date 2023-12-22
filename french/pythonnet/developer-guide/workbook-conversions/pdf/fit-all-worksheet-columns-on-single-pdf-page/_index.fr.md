---
title: Ajuster toutes les colonnes de la feuille de calcul sur une seule page PDF
type: docs
weight: 160
url: /fr/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Découvrez comment adapter toutes les colonnes d'une feuille de calcul sur une seule page PDF avec Aspose.Cells for Python via .NET API.
keywords: Python Fit All Worksheet Columns on Single PDF Page, Fit Worksheet Columns on Single PDF Page using Python, Python Save All Worksheet Columns to a PDF Page, Save All Columns to single PDF Page in Python
---
{{% alert color="primary" %}}

Parfois, vous souhaitez générer un fichier PDF qui regroupe toutes les colonnes d'une feuille de calcul sur une seule page. Le[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) property fournit cette fonctionnalité d’une manière très simple à utiliser. Les calculs complexes tels que la hauteur et la largeur de la sortie PDF sont traités en interne et sont basés sur les données de la feuille de calcul.

{{% /alert %}}

##  **Ajuster les colonnes de la feuille de calcul sur une seule page PDF**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)garantit que toutes les colonnes d'une feuille de calcul sont restituées sur une seule page PDF, bien que les lignes puissent s'étendre sur plusieurs pages en fonction des données de la feuille de calcul.

L'exemple de code ci-dessous montre comment utiliser[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)propriété pour afficher une grande feuille de calcul de 100 colonnes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul donnée comporte de nombreuses colonnes, le fichier PDF rendu peut afficher le contenu dans une très petite taille. Il reste lisible lorsqu'il est mis à l'échelle dans une application de visualisation telle qu'Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

 Si votre feuille de calcul contient des formules, il est préférable d'appeler[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
