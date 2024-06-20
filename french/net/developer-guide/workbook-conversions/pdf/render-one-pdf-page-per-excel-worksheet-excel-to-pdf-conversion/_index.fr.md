---
title: Rendre une page PDF par feuille de calcul Excel  Conversion Excel en PDF
type: docs
weight: 100
url: /fr/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

Lorsque vous travaillez avec de grands fichiers Microsoft Excel (par exemple un classeur comportant de nombreuses feuilles, chacune avec 50 colonnes et 300 lignes ou plus de données), vous voudrez peut-être que la sortie PDF montre une page par feuille de calcul, quelle que soit la taille de la feuille de calcul. Cela signifierait que chaque page est susceptible d'avoir une taille de page radicalement différente. Cela peut être réalisé en utilisant Aspose.Cells for .NET.

{{% /alert %}} 

Veuillez consulter le code d'exemple suivant qui convertit un fichier Excel avec plusieurs feuilles de calcul en PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

Si l'option [OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) est définie sur **true**, tout le contenu de la feuille de calcul sera rendu sur une seule page PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) juste avant de rendre la feuille de calcul au format PDF. Cela garantit que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
