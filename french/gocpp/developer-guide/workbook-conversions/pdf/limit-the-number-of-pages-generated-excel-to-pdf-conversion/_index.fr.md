---
title: Limiter le nombre de pages générées  Conversion Excel en PDF avec Golang via C++
linktitle: Limiter le nombre de pages générées
type: docs
weight: 180
url: /fr/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Apprenez comment limiter le nombre de pages générées lors de la conversion d Excel en PDF en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Parfois, vous souhaitez imprimer une plage de pages dans un fichier PDF de sortie. Aspose.Cells a la capacité de limiter le nombre de pages générées lors de la conversion d'une feuille de calcul Excel au format de fichier PDF.

{{% /alert %}}

## **Limitez le nombre de pages générées**

L'exemple suivant montre comment restituer une plage de pages (3 et 4) dans un fichier Microsoft Excel au format PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) juste avant de la convertir au format PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et les valeurs correctes sont rendues dans le fichier de sortie.

{{% /alert %}}
