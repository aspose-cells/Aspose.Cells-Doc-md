---
title: Convertir la feuille de calcul en image - Supprimer les espaces autour des données
type: docs
weight: 40
url: /fr/net/convert-worksheet-to-image-remove-whitespace-around-data/
---
{{% alert color="primary" %}}

Parfois, vous devez présenter des images de feuille de calcul dans des applications ou des pages Web. Par exemple, vous devrez peut-être insérer des images dans un document Word, un fichier PDF, une présentation PowerPoint ou un autre document. Fondamentalement, vous souhaitez rendre une feuille de calcul sous forme d'image afin qu'elle puisse être collée dans d'autres applications. Aspose.Cells vous permet de convertir des feuilles de calcul Excel Microsoft en images.

{{% /alert %}}

## **Supprimer les espaces autour des données**

 La[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)API convertit une feuille de calcul en un fichier image avec tous les attributs spécifiés, par exemple, format d'image, feuilles paginées, etc. Plusieurs formats d'image sont pris en charge, notamment BMP, GIF, JPG, TIFF et EMF.

 Lorsque vous utilisez la fonction feuille vers image, l'image de sortie est entourée par défaut d'un espace, c'est-à-dire d'une bordure. Vous pouvez supprimer cela en définissant les marges de mise en page supérieure, inférieure, gauche et droite de la feuille de calcul source sur 0 et en spécifiant[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)attributs en conséquence.

L'extrait de code suivant supprime l'espace autour des données dans l'image de sortie.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

