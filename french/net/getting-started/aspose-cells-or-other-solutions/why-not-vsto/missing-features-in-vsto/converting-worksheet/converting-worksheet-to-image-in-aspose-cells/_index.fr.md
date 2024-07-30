---
title: Conversion de la feuille de calcul en image dans Aspose.Cells
type: docs
weight: 20
url: /fr/net/converting-worksheet-to-image-in-aspose-cells/
---

Ce document est conçu pour fournir aux développeurs une compréhension détaillée de la manière de convertir une feuille de calcul en un fichier image et une feuille de calcul avec plusieurs pages en un fichier image par page.
Parfois, vous pourriez avoir besoin de présenter des feuilles de calcul sous forme d'images, par exemple pour les utiliser dans des applications ou des pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier **PDF**, une présentation PowerPoint ou les utiliser dans un autre scénario. Simplement, vous voulez rendre la feuille de calcul comme une image. Aspose.Cells prend en charge la conversion de feuilles de calcul dans des fichiers Microsoft Excel en images. De plus, **Aspose.Cells** prend en charge la conversion d'un classeur en plusieurs fichiers image, un par page.

Vous pourriez utiliser l'automatisation Office pour y parvenir, mais l'automatisation Office a ses propres inconvénients. Il existe plusieurs raisons et problèmes impliqués : par exemple la sécurité, la stabilité, la scalabilité/la vitesse, le prix et les fonctionnalités. En bref, il existe de nombreuses raisons, mais la principale est que Microsoft elle-même déconseille fortement l'automatisation Office.

Cet article montre comment créer une application console dans Visual Studio.Net, convertir une feuille de calcul en une image, et une feuille de calcul en une image pour chaque feuille de calcul avec quelques lignes de code les plus simples en utilisant l'API Aspose.Cells. Vous devez importer l'espace de noms Aspose.Cells.Rendering dans votre programme/projet. Il possède plusieurs classes précieuses, par exemple SheetRender, ImageOrPrintOptions, WorkbookRender, etc. La classe Aspose.Cells.Rendering.SheetRender représente une feuille de calcul pour rendre des images pour la feuille de calcul, elle possède une méthode **ToImage** surchargée qui peut convertir directement une feuille de calcul en fichier image(s) spécifié(s) avec vos attributs ou options désirés. Elle peut retourner un objet **System.Drawing.Bitmap** et vous pouvez sauvegarder un fichier image sur le disque/flux. Plusieurs formats d'image sont pris en charge, par exemple .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf etc.

{{< highlight csharp >}}

//Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image type

imgOptions.ImageType = ImageType.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
