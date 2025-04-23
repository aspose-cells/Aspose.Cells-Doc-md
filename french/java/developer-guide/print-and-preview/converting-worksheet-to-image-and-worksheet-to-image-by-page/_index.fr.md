---
title: Conversion de la feuille de calcul en image et de la feuille de calcul en image par page
type: docs
weight: 210
url: /fr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Ce document est conçu pour fournir aux développeurs une compréhension détaillée de la manière de convertir une feuille de calcul en un fichier image et une feuille de calcul avec plusieurs pages en un fichier image par page.

Parfois, vous pourriez avoir besoin de présenter des feuilles de calcul sous forme d'images, par exemple, pour les utiliser dans des applications ou des pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint, ou les utiliser dans un autre scénario. En somme, vous voulez rendre la feuille de calcul sous forme d'image. Les API Aspose.Cells prennent en charge la conversion des feuilles de calcul dans les fichiers Microsoft Excel en images. De plus, Aspose.Cells prend en charge la conversion d'un classeur en plusieurs fichiers image, un par page.

{{% /alert %}}

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en un fichier image**

Cet article montre comment utiliser Aspose.Cells for Java API pour convertir une feuille de calcul en image. L'API fournit plusieurs classes utiles, telles que [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), et ainsi de suite. La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) représente une feuille de calcul pour rendre des images pour la feuille de calcul et dispose d'une méthode [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-) surchargée qui peut convertir une feuille de calcul en images directement avec des attributs ou des options définis.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Résultat**

Après l'exécution du code ci-dessus, la feuille de calcul nommée Feuil1 est convertie en un fichier image FeuilleImage.jpg.

**Le fichier JPG de sortie**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en fichier image par page**

Cet exemple montre comment utiliser Aspose.Cells pour convertir une feuille de calcul d'un classeur modèle comportant plusieurs pages en un fichier image unique par page.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Résultat**

Après l'exécution du code ci-dessus, la feuille de calcul nommée Feuil1 est convertie en deux fichiers image (1 par page) Feuil1 Page 1.Tiff et Feuil1 Page 2.Tiff.

**Fichier image généré (Feuil1 Page 1.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Fichier image généré (Feuil1 Page 2.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Cet article montre comment convertir une feuille de calcul en un fichier image et convertir des feuilles de calcul avec plusieurs pages en plusieurs fichiers image (un par page) en utilisant Aspose.Cells. Aspose.Cells offre plus de flexibilité que d'autres composants et garantit une vitesse, une efficacité et une fiabilité exceptionnelles. Les résultats montrent qu'Aspose.Cells a bénéficié de nombreuses années de recherche, de conception et d'ajustements minutieux.

{{% /alert %}}

## Articles Connexes

- [Conversion de la feuille de calcul dans différents formats d'image](/cells/fr/java/converting-worksheet-to-different-image-formats/)
- [Exporter une feuille de calcul ou un graphique en image avec une largeur et une hauteur souhaitées](/cells/fr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
