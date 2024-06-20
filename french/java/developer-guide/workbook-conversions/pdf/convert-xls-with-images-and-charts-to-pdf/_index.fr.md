---
title: Convertir XLS avec des images et des graphiques en PDF
type: docs
weight: 230
url: /fr/java/convert-xls-with-images-and-charts-to-pdf/
description: Le code Java pour convertir des fichiers Excel avec des images et des graphiques au format PDF en utilisant l API Aspose.Cells for Java.
keywords: excel to pdf java, convertir excel en pdf, convertir excel en pdf java, convertir excel avec des images en pdf java, convertir excel avec des graphiques en pdf java, convertir xls en pdf, convertir xlsx en pdf, xls en pdf java, xlsx en pdf java, excel en pdf.
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion de fichiers XLS contenant des images et des graphiques en documents PDF. Aspose.Cells for Java peut fonctionner de manière indépendante pour convertir une feuille de calcul en PDF : les API Aspose.PDF ne sont pas nécessaires pour la conversion.

{{% /alert %}}

Le processus peut être effectué en mémoire car il ne dépend pas de fichiers XML temporaires ou intermédiaires. Cela signifie que les grands fichiers Excel, par exemple, ceux contenant des images, des graphiques et d'autres objets de dessin, peuvent être convertis rapidement et efficacement.

{{% alert color="primary" %}}

Si le classeur contient des formules, il est préférable d'appeler la méthode [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) juste avant le rendu en PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertXLSFileToPDF-ConvertXLSFileToPDF.java" >}}

## Articles Connexes

- [Convertir un fichier Excel au format PDF compatible avec PDFA-1a](/cells/fr/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Rendu du graphique](/cells/fr/java/chart-rendering/)
