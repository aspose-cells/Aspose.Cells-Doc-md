---
title: Conversion d'une feuille de calcul en différents formats d'image
type: docs
weight: 90
url: /fr/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells vous permet d'exporter une feuille de calcul à partir d'un classeur et de la convertir en différents formats d'image. Cet article explique comment convertir une feuille de calcul en différents formats d'image.

{{% /alert %}} 
##  **Conversion d'une feuille de calcul en image**
Les feuilles de calcul contiennent des données que vous souhaitez analyser. Par exemple, une feuille de calcul peut contenir des paramètres, des totaux, des pourcentages, des exceptions et des calculs.

En tant que développeur, vous devrez peut-être présenter des feuilles de calcul sous forme d'images. Par exemple, vous devrez peut-être utiliser l'image d'une feuille de calcul dans une application ou une page Web. Vous souhaiterez peut-être insérer une image dans un document Word Microsoft, un fichier PDF, une présentation PowerPoint ou un autre type de document. En termes simples, vous souhaitez qu'une feuille de calcul soit rendue sous forme d'image afin de pouvoir l'utiliser ailleurs.

Aspose.Cells prend en charge la conversion de feuilles de calcul Excel en images. Pour utiliser cette fonctionnalité, vous devez importer le[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)espace de noms à votre programme ou projet. Il possède plusieurs classes utiles pour le rendu et l'impression, par exemple :[Rendu de feuille](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [OptionsImageOuImpression](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)et d'autres.

La classe `Aspose.Cells.Rendering.ISheetRender` représente une feuille de calcul à restituer sous forme d'images. Il a une méthode surchargée,[VersImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), qui peut convertir une feuille de calcul en fichier(s) image avec différents attributs ou options. Plusieurs formats d'image sont pris en charge, par exemple BMP, PNG, GIF, JPG, JPEG, EMF.

L'extrait de code suivant montre comment convertir une feuille de calcul d'un fichier Excel en fichier image.
###  **Format PNG**
 Veuillez consulter l'exemple de code suivant, son[exemple de fichier Excel](67338402.xlsx) , et le[sortie PNG Images](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}
<!--
### **TIFF Format**
Please see the following sample code, its [sample Excel file](67338402.xlsx), and the [output TIFF Image](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}
-->
##  **Conversion d'une feuille de calcul en SVG**
SVG signifie Graphiques vectoriels évolutifs. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'un standard ouvert développé par le World Wide Web Consortium (W3C) depuis 1999.

Aspose.Cells for C++ est capable de convertir des feuilles de calcul en image SVG depuis la version 18.5.0.

Pour utiliser cette fonctionnalité, importez l'espace de noms `Aspose.Cells.Rendering` dans votre programme ou projet. Il comporte plusieurs classes utiles pour le rendu et l'impression, par exemple `ISheetRender`, `IImageOrPrintOptions` et autres.

La classe `Aspose.Cells.Rendering.IImageOrPrintOptions` précise que la feuille de calcul sera enregistrée au format SVG. L'extrait de code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image SVG.

 Veuillez consulter l'exemple de code suivant, son[exemple de fichier Excel](67338402.xlsx) , et le[sortie SVG Images](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
