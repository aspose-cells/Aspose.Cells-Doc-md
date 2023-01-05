---
title: Supprimer les espaces blancs des données avant le rendu à l'image
type: docs
weight: 270
url: /fr/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---
{{% alert color="primary" %}}

Parfois, vous devez présenter des images de feuille de calcul dans des applications ou des pages Web. Par exemple, vous devrez peut-être insérer une image dans un document Word, un fichier PDF, une présentation PowerPoint ou un autre document. Fondamentalement, vous souhaitez rendre une feuille de calcul sous forme d'image afin qu'elle puisse être collée dans d'autres applications. Les API Aspose.Cells vous permettent de convertir des feuilles de calcul Excel Microsoft en images.

{{% /alert %}}

 Le[**FeuilleRendu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)est capable de convertir une feuille de calcul en un fichier image avec tous les attributs spécifiés, par exemple, format d'image, feuilles paginées, etc. Plusieurs formats d'image sont pris en charge, notamment BMP, GIF, JPG, TIFF et EMF.

 Lorsque vous utilisez la fonction feuille à image, l'image de sortie comporte un espace blanc/vide, c'est-à-dire une bordure, autour d'elle par défaut. Vous pouvez supprimer ceci. Définissez les marges de mise en page supérieure, gauche, inférieure et droite de la feuille de calcul source sur 0 et spécifiez[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)attributs en conséquence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
