---
title: Conversion de la feuille de calcul en image dans Aspose.Cells
type: docs
weight: 20
url: /fr/net/converting-worksheet-to-image-in-aspose-cells/
---
Ce document est conçu pour fournir aux développeurs une compréhension détaillée sur la façon de convertir une feuille de calcul en un fichier image et une feuille de calcul avec plusieurs pages en un fichier image par page.
 Parfois, vous devrez peut-être présenter des feuilles de calcul sous forme d'images, par exemple pour les utiliser dans des applications ou des pages Web. Vous devrez peut-être insérer les images dans un document Word, un**PDF** fichier, une présentation PowerPoint ou les utiliser dans un autre scénario. Simplement, vous voulez rendre la feuille de calcul sous forme d'image. Aspose.Cells prend en charge la conversion des feuilles de calcul dans les fichiers Excel Microsoft en images. Aussi,**Aspose.Cells** prend en charge la conversion d'un classeur en plusieurs fichiers image, un par page.

Vous pouvez utiliser la bureautique pour y parvenir, mais la bureautique a ses propres inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple la sécurité, la stabilité, l'évolutivité/la vitesse, le prix et les fonctionnalités. Bref, les raisons sont multiples, mais la principale est que le Microsoft lui-même déconseille fortement la bureautique.

Cet article montre comment créer une application console dans Visual Studio.Net, convertir une feuille de calcul en image et une feuille de calcul en une image pour chaque feuille de calcul avec quelques lignes de code simples à l'aide de Aspose.Cells API.Vous devez importer Aspose.Cells.Rendering namespace à votre programme/projet. Il a plusieurs classes utiles, par exemple SheetRender, ImageOrPrintOptions, WorkbookRender etc.**VersImage** méthode qui peut convertir directement une feuille de calcul en fichier(s) image spécifié(s) avec les attributs ou options souhaités. Il peut revenir**System.Drawing.Bitmap** objet et vous pouvez enregistrer un fichier image sur le disque/flux. Plusieurs formats d'image sont pris en charge, par exemple .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf, etc.

{{< highlight "csharp" >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
