---
title: Limitez le nombre de pages générées  Conversion Excel en PDF
type: docs
weight: 60
url: /fr/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez imprimer une plage de pages dans un fichier PDF de sortie. Aspose.Cells a la capacité de définir une limite sur le nombre de pages générées lors de la conversion d'une feuille de calcul Excel en PDF.

{{% /alert %}}

## **Limitez le nombre de pages générées**

L'exemple suivant montre comment restituer une plage de pages (3 et 4) dans un fichier Microsoft Excel au format PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) juste avant de la rendre au format PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont rendues dans le fichier de sortie.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
