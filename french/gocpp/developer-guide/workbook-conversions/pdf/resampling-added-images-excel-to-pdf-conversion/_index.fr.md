---
title: Resampling des images ajoutées  Conversion d Excel en PDF avec Golang via C++
linktitle: Rééchantillonnage des images ajoutées  Conversion d Excel en PDF
type: docs
weight: 150
url: /fr/go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Découvrez comment rééchantillonner les images ajoutées pour réduire la taille du PDF en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Lorsque vous travaillez avec de gros fichiers Microsoft Excel comportant de nombreuses images, vous devrez peut-être compresser les images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer les performances globales de conversion. Aspose.Cells prend en charge le rééchantillonnage des images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer quelque peu les performances.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant qui décrit comment effectuer la tâche à l'aide de l'API Aspose.Cells. L'exemple convertit un fichier Microsoft Excel en un fichier PDF tout en compressant les images dans le fichier.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

L'utilisation de l'option [**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/) minimise la taille du PDF de sortie mais peut affecter légèrement la qualité de l'image.

{{% /alert %}} 

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}

