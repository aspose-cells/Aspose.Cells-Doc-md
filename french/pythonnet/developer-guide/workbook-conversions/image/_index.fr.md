---
title: Image
type: docs
weight: 300
url: /fr/python-net/convert-excel-to-image/
description: Convertissez le graphique en Image en utilisant Aspose.Cells for Python via .NET API.
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET vous permet d'exporter une feuille de calcul à partir du classeur et de la convertir en différents formats. Cet article explique comment convertir une feuille de calcul en différents formats.

{{% /alert %}}

##  Conversion du classeur en TIFF

 Un fichier Excel peut contenir plusieurs feuilles de plusieurs pages.[Rendu du classeur](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) vous permet de convertir Excel en TIFF avec plusieurs pages. En outre, vous pouvez contrôler plusieurs options pour TIFF, comme[Compression](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [La profondeur de la couleur](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Résolution([Résolution horizontale](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Résolution verticale](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

 L'extrait de code suivant montre comment convertir Excel en TIFF avec plusieurs pages. Le[fichier Excel source](workbook-to-tiff-with-mulitiple-pages.xlsx) et[image générée TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) sont joints pour votre référence.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

##  **Conversion d'une feuille de calcul en Image**

Les feuilles de calcul contiennent des données que vous souhaitez analyser. Par exemple, une feuille de calcul peut contenir des paramètres, des totaux, des pourcentages, des exceptions et des calculs.

En tant que développeur, vous devrez peut-être présenter des feuilles de calcul sous forme d'images. Par exemple, vous devrez peut-être utiliser l'image d'une feuille de calcul dans une application ou une page Web. Vous souhaiterez peut-être insérer une image dans un document Word Microsoft, un fichier PDF, une présentation PowerPoint ou un autre type de document. En termes simples, vous souhaitez qu'une feuille de calcul soit rendue sous forme d'image afin de pouvoir l'utiliser ailleurs.

Aspose.Cells for Python via .NET prend en charge la conversion de feuilles de calcul Excel en images. Pour utiliser cette fonctionnalité, vous devez importer le**[aspose.cells.rendering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)**espace de noms à votre programme ou projet. Il possède plusieurs classes utiles pour le rendu et l'impression, par exemple *[Rendu de feuille](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**, *[OptionsImageOuImpression](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)**, *[Rendu du classeur](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)**, et d'autres.

 Le**[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**la classe représente une feuille de calcul à restituer sous forme d'images. Il a une méthode surchargée, *[vers_image](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)**, qui peut convertir une feuille de calcul en fichier(s) image avec différents attributs ou options. Il renvoie un objet System.Drawing.Bitmap et vous pouvez enregistrer un fichier image sur le disque ou en streaming. Plusieurs formats d'images sont pris en charge, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

L'extrait de code suivant montre comment convertir une feuille de calcul d'un fichier Excel en fichier image.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

À l'heure actuelle, le API pour la conversion de feuilles de calcul en images ne prend pas en charge les graphiques à bulles 3D.

{{% /alert %}}

##  **Conversion d'une feuille de calcul en SVG**

SVG signifie Graphiques vectoriels évolutifs. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'un standard ouvert développé par le World Wide Web Consortium (W3C) depuis 1999.

Aspose.Cells for Python via .NET peut convertir des feuilles de calcul en image SVG depuis la version 7.1.0. L'extrait de code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image SVG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

##  **Sujets avancés**
- [Convertir un graphique Excel en Image](/cells/fr/python-net/convert-an-excel-chart-to-image/)
- [Conversion du graphique en Image au format SVG](/cells/fr/python-net/converting-chart-to-image-in-svg-format/)
- [Exporter le graphique vers SVG avec l'attribut viewBox](/cells/fr/python-net/export-chart-to-svg-with-viewbox-attribute/)
