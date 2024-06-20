---
title: Conversion de feuille de calcul en image en PHP
type: docs
weight: 50
url: /fr/java/converting-worksheet-to-image-in-php/
---

## **Aspose.Cells - Conversion de feuille de calcul en image**
Pour convertir une feuille de calcul en image à l'aide du Aspose.Cells for Java en PHP, il suffit d'appeler le module Converter.

**Code PHP**

{{< highlight php >}}

 $imageFormat = new ImageFormat();

//Instantiate a new workbook with path to an Excel file

$book = new Workbook($dataDir . "MyTestBook1.xls");

//Create an object for ImageOptions

$imgOptions = new ImageOrPrintOptions();

//Set the image type

$imgOptions->setImageFormat($imageFormat->getPng());

//Get the first worksheet.

$sheet = $book->getWorksheets()->get(0);

//Create a SheetRender object for the target sheet

$sr = new SheetRender($sheet, $imgOptions);

for ($j = 0; $j < $sr->getPageCount(); $j++)

{

    //Generate an image for the worksheet

    $sr->toImage($j, $dataDir . "mysheetimg" . $j . ".png");

}

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Converting Worksheet to Image (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
