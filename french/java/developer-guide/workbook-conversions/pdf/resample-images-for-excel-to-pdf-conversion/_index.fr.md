---
title: Rééchantillonner les images pour la conversion Excel vers PDF
type: docs
weight: 250
url: /fr/java/resample-images-for-excel-to-pdf-conversion/
description: Cet article montre comment réduire la taille des images lors de la conversion de fichiers Excel en PDF
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

Lorsque vous travaillez avec de gros fichiers Excel Microsoft contenant de nombreuses images, vous devrez peut-être compresser les images qui ont été ajoutées pour réduire la taille du fichier de sortie PDF et améliorer les performances de conversion globales. Aspose.Cells prend en charge le rééchantillonnage des images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer les performances.

{{% /alert %}}

## **Rééchantillonner les images pour la conversion Excel vers PDF**

Veuillez consulter l'exemple de code suivant qui décrit comment effectuer la tâche à l'aide du Aspose.Cells API. L'exemple convertit un fichier Excel Microsoft en un fichier PDF tout en compressant les images dans le fichier.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

 En utilisant le[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) minimise la taille de la sortie PDF mais cela peut affecter un peu la qualité de l'image.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le fichier PDF.

{{% /alert %}}
