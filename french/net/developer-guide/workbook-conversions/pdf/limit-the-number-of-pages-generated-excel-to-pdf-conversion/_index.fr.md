---
title: Limitez le nombre de pages générées  Conversion Excel en PDF
type: docs
weight: 180
url: /fr/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez imprimer une plage de pages dans un fichier PDF de sortie. Aspose.Cells a la capacité de limiter le nombre de pages générées lors de la conversion d'une feuille de calcul Excel au format de fichier PDF.

{{% /alert %}}

## **Limitez le nombre de pages générées**

L'exemple suivant montre comment restituer une plage de pages (3 et 4) dans un fichier Microsoft Excel au format PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) juste avant de la convertir au format PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et les valeurs correctes sont rendues dans le fichier de sortie.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
