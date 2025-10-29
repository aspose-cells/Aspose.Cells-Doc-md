---
title: Rendre une page PDF par feuille de calcul Excel  Conversion Excel en PDF avec Golang via C++
type: docs
weight: 100
url: /fr/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Convertir les feuilles Excel au format PDF avec une page pour chaque feuille en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}} 

Lorsque vous travaillez avec de grands fichiers Excel Microsoft (par exemple un classeur contenant plusieurs feuilles, chacune avec 50 colonnes et 300 lignes ou plus), vous pouvez vouloir que la sortie PDF affiche une page par feuille, indépendamment de la taille de la feuille. Cela signifie que chaque page aura probablement une taille de page très différente. Cela peut être réalisé en utilisant Aspose.Cells for C++.

{{% /alert %}} 

Veuillez consulter le code d'exemple suivant qui convertit un fichier Excel avec plusieurs feuilles de calcul en PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

Si l'option [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) est réglée sur **true**, tout le contenu de la feuille sera rendu sur une seule page PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) juste avant de rendre la feuille de calcul en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et que les valeurs correctes sont affichées dans le PDF.

{{% /alert %}}
