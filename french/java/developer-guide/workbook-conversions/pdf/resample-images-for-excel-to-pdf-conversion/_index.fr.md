---
title: Rééchantillonner les images pour la conversion Excel en PDF
type: docs
weight: 250
url: /fr/java/resample-images-for-excel-to-pdf-conversion/
description: Cet article montre comment réduire la taille des images lors de la conversion de fichiers Excel en PDF.
keywords: excel en pdf, rééchantillonner les images pendant la conversion excel en pdf, compresser les images pendant la conversion excel en pdf, réduire la taille des images pendant la conversion excel en pdf, convertir excel en pdf avec une taille plus petite, conversion de excel en pdf avec rééchantillonnage d images, conversion de excel en pdf avec compression d images, rééchantillonner les images pendant la conversion excel en pdf java
---

{{% alert color="primary" %}}

Lorsque vous travaillez avec de gros fichiers Microsoft Excel contenant de nombreuses images, vous pouvez avoir besoin de compresser les images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer les performances de conversion globales. Aspose.Cells prend en charge le rééchantillonnage des images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer les performances.

{{% /alert %}}

## **Rééchantillonner les images pour la conversion Excel en PDF**

Veuillez consulter le code d'exemple suivant qui décrit comment effectuer la tâche à l'aide de l'API Aspose.Cells. L'exemple convertit un fichier Microsoft Excel en un fichier PDF tout en compressant les images dans le fichier.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

L'utilisation de l'option [**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) minimise la taille du PDF de sortie mais peut affecter légèrement la qualité de l'image.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
