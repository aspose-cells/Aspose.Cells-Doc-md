---
title: Supprimer les espaces blancs des données avant de les rendre en image
type: docs
weight: 270
url: /fr/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

Parfois, vous devez présenter des images de feuilles de calcul dans des applications ou des pages web. Par exemple, vous pourriez avoir besoin d'insérer une image dans un document Word, un fichier PDF, une présentation PowerPoint ou tout autre document. Fondamentalement, vous souhaitez rendre une feuille de calcul sous forme d'image pour pouvoir la coller dans d'autres applications. Les APIs Aspose.Cells vous permettent de convertir les feuilles de calcul Microsoft Excel en images.

{{% /alert %}}

La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) est capable de convertir une feuille de calcul en un fichier image avec des attributs spécifiés, par exemple, le format d'image, les feuilles paginées, etc. Plusieurs formats d'image sont pris en charge, notamment BMP, GIF, JPG, TIFF, et EMF.

Lorsque vous utilisez la fonction de feuille à image, l'image de sortie a par défaut un espace blanc/vide, c'est-à-dire une bordure, autour d'elle. Vous pouvez supprimer cela. Définissez les marges de mise en page supérieure, gauche, inférieure et droite pour la feuille source à 0 et spécifiez les attributs [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) en conséquence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
{{< app/cells/assistant language="java" >}}
