---
title: Enregistrer chaque feuille de calcul dans un fichier PDF différent
type: docs
weight: 50
url: /fr/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion de fichiers de feuille de calcul (contenant des images, des graphiques, etc.) en documents PDF. Aspose.Cells for Java peut fonctionner indépendamment pour convertir une feuille de calcul en document PDF et vous n'avez plus besoin d'utiliser Aspose.PDF for Java pour la conversion. La conversion ne nécessite pas non plus de créer/utiliser de fichier(s) temporaire(s) car l'ensemble du processus peut être effectué dans la mémoire.

{{% /alert %}}

Si vous devez enregistrer chaque feuille de calcul dans votre modèle de fichier Excel pour générer différents fichiers PDF. Ceci peut être réalisé facilement. Vous pouvez essayer de masquer des feuilles dans le fichier et de rendre une feuille visible à la fois en fonction de laquelle vous rendriez les PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

 Si la feuille de calcul contient des formules, il est préférable d'appeler le[**Workbook.calculateFormulaWorkbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()juste avant de rendre la feuille de calcul au format PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
