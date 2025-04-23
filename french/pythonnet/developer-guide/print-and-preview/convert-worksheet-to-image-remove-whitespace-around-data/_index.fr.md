---
title: Convertir la feuille de calcul en image  Supprimer les espaces blancs autour des données
type: docs
weight: 40
url: /fr/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

Parfois, vous devez présenter des images de feuilles de calcul dans des applications ou des pages web. Par exemple, vous pourriez avoir besoin d’insérer des images dans un document Word, un fichier PDF, une présentation PowerPoint ou un autre document. En gros, vous souhaitez rendre une feuille de calcul en tant qu’image afin de pouvoir la coller dans d’autres applications. Aspose.Cells pour Python via .NET vous permet de convertir des feuilles de calcul Microsoft Excel en images.

{{% /alert %}}

## **Supprimer les espaces vides autour des données**

L'API [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) convertit une feuille de calcul en un fichier image avec les attributs spécifiés, par exemple, le format de l'image, les feuilles paginées, etc. Plusieurs formats d'image sont pris en charge, notamment BMP, GIF, JPG, TIFF et EMF.

Lorsque vous utilisez la fonction de feuille à image, l'image de sortie comporte par défaut des espaces vides, c'est-à-dire une bordure. Vous pouvez supprimer cela en définissant les marges de mise en page supérieure, inférieure, gauche et droite pour la feuille source sur 0 et en spécifiant les attributs [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) en conséquence.

Le code suivant supprime les espaces vides autour des données dans l'image de sortie.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

