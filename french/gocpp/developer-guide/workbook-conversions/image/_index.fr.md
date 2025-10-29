---
title: Convertir Excel en image avec Golang via C++
linktitle: Convertir Excel en Image
type: docs
weight: 300
url: /fr/go-cpp/convert-excel-to-image/
description: Apprenez à convertir les feuilles de calcul Excel en images, y compris les formats TIFF et SVG, en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter une feuille de calcul du classeur et de la convertir en différents formats. Cet article explique comment convertir une feuille de calcul en différents formats.

{{% /alert %}}

## Conversion du classeur en TIFF

Un fichier Excel peut contenir plusieurs feuilles avec plusieurs pages. [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) vous permet de convertir Excel en TIFF avec plusieurs pages. De plus, vous pouvez contrôler plusieurs options pour TIFF, comme [Compression](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Résolution ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

Le code ci-dessous montre comment convertir Excel en TIFF avec plusieurs pages. Les [fichier Excel source](workbook-to-tiff-with-mulitiple-pages.xlsx) et [image TIFF générée](workbook-to-tiff-with-mulitiple-pages.tiff) sont joints à titre de référence.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image.go" >}}
## **Conversion de la feuille de calcul en image**

Les feuilles de calcul contiennent des données que vous souhaitez analyser. Par exemple, une feuille de calcul peut contenir des paramètres, des totaux, des pourcentages, des exceptions et des calculs.

En tant que développeur, vous pourriez avoir besoin de présenter des feuilles de calcul sous forme d'images. Par exemple, vous pourriez avoir besoin d'utiliser une image d'une feuille de calcul dans une application ou une page Web. Vous pourriez vouloir insérer une image dans un document Microsoft Word, un fichier PDF, une présentation PowerPoint ou tout autre type de document. En bref, vous voulez qu'une feuille de calcul soit rendue sous forme d'image afin de pouvoir l'utiliser ailleurs.

Aspose.Cells prend en charge la conversion des feuilles de calcul Excel en images. Pour utiliser cette fonctionnalité, vous devez importer l'espace de noms [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/) dans votre programme ou projet. Il dispose de plusieurs classes précieuses pour le rendu et l'impression, par exemple [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/), et d'autres.

La classe [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/) représente une feuille de calcul à rendre sous forme d'images. Elle dispose d'une méthode surchargée, [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage/), qui peut convertir une feuille de calcul en fichier(s) image avec différents attributs ou options. Elle retourne un objet `System.Drawing.Bitmap` et vous pouvez enregistrer un fichier image sur le disque ou en flux. Plusieurs formats d'image sont pris en charge, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-1.go" >}}
{{% alert color="primary" %}}

Actuellement, l'API de conversion des feuilles de calcul en images ne prend pas en charge les graphiques à bulles en 3D.

{{% /alert %}}

## **Conversion de feuille de calcul en SVG**

SVG signifie Scalable Vector Graphics. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

Aspose.Cells for C++ a été capable de convertir des feuilles de calcul en SVG depuis la version 7.1.0. Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en une image SVG.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-2.go" >}}
## **Sujets avancés**
- [Convertir un graphique Excel en image](/cells/fr/cpp/convert-an-excel-chart-to-image/)
- [Conversion de graphique en image au format SVG](/cells/fr/cpp/converting-chart-to-image-in-svg-format/)
- [Exportation du graphique en SVG avec l'attribut viewBox](/cells/fr/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Suivre la progression de la conversion d'Excel en TIFF](/cells/fr/cpp/track-conversion-progress-of-excel-to-tiff/)
