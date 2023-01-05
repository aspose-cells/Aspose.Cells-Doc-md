---
title: Image
type: docs
weight: 300
url: /fr/net/convert-excel-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter une feuille de calcul à partir du classeur et de la convertir en différents formats. Cet article explique comment convertir une feuille de calcul en différents formats.

{{% /alert %}}

## Conversion du classeur en TIFF

 Un fichier Excel peut contenir plusieurs feuilles avec plusieurs pages.[ClasseurRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) vous permet de convertir Excel en TIFF avec plusieurs pages. En outre, vous pouvez contrôler plusieurs options pour TIFF, comme[Compression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [La profondeur de la couleur](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Résolution([Résolution horizontale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Résolution verticale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

 L'extrait de code suivant montre comment convertir Excel en TIFF avec plusieurs pages. Le[fichier Excel source](workbook-to-tiff-with-mulitiple-pages.xlsx) et[image générée TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) sont joints pour votre référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Conversion d'une feuille de calcul en image**

Les feuilles de calcul contiennent des données que vous souhaitez analyser. Par exemple, une feuille de calcul peut contenir des paramètres, des totaux, des pourcentages, des exceptions et des calculs.

En tant que développeur, vous devrez peut-être présenter des feuilles de calcul sous forme d'images. Par exemple, vous devrez peut-être utiliser l'image d'une feuille de calcul dans une application ou une page Web. Vous pouvez insérer une image dans un document Word Microsoft, un fichier PDF, une présentation PowerPoint ou un autre type de document. En termes simples, vous voulez qu'une feuille de calcul soit rendue sous forme d'image afin que vous puissiez l'utiliser ailleurs.

Aspose.Cells prend en charge la conversion des feuilles de calcul Excel en images. Pour utiliser cette fonction, vous devez importer le**[Aspose.Cells.Rendu](https://reference.aspose.com/cells/net/aspose.cells.rendering)** namespace à votre programme ou projet. Il a plusieurs classes utiles pour le rendu et l'impression, par exemple**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, **[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)**, et d'autres.

 Le**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)** La classe représente une feuille de calcul à afficher sous forme d'images. Il a une méthode surchargée,**[ToImage](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)**qui peuvent convertir une feuille de calcul en fichier(s) image avec différents attributs ou options. Il renvoie un objet System.Drawing.Bitmap et vous pouvez enregistrer un fichier image sur le disque ou le flux. Plusieurs formats d'image sont pris en charge, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

L'extrait de code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

À l'heure actuelle, le API pour la conversion des feuilles de calcul en images ne prend pas en charge les graphiques à bulles 3D.

{{% /alert %}}

## **Conversion de la feuille de calcul en SVG**

SVG signifie Scalable Vector Graphics. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'un standard ouvert développé par le World Wide Web Consortium (W3C) depuis 1999.

Aspose.Cells for .NET est capable de convertir des feuilles de calcul en image SVG depuis la version 7.1.0. L'extrait de code suivant montre comment convertir une feuille de calcul dans un fichier Excel en un fichier image SVG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Sujets avancés**
- [Convertir un graphique Excel en image](/cells/fr/net/convert-an-excel-chart-to-image/)
- [Conversion d'un graphique en image au format SVG](/cells/fr/net/converting-chart-to-image-in-svg-format/)
- [Exporter le graphique vers SVG avec l'attribut viewBox](/cells/fr/net/export-chart-to-svg-with-viewbox-attribute/)
- [Suivre la progression de la conversion d'Excel vers TIFF](/cells/fr/net/track-conversion-progress-of-excel-to-tiff/)
