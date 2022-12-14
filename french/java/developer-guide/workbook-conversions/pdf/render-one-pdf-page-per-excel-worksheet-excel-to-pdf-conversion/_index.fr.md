---
title: Rendu d'une page PDF par feuille de calcul Excel - Conversion d'Excel en PDF
type: docs
weight: 40
url: /fr/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Lorsque vous travaillez avec de gros fichiers Excel Microsoft (par exemple, un classeur contenant de nombreuses feuilles, chacune avec 50 colonnes et 300 lignes de données ou plus), vous souhaiterez peut-être que la sortie PDF affiche une page par feuille de calcul, quelle que soit la taille de la feuille de calcul. . Cela signifierait que chaque page est susceptible d'avoir une taille de page radicalement différente. Ceci peut être réalisé en utilisant Aspose.Cells for Java.

{{% /alert %}}

Veuillez consulter l'exemple de code suivant qui convertit un fichier Excel avec plusieurs feuilles de calcul en PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

 Si la[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) l'option est définie sur**vrai** , tout le contenu de la feuille est restitué sur une seule page PDF. Le format de papier défini par[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) n'est pas valide, mais les autres paramètres définis avec[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)prennent encore effet.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler le[**Workbook.calculateFormulaWorkbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) juste avant de rendre la feuille de calcul au format PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
