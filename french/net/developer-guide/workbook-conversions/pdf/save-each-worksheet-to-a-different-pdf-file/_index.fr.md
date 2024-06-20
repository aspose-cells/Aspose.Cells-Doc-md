---
title: Enregistrer chaque feuille de calcul dans un fichier PDF différent
type: docs
weight: 130
url: /fr/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge la conversion de fichiers XLS (contenant des images, des graphiques, etc.) en documents PDF. Aspose.Cells for .NET peut fonctionner de manière indépendante pour convertir une feuille de calcul en PDF et vous n'avez pas besoin d'utiliser Aspose.PDF pour .NET pour la conversion. La conversion ne nécessite pas que le logiciel crée ou utilise des fichiers temporaires, car tout le processus peut être effectué en mémoire.

{{% /alert %}} 
## **Sauvegarder chaque feuille de calcul dans un fichier PDF différent**
Si vous avez besoin de sauvegarder chaque feuille de calcul de votre fichier Excel modèle pour générer différents fichiers PDF, vous pouvez y parvenir facilement. Vous pouvez essayer de définir un indice de feuille à la fois à rendre en PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
