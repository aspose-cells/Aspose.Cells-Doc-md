---
title: Rééchantillonner les images ajoutées  Conversion Excel en PDF
type: docs
weight: 150
url: /fr/python-net/resample-added-images-excel-to-pdf-conversion/
description: Apprenez comment rééchantillonner les images ajoutées lors de la conversion d Excel en PDF avec Aspose.Cells pour Python via .NET API.
keywords: Rééchantillonner les images ajoutées en Python lors de la conversion d Excel en PDF
---

{{% alert color="primary" %}}

Lorsque vous travaillez avec de gros fichiers Microsoft Excel contenant de nombreuses images, vous pourriez avoir besoin de compresser les images ajoutées pour réduire la taille du fichier PDF en sortie et améliorer les performances de conversion globales. Aspose.Cells pour Python via .NET prend en charge le rééchantillonnage des images ajoutées pour réduire la taille du fichier PDF en sortie et améliorer quelque peu les performances.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant qui décrit comment effectuer la tâche à l'aide de l'API Aspose.Cells pour Python via .NET. L'exemple convertit un fichier Microsoft Excel en un fichier PDF tout en compressant les images dans le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

En utilisant l'option [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int), la taille du PDF de sortie est minimisée mais cela peut affecter légèrement la qualité de l'image.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
