---
title: Rééchantillonnage des images ajoutées  Conversion d Excel en PDF
type: docs
weight: 150
url: /fr/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Lorsque vous travaillez avec de gros fichiers Microsoft Excel comportant de nombreuses images, vous devrez peut-être compresser les images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer les performances globales de conversion. Aspose.Cells prend en charge le rééchantillonnage des images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer quelque peu les performances.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant qui décrit comment effectuer la tâche à l'aide de l'API Aspose.Cells. L'exemple convertit un fichier Microsoft Excel en un fichier PDF tout en compressant les images dans le fichier.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

En utilisant l'option [**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample), la taille du PDF de sortie est minimisée mais cela peut affecter légèrement la qualité de l'image.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
