---
title: Image
type: docs
weight: 300
url: /fr/net/convert-excel-to-image/
---


{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter une feuille de calcul du classeur et de la convertir en différents formats. Cet article explique comment convertir une feuille de calcul en différents formats.

{{% /alert %}}

## Conversion du classeur en TIFF

Un fichier Excel peut contenir plusieurs feuilles avec plusieurs pages. [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) vous permet de convertir Excel en TIFF avec plusieurs pages. Vous pouvez également contrôler plusieurs options pour TIFF, comme [Compression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Profondeur de couleur](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Résolution ([Résolution horizontale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Résolution verticale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

Le code ci-dessous montre comment convertir Excel en TIFF avec plusieurs pages. Les [fichier Excel source](workbook-to-tiff-with-mulitiple-pages.xlsx) et [image TIFF générée](workbook-to-tiff-with-mulitiple-pages.tiff) sont joints à titre de référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Conversion de la feuille de calcul en image**

Les feuilles de calcul contiennent des données que vous souhaitez analyser. Par exemple, une feuille de calcul peut contenir des paramètres, des totaux, des pourcentages, des exceptions et des calculs.

En tant que développeur, vous pourriez avoir besoin de présenter des feuilles de calcul sous forme d'images. Par exemple, vous pourriez avoir besoin d'utiliser une image d'une feuille de calcul dans une application ou une page Web. Vous pourriez vouloir insérer une image dans un document Microsoft Word, un fichier PDF, une présentation PowerPoint ou tout autre type de document. En bref, vous voulez qu'une feuille de calcul soit rendue sous forme d'image afin de pouvoir l'utiliser ailleurs.

Aspose.Cells prend en charge la conversion des feuilles de calcul Excel en images. Pour utiliser cette fonctionnalité, vous devez importer l'espace de noms [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) dans votre programme ou projet. Il a plusieurs classes précieuses pour le rendu et l'impression, par exemple [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), et d'autres.

La classe [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) représente une feuille de calcul à convertir en images. Elle dispose d'une méthode surchargée, [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index), qui peut convertir une feuille de calcul en fichier(s) image avec différents attributs ou options. Elle renvoie un objet System.Drawing.Bitmap et vous pouvez enregistrer un fichier image sur le disque ou le flux. Plusieurs formats d'image sont pris en charge, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

Actuellement, l'API de conversion des feuilles de calcul en images ne prend pas en charge les graphiques à bulles en 3D.

{{% /alert %}}

## **Conversion de feuille de calcul en SVG**

SVG signifie Scalable Vector Graphics. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

Aspose.Cells for .NET a été capable de convertir des feuilles de calcul en image SVG depuis la version 7.1.0. L'extrait de code suivant montre comment convertir une feuille de calcul dans un fichier Excel en un fichier image SVG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Sujets avancés**
- [Convertir un graphique Excel en image](/cells/fr/net/convert-an-excel-chart-to-image/)
- [Conversion de graphique en image au format SVG](/cells/fr/net/converting-chart-to-image-in-svg-format/)
- [Exportation du graphique en SVG avec l'attribut viewBox](/cells/fr/net/export-chart-to-svg-with-viewbox-attribute/)
- [Suivre la progression de la conversion d'Excel en TIFF](/cells/fr/net/track-conversion-progress-of-excel-to-tiff/)
