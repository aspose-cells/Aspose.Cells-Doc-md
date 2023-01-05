---
title: Convertir le fichier XLS avec des images ou des graphiques en PDF
type: docs
weight: 50
url: /fr/net/convert-xls-file-with-images-or-charts-to-pdf/
---
{{% alert color="primary" %}} 

Aspose.Cells prend en charge la conversion de fichiers XLS contenant des images et des graphiques en documents PDF. Aspose.Cells for .NET peut fonctionner indépendamment pour convertir une feuille de calcul en PDF : Aspose.PDF for .NET n'est pas nécessaire pour la conversion. Le processus peut être effectué en mémoire car le processus ne dépend pas de fichiers XML temporaires ou intermédiaires. Cela signifie que les fichiers Excel volumineux, par exemple ceux contenant des images, des graphiques et d'autres objets de dessin, peuvent être convertis rapidement et efficacement.

{{% /alert %}} 
## **Exemple de code**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Si la feuille de calcul contient des formules, il est préférable d'appeler le[Workbook.CalculateFormulaWorkbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) juste avant le rendu en PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
