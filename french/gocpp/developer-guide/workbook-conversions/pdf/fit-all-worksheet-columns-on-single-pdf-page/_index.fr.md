---
title: Adapter toutes les colonnes de la feuille de calcul à une seule page PDF avec Golang via C++
linktitle: Adapter toutes les colonnes de la feuille de calcul sur une seule page PDF
type: docs
weight: 160
url: /fr/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Générez un PDF qui ajuste toutes les colonnes de la feuille de calcul sur une seule page en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Parfois, vous souhaitez générer un fichier PDF qui ajuste toutes les colonnes d'une feuille de calcul sur une seule page. La propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) offre cette fonctionnalité de manière très simple. Les calculs complexes, comme la hauteur et la largeur du PDF de sortie, sont gérés en interne et sont basés sur les données de la feuille de calcul.

{{% /alert %}}

## **Adapter les colonnes de la feuille de calcul sur une seule page PDF**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) garantit que toutes les colonnes d'une feuille de calcul sont rendues sur une seule page PDF, bien que les lignes puissent s'étendre sur plusieurs pages en fonction des données de la feuille de calcul.

Le code d'exemple ci-dessous montre comment utiliser la propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) pour rendre une grande feuille de calcul de 100 colonnes.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

Lorsqu'une feuille de calcul donnée comporte de nombreuses colonnes, le fichier PDF généré peut afficher le contenu dans une taille très petite. Il reste lisible lorsqu'il est agrandi dans une application de visualisation telle que Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
