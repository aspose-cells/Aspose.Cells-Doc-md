---
title: Limitez le nombre de pages générées  Conversion Excel en PDF
type: docs
weight: 180
url: /fr/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Apprenez comment limiter le nombre de pages générées lors du rendu d Excel en PDF avec Aspose.Cells pour Python via .NET API.
keywords: Limiter le nombre de pages générées en Python lors du rendu d Excel en PDF, Limiter le nombre de pages générées en enregistrement d Excel en PDF en utilisant Python, Définir le nombre de pages générées en convertissant Excel en PDF avec Python, Contrôler le nombre de pages générées pour Excel en PDF en Python
---

{{% alert color="primary" %}}

Parfois, vous voulez imprimer une plage de pages dans un fichier PDF de sortie. Aspose.Cells pour Python via .NET a la capacité de limiter le nombre de pages générées lors de la conversion d'une feuille de calcul Excel au format de fichier PDF.

{{% /alert %}}

## **Limitez le nombre de pages générées**

L'exemple suivant montre comment restituer une plage de pages (3 et 4) dans un fichier Microsoft Excel au format PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

Si le classeur contient des formules, il est préférable d'appeler la méthode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de le rendre en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont rendues dans le fichier de sortie.

{{% /alert %}}
