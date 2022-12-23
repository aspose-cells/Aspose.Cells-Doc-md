---
title: Rendre une page PDF par feuille de calcul Excel - Conversion d'Excel en PDF
type: docs
weight: 100
url: /fr/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

Lorsque vous travaillez avec de gros fichiers Excel Microsoft (par exemple, un classeur contenant de nombreuses feuilles, chacune avec 50 colonnes et 300 lignes de données ou plus), vous souhaiterez peut-être que la sortie PDF affiche une page par feuille de calcul, quelle que soit la taille de la feuille de calcul. . Cela signifierait que chaque page est susceptible d'avoir une taille de page radicalement différente. Ceci peut être réalisé en utilisant Aspose.Cells for .NET.

{{% /alert %}} 

Veuillez consulter l'exemple de code suivant qui convertit un fichier Excel avec plusieurs feuilles de calcul en PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

 Si la[Unepageparfeuille](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) l'option est définie sur**vrai**, tout le contenu de la feuille sera rendu sur une page PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)juste avant de rendre la feuille de calcul en PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
