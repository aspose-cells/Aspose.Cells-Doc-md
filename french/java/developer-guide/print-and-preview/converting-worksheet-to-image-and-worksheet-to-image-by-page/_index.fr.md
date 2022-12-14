---
title: Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page
type: docs
weight: 210
url: /fr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Ce document est conçu pour fournir aux développeurs une compréhension détaillée de la façon de convertir une feuille de calcul en un fichier image et une feuille de calcul avec plusieurs pages en un fichier image par page.

Parfois, vous devrez peut-être présenter des feuilles de calcul sous forme d'images, par exemple, pour les utiliser dans des applications ou des pages Web. Vous devrez peut-être insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre scénario. Simplement, vous voulez rendre la feuille de calcul sous forme d'image. Les API Aspose.Cells prennent en charge la conversion des feuilles de calcul dans les fichiers Excel Microsoft en images. En outre, Aspose.Cells prend en charge la conversion d'un classeur en plusieurs fichiers image, un par page.

{{% /alert %}}

## **Utilisation de Aspose.Cells pour convertir une feuille de calcul en fichier image**

Cet article explique comment utiliser Aspose.Cells for Java API pour convertir une feuille de calcul en image. Le API fournit plusieurs classes précieuses, telles que[**FeuilleRendu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**ClasseurRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) , etc. La[**FeuilleRendu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) la classe représente une feuille de calcul pour restituer des images pour la feuille de calcul et a une surcharge[**àImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) qui peut convertir une feuille de calcul en fichiers image directement avec n'importe quel ensemble d'attributs ou d'options.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Résultat**

Après avoir exécuté le code ci-dessus, la feuille de calcul nommée Sheet1 est convertie en un fichier image SheetImage.jpg.

**La sortie JPG**

![tâche : image_autre_texte](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Utilisation de Aspose.Cells pour convertir une feuille de calcul en fichier image par page**

Cet exemple montre comment utiliser Aspose.Cells pour convertir une feuille de calcul à partir d'un modèle de classeur comportant plusieurs pages en un fichier image par page.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Résultat**

Après avoir exécuté le code ci-dessus, la feuille de calcul nommée Sheet1 est convertie en deux fichiers image (1 par page) Sheet 1 Page 1.Tiff et Sheet 1 Page 2.Tiff.

**Fichier image généré (Feuille 1 Page 1.Tiff)**

![tâche : image_autre_texte](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Fichier image généré (Feuille 1 Page 2.Tiff)**

![tâche : image_autre_texte](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Cet article montre comment convertir une feuille de calcul en fichier image et convertir des feuilles de calcul avec plusieurs pages en plusieurs fichiers image (un par page) à l'aide de Aspose.Cells. Aspose.Cells offre plus de flexibilité que les autres composants et offre une vitesse, une efficacité et une fiabilité exceptionnelles. Les résultats montrent que Aspose.Cells a bénéficié d'années de recherche, de conception et de réglages minutieux.

{{% /alert %}}

## Articles Liés

- [Conversion d'une feuille de calcul en différents formats d'image](/cells/fr/java/converting-worksheet-to-different-image-formats/)
- [Exporter une feuille de calcul ou un graphique dans une image avec la largeur et la hauteur souhaitées](/cells/fr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
