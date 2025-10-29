---
title: Convertir un fichier XLS avec images ou graphiques en PDF avec Golang via C++
linktitle: Convertir un fichier XLS avec des images ou des graphiques en PDF
type: docs
weight: 50
url: /fr/go-cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Convertir des fichiers XLS contenant des images ou des graphiques en documents PDF en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}} 

Aspose.Cells supporte la conversion des fichiers XLS contenant des images et des graphiques en documents PDF. Aspose.Cells for C++ peut fonctionner indépendamment pour convertir une feuille de calcul en PDF : Aspose.PDF pour C++ n'est pas requis pour la conversion. Le processus peut être effectué en mémoire car il ne dépend pas de fichiers XML temporaires ou intermédiaires. Cela signifie que de gros fichiers Excel, par exemple ceux contenant des images, des graphiques et d'autres objets de dessin, peuvent être convertis rapidement et efficacement.

{{% /alert %}} 
## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsFileWithImagesOrChartsToPdf.go" >}}
{{% alert color="primary" %}} 

Si la feuille de calcul contient des formules, il est préférable d'appeler la méthode [Calculate(CalculationData data)](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) juste avant de rendre en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont affichées dans le PDF.

{{% /alert %}}
