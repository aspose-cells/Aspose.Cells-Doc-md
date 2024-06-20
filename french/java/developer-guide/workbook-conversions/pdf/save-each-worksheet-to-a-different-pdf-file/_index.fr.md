---
title: Enregistrer chaque feuille de calcul dans un fichier PDF différent
type: docs
weight: 50
url: /fr/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion de fichiers de feuille de calcul (contenant des images, des graphiques, etc.) en documents PDF. Aspose.Cells for Java peut travailler de manière indépendante pour convertir une feuille de calcul en document PDF et vous n'avez plus besoin d'utiliser Aspose.PDF pour Java pour la conversion. La conversion ne nécessite pas de créer ou d'utiliser de fichier(s) temporaire(s) non plus car tout le processus peut être effectué en mémoire.

{{% /alert %}}

Si vous avez besoin de sauvegarder chaque feuille de calcul de votre fichier Excel modèle pour générer différents fichiers PDF, cela peut être réalisé facilement. Vous pouvez essayer de définir un index de feuille à la fois sur l'option [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) pour générer en PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler la méthode [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
