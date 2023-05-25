---
title: Enregistrer chaque feuille de calcul dans un fichier PDF différent
type: docs
weight: 130
url: /fr/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

Aspose.Cells prend en charge la conversion de fichiers XLS (contenant des images, des graphiques, etc.) en documents PDF. Aspose.Cells for .NET peut fonctionner indépendamment pour convertir une feuille de calcul en PDF et vous n'avez pas besoin d'utiliser Aspose.PDF for .NET pour la conversion. La conversion ne nécessite pas que le logiciel crée ou utilise des fichiers temporaires car l'ensemble du processus peut être effectué en mémoire.

{{% /alert %}} 
##  **Enregistrer chaque feuille de calcul dans un fichier PDF différent**
 Si vous devez enregistrer chaque feuille de calcul dans votre modèle de fichier Excel pour générer différents fichiers PDF, vous pouvez y parvenir facilement. Vous pouvez essayer de définir un index de feuille sur**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option à la fois pour rendre à PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Si votre feuille de calcul contient des formules, il est préférable d'appeler[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le fichier PDF.

{{% /alert %}}
