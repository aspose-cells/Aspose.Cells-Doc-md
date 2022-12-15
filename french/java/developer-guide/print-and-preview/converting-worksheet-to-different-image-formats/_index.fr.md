---
title: Conversion d'une feuille de calcul en différents formats d'image
type: docs
weight: 30
url: /fr/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter une feuille de calcul à partir du classeur et de la convertir en différents formats. Cet article explique comment convertir une feuille de calcul en différents formats.

{{% /alert %}}

## **Conversion d'une feuille de calcul en image**

Parfois, il est utile d'enregistrer une image d'une feuille de calcul. Les images peuvent être partagées en ligne, insérées dans d'autres documents (rapports rédigés en Microsoft Word, par exemple, ou PowerPoint présentations).

Aspose.Cells fournit l'exportation d'images via le**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** classer. Cette classe représente la feuille de calcul qui sera rendue à une image. La**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** la classe fournit la**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**méthode pour convertir une feuille de calcul en un fichier image. Les formats BMP, PNG, JPEG, TIFF et EMF sont pris en charge.

{{% alert color="primary" %}}

Aspose.Cells for Java prend également en charge la conversion au format TIFF. Pour convertir une feuille de calcul en image TIFF, ajoutez la bibliothèque JAI à votre chemin de classe.

{{% /alert %}} {{% alert color="primary" %}}

À l'heure actuelle, la feuille de calcul de conversion en image API ne prend pas en charge les graphiques à bulles 3D.

{{% /alert %}}

Le code ci-dessous montre comment convertir une feuille de calcul dans un fichier Excel Microsoft en un fichier PNG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Conversion d'une feuille de calcul en SVG**

 SVG signifie**Image Vectorielle**. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'un standard ouvert développé par le World Wide Web Consortium (W3C) depuis 1999.

Depuis la sortie de la v7.1.0,**Aspose.Cells for Java** peut convertir des feuilles de calcul en images SVG.

Pour utiliser cette fonctionnalité, vous devez importer l'espace de noms com.aspose.cells dans votre programme ou projet. Il a plusieurs classes utiles pour le rendu et l'impression, par exemple,**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**, et d'autres.

La**[com.aspose.cells.ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** classe spécifie que la feuille de calcul sera enregistrée au format SVG.

La**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**la classe prend l'objet de**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** en tant que paramètre qui définit le format de sauvegarde au format SVG.

L'extrait de code suivant montre comment convertir une feuille de calcul dans un fichier Excel en un fichier image SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Afficher la feuille de calcul active dans un classeur**

Un moyen simple de convertir une feuille de calcul active dans un classeur consiste à définir l'index de la feuille active, puis à enregistrer le classeur au format SVG. Il rendra la feuille active en SVG. L'exemple de code suivant illustre cette fonctionnalité :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Articles Liés

- [Exporter le graphique vers SVG avec l'attribut viewBox](/cells/fr/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exporter une feuille de calcul ou un graphique dans une image avec la largeur et la hauteur souhaitées](/cells/fr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page](/cells/fr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
