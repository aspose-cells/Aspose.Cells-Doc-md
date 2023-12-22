---
title: Rééchantillonner les images ajoutées - Conversion Excel vers PDF
type: docs
weight: 150
url: /fr/python-net/resample-added-images-excel-to-pdf-conversion/
description: Apprenez à rééchantillonner les images ajoutées lors de la conversion d'Excel en PDF avec Aspose.Cells for Python via .NET API.
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

Lorsque vous travaillez avec de gros fichiers Excel Microsoft contenant de nombreuses images, vous devrez peut-être compresser les images qui ont été ajoutées pour réduire la taille du fichier PDF de sortie et améliorer les performances globales de conversion. Aspose.Cells for Python via .NET prend en charge le rééchantillonnage des images ajoutées pour réduire la taille du fichier de sortie PDF et améliorer quelque peu les performances.

{{% /alert %}}

Veuillez consulter l'exemple de code suivant qui décrit comment effectuer la tâche à l'aide du Aspose.Cells for Python via .NET API. L'exemple convertit un fichier Excel Microsoft en fichier PDF tout en compressant les images du fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

 En utilisant le[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)L'option minimise la taille de la sortie PDF mais elle peut affecter un peu la qualité de l'image.

{{% /alert %}} {{% alert color="primary" %}}

 Si votre feuille de calcul contient des formules, il est préférable d'appeler[**Classeur.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
