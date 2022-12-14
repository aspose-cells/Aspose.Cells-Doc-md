---
title: Arbeitsblatt in Bild in PHP konvertieren
type: docs
weight: 50
url: /de/java/converting-worksheet-to-image-in-php/
---
## **Aspose.Cells – Arbeitsblatt in Bild konvertieren**
Um ein Arbeitsblatt mit Aspose.Cells for Java in PHP in ein Bild zu konvertieren, rufen Sie einfach das Konvertermodul auf.

**PHP-Code**

{{< highlight "php" >}}

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
## **Laufcode herunterladen**
Download**Arbeitsblatt in Bild konvertieren (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
