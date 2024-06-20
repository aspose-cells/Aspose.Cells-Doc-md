---
title: Conversion de Feuille de Calcul dans Différents Formats d Image
type: docs
weight: 30
url: /fr/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter une feuille de calcul du classeur et de la convertir en différents formats. Cet article explique comment convertir une feuille de calcul en différents formats.

{{% /alert %}}

## **Conversion de la feuille de calcul en image**

Parfois, il est utile de sauvegarder une image d'une feuille de calcul. Les images peuvent être partagées en ligne, insérées dans d'autres documents (rapports rédigés dans Microsoft Word, par exemple, ou présentations PowerPoint).

Aspose.Cells fournit l'exportation d'images via la classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). Cette classe représente la feuille de calcul qui sera rendue sous forme d'image. La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) fournit la méthode [**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) pour convertir une feuille de calcul en un fichier image. Les formats BMP, PNG, JPEG, TIFF et EMF sont pris en charge.

{{% alert color="primary" %}}

Aspose.Cells for Java prend également en charge la conversion au format TIFF. Pour convertir une feuille de calcul en une image TIFF, ajoutez la bibliothèque JAI à votre chemin de classe.

{{% /alert %}} {{% alert color="primary" %}}

Actuellement, l'API de conversion de feuille de calcul en image ne prend pas en charge les graphiques en bulles 3D.

{{% /alert %}}

Le code ci-dessous montre comment convertir une feuille de calcul dans un fichier Microsoft Excel en un fichier PNG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Conversion de feuille de calcul en SVG**

SVG signifie Scalable Vector Graphics. SVG est une spécification basée sur des normes XML pour les graphiques vectoriels en deux dimensions. Il s'agit d'une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

Depuis la version 7.1.0, Aspose.Cells for Java peut convertir des feuilles de calcul en images SVG.

Pour utiliser cette fonctionnalité, vous devez importer l'espace de noms com.aspose.cells dans votre programme ou projet. Il contient plusieurs classes précieuses pour le rendu et l'impression, par exemple, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender), et d'autres.

La classe [**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) spécifie que la feuille de calcul sera enregistrée au format SVG.

La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) prend comme paramètre l'objet de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) qui définit le format d'enregistrement au format SVG.

Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en un fichier image SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Rendre la feuille de calcul active dans un classeur**

Un moyen simple de convertir la feuille de calcul active dans un classeur est de définir l'index de la feuille active, puis d'enregistrer le classeur au format SVG. Cela rendra la feuille active au format SVG. Le code d'exemple suivant démontre cette fonctionnalité :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Articles Connexes

- [Exportation du graphique en SVG avec l'attribut viewBox](/cells/fr/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exporter une feuille de calcul ou un graphique en image avec une largeur et une hauteur souhaitées](/cells/fr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page](/cells/fr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
