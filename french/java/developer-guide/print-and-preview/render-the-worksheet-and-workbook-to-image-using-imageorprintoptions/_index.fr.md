---
title: Rendre la feuille de calcul et le classeur en image à l'aide d'ImageOrPrintOptions
type: docs
weight: 220
url: /fr/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

Ce document est conçu pour fournir une compréhension détaillée de la façon de convertir une feuille de calcul ou un classeur en fichier image et d'appliquer différentes options d'image et d'impression pour l'image, des options telles que la résolution, la compression TIFF, le format d'image et la qualité de la page.

{{% /alert %}}

## **Aperçu**

Parfois, vous devrez peut-être présenter vos feuilles de calcul sous forme de représentation graphique. Vous devez présenter les images de la feuille de calcul dans vos applications ou vos pages Web. Vous devrez peut-être insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre scénario. Vous voulez simplement qu'une feuille de calcul soit rendue sous forme d'image afin que vous puissiez l'utiliser ailleurs. Aspose.Cells prend en charge la conversion de feuilles de calcul dans des fichiers Excel en images. En outre, Aspose.Cells prend en charge la définition de différentes options telles que le format d'image, la résolution (verticale et horizontale), la qualité d'image et d'autres options d'image et d'impression.

Le API fournit plusieurs classes précieuses, par exemple,[**FeuilleRendu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**ClasseurRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), etc.

 La[**FeuilleRendu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) classe gère la tâche de rendu des images pour la feuille de calcul alors que la[**ClasseurRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)fait de même pour un classeur. Les deux classes susmentionnées ont plusieurs versions surchargées de la*àImage*méthode qui peut convertir directement une feuille de calcul ou un classeur en fichier(s) image spécifié(s) avec les attributs ou options souhaités. Vous pouvez enregistrer le fichier image sur le disque/flux. Plusieurs formats d'image sont pris en charge, par exemple BMP, PNG, GIFF, JPEG, TIFF, EMF, etc.

### **Convertir une feuille de calcul en image**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Options de conversion**

Il est possible d'enregistrer des pages spécifiques à l'image. Le code suivant convertit les première et deuxième feuilles de calcul d'un classeur en images JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Ou vous pouvez parcourir le classeur et afficher chaque feuille de calcul dans une image distincte :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Convertir le classeur en image :**

 Afin de rendre le classeur complet au format image, vous pouvez soit utiliser l'approche ci-dessus, soit simplement utiliser le[**ClasseurRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) classe qui accepte une instance de[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) ainsi que l'objet de[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

{{% alert color="primary" %}}

 La[**ClasseurRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) peut uniquement enregistrer le classeur au format TIFF.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## Articles Liés

- [Conversion d'une feuille de calcul en différents formats d'image](/cells/fr/java/converting-worksheet-to-different-image-formats/)
- [Exporter le graphique vers SVG avec l'attribut viewBox](/cells/fr/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exporter une feuille de calcul ou un graphique dans une image avec la largeur et la hauteur souhaitées](/cells/fr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page](/cells/fr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
