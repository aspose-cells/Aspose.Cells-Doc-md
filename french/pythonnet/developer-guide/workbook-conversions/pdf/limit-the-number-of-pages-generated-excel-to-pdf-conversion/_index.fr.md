---
title: Limiter le nombre de pages générées - Conversion Excel à PDF
type: docs
weight: 180
url: /fr/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Découvrez comment limiter le nombre de pages générées lors du rendu Excel à PDF avec Aspose.Cells for Python via .NET API.
keywords: Python Limit the Number of Pages Generated while Rendering Excel to PDF, Limit the Number of Pages Generated while saving Excel to PDF using Python, Python Set the Number of Pages Generated while converting Excel to PDF, Control the Number of Pages Generated for Excel to PDF in python
---
{{% alert color="primary" %}}

Parfois, vous souhaitez imprimer une plage de pages dans un fichier de sortie PDF. Aspose.Cells for Python via .NET a la possibilité de définir une limite sur le nombre de pages générées lors de la conversion d'une feuille de calcul Excel au format de fichier PDF.

{{% /alert %}}

##  **Limiter le nombre de pages générées**

L'exemple suivant montre comment restituer une plage de pages (3 et 4) d'un fichier Excel Microsoft vers PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

 Si la feuille de calcul contient des formules, il est préférable d'appeler[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de le rendre à PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le fichier de sortie.

{{% /alert %}}
