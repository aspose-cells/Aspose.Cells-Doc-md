---
title: Rendre une page PDF par feuille de calcul Excel  Conversion Excel en PDF
type: docs
weight: 40
url: /fr/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Lorsque vous travaillez avec de grands fichiers Microsoft Excel (par exemple, un classeur comprenant de nombreuses feuilles, chacune avec 50 colonnes et 300 lignes de données ou plus), vous voudrez peut-être que la sortie PDF affiche une page par feuille de calcul, quelle que soit la taille de la feuille de calcul. Cela signifie que chaque page est susceptible d'avoir une taille de page radicalement différente. Cela peut être réalisé en utilisant Aspose.Cells for Java.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant qui convertit un fichier Excel avec plusieurs feuilles de calcul en PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

Si l'option [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) est définie sur **true**, tout le contenu de la feuille est rendu sur une seule page PDF. La taille de papier définie par [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) est invalide, mais les autres paramètres définis avec [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) restent valables.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) juste avant de rendre la feuille de calcul en PDF. Cela garantit que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
