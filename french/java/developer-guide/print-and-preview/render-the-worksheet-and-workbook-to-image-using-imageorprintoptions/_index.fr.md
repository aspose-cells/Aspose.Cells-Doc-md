---
title: Rendre la feuille de calcul et le classeur en image en utilisant ImageOrPrintOptions
type: docs
weight: 220
url: /fr/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

Ce document est conçu pour fournir une compréhension détaillée de la conversion d'une feuille de calcul ou d'un classeur en un fichier image et d'appliquer différentes options d'image et d'impression pour l'image, telles que la résolution, la compression TIFF, le format d'image et la qualité de page.

{{% /alert %}}

## **Vue d'ensemble**

Parfois, vous pourriez avoir besoin de présenter vos feuilles de calcul sous forme de représentation imagée. Vous devez présenter les images de feuilles de calcul dans vos applications ou pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre contexte. Tout simplement, vous souhaitez une feuille de calcul rendue sous forme d'image afin de pouvoir l'utiliser ailleurs. Aspose.Cells prend en charge la conversion des feuilles de calcul dans des fichiers Excel en images. De plus, Aspose.Cells prend en charge la définition de différentes options telles que le format d'image, la résolution (verticale et horizontale), la qualité d'image et d'autres options d'image et d'impression.

L'API fournit plusieurs classes utiles, par exemple, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), etc.

La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) gère la tâche de rendre des images pour la feuille de calcul tandis que la classe [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) fait de même pour un classeur. Lesdites classes ont plusieurs versions surchargées de la méthode *toImage* qui peuvent directement convertir une feuille de calcul ou un classeur en fichier(s) image spécifié(s) avec vos attributs ou options désirés. Vous pouvez enregistrer le fichier image sur le disque/le flux. Plusieurs formats d'image sont pris en charge, tels que BMP, PNG, GIFF, JPEG, TIFF, EMF, etc.

### **Convertir une feuille de calcul en image**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Options de conversion**

Il est possible d'enregistrer des pages spécifiques en tant qu'images. Le code suivant convertit les première et deuxième feuilles de calcul dans un classeur en images JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Ou vous pouvez parcourir le classeur et rendre chaque feuille de calcul en une image distincte :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Convertir un classeur en image :**

Pour rendre le classeur complet au format image, vous pouvez soit utiliser l'approche ci-dessus, soit simplement utiliser la classe [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) qui accepte une instance de [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) ainsi que l'objet de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Vous pouvez enregistrer le classeur entier dans une seule image TIFF avec plusieurs cadres ou pages :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## Articles Connexes

- [Conversion de la feuille de calcul dans différents formats d'image](/cells/fr/java/converting-worksheet-to-different-image-formats/)
- [Exportation du graphique en SVG avec l'attribut viewBox](/cells/fr/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exporter une feuille de calcul ou un graphique en image avec une largeur et une hauteur souhaitées](/cells/fr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page](/cells/fr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
