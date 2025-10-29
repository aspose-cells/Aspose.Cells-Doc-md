---
title: Convertir un fichier XLS avec des images ou des graphiques en PDF
type: docs
weight: 50
url: /fr/python-net/convert-xls-file-with-images-or-charts-to-pdf/
description: Apprenez à convertir un fichier XLS avec des images ou des graphiques au format PDF avec l API Aspose.Cells pour Python via .NET.
keywords: Convertir un fichier XLS avec des images ou des graphiques au format PDF en Python, Convertir xls en pdf en utilisant Python, fichier XLS avec des images en PDF, fichier xls avec des graphiques en PDF en python, python xls en pdf
---

{{% alert color="primary" %}} 

Aspose.Cells pour Python via .NET prend en charge la conversion de fichiers XLS contenant des images et des graphiques en documents PDF. L'API Aspose.Cells pour Python via .NET peut travailler de manière autonome pour convertir une feuille de calcul en PDF : Aspose.PDF pour .NET n'est pas requis pour la conversion. Le processus peut être effectué en mémoire car il ne dépend pas de fichiers XML temporaires ou intermédiaires. Cela signifie que les grands fichiers Excel, par exemple ceux contenant des images, des graphiques et d'autres objets de dessin, peuvent être convertis rapidement et efficacement.

{{% /alert %}} 
## **Code d'exemple**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXLSFileToPDF-1.py" >}}

{{% alert color="primary" %}} 

Si la feuille de calcul contient des formules, il est préférable d'appeler la méthode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant le rendu en PDF. Ce faisant, on s'assure que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
