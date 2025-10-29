---
title: Conversion de Feuille de Calcul dans Différents Formats d Image
type: docs
weight: 90
url: /fr/go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter une feuille de calcul à partir d'un classeur et de la convertir dans différents formats d'image. Cet article explique comment convertir une feuille de calcul dans différents formats d'image.

{{% /alert %}}

## **Conversion de la feuille de calcul en image**

Les feuilles de calcul contiennent des données que vous souhaitez analyser. Par exemple, une feuille de calcul peut contenir des paramètres, des totaux, des pourcentages, des exceptions et des calculs.

En tant que développeur, vous pourriez avoir besoin de présenter des feuilles de calcul sous forme d'images. Par exemple, vous pourriez avoir besoin d'utiliser une image d'une feuille dans une application ou une page web. Vous souhaitez peut-être insérer une image dans un document Microsoft Word, un fichier PDF, une présentation PowerPoint ou tout autre type de document. En résumé, vous souhaitez que la feuille soit rendue sous forme d'image afin de pouvoir l'utiliser ailleurs.

Aspose.Cells prend en charge la conversion des feuilles Excel en images. Pour utiliser cette fonctionnalité, vous devez importer l'espace de noms [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) dans votre programme ou projet. Il comprend plusieurs classes utiles pour le rendu et l'impression, par exemple, [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), et d'autres.

La classe [Aspose.Cells.Rendering.ISheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) représente une feuille à rendre sous forme d'images. Elle possède une méthode surchargée, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), qui peut convertir une feuille en fichier(s) image avec différents attributs ou options. Plusieurs formats d'image sont supportés, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF et EMF.

Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image.

### ** convertir Excel/spreadsheet en PNG avec GoLang**

Veuillez consulter le code d'exemple suivant, son [fichier Excel d'exemple](67338402.xlsx) et les [images PNG de sortie](67338401.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### ** convertir Excel/spreadsheet en TIFF avec GoLang**

Veuillez consulter le code d'exemple suivant, son [fichier Excel d'exemple](67338402.xlsx) et l'[image TIFF de sortie](67338419.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## ** convertir Excel/spreadsheet en SVG avec GoLang**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Svg.go" >}}

SVG signifie Scalable Vector Graphics. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

Aspose.Cells for Go via C++ a pu convertir des feuilles en images SVG depuis la version 24.12.0.

Pour utiliser cette fonctionnalité, importez l'espace de noms `Aspose.Cells.Rendering` dans votre programme ou projet. Il dispose de plusieurs classes précieuses pour le rendu et l'impression, par exemple `ISheetRender`, `IImageOrPrintOptions`, et d'autres.

La classe `Aspose.Cells.Rendering.IImageOrPrintOptions` spécifie que la feuille de calcul sera enregistrée au format SVG. Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image SVG

Veuillez consulter le code d'exemple suivant, son [fichier Excel d'exemple](67338402.xlsx) et les [images SVG de sortie](67338403.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}
