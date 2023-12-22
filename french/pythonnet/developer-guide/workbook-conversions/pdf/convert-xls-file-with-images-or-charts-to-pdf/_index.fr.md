---
title: Convertir un fichier XLS avec des images ou des graphiques en PDF
type: docs
weight: 50
url: /fr/python-net/convert-xls-file-with-images-or-charts-to-pdf/
description: Découvrez comment convertir un fichier XLS contenant des images ou des graphiques en PDF avec Aspose.Cells for Python via .NET API.
keywords: Python Convert XLS File with Images or Charts to PDF, Convert xls to pdf using Python, Python XLS file with images to pdf, xls file with charts to pdf in python, python xls to pdf
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET prend en charge la conversion de fichiers XLS contenant des images et des graphiques en documents PDF. Aspose.Cells for Python via .NET API peut fonctionner indépendamment pour convertir une feuille de calcul en PDF : Aspose.PDF for .NET n'est pas requis pour la conversion. Le processus peut être effectué en mémoire car le processus ne dépend pas de fichiers XML temporaires ou intermédiaires. Cela signifie que les fichiers Excel volumineux, par exemple ceux contenant des images, des graphiques et d'autres objets de dessin, peuvent être convertis rapidement et efficacement.

{{% /alert %}} 
##  **Exemple de code**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXLSFileToPDF-1.py" >}}

{{% alert color="primary" %}} 

 Si la feuille de calcul contient des formules, il est préférable d'appeler la[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant le rendu vers PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
