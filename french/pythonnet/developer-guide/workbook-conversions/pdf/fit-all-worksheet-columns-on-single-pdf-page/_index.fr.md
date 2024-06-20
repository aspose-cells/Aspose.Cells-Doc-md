---
title: Adapter toutes les colonnes de la feuille de calcul sur une seule page PDF
type: docs
weight: 160
url: /fr/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Apprenez à ajuster toutes les colonnes de la feuille de calcul sur une seule page PDF avec Aspose.Cells pour Python via .NET API.
keywords: Ajuster toutes les colonnes de la feuille de calcul sur une seule page PDF en Python, Ajuster les colonnes de la feuille de calcul sur une seule page PDF en utilisant Python, Enregistrer toutes les colonnes sur une seule page PDF, Enregistrer toutes les colonnes sur une seule page PDF en Python
---

{{% alert color="primary" %}}

Parfois, vous voulez générer un fichier PDF qui adapte toutes les colonnes d'une feuille de calcul sur une seule page. La propriété [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) offre cette fonctionnalité de manière très facile à utiliser. Les calculs complexes tels que la hauteur et la largeur du PDF de sortie sont gérés en interne et sont basés sur les données de la feuille de calcul.

{{% /alert %}}

## **Adapter les colonnes de la feuille de calcul sur une seule page PDF**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) s'assure que toutes les colonnes d'une feuille de calcul sont rendues sur une seule page PDF, bien que les lignes puissent s'étendre sur plusieurs pages en fonction des données dans la feuille de calcul.

Le code d'exemple ci-dessous montre comment utiliser la propriété [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) pour afficher une grande feuille de calcul de 100 colonnes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul donnée comporte de nombreuses colonnes, le fichier PDF généré peut afficher le contenu dans une taille très petite. Il reste lisible lorsqu'il est agrandi dans une application de visualisation telle que Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de générer la feuille de calcul au format PDF. De cette façon, les valeurs dépendant des formules seront recalculées et les valeurs correctes seront rendues dans le PDF.

{{% /alert %}}
