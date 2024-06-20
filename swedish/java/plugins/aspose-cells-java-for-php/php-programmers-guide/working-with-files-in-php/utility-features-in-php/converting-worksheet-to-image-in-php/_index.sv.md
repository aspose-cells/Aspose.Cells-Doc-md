---
title: Konvertera arbetsblad till bild i PHP
type: docs
weight: 50
url: /sv/java/converting-worksheet-to-image-in-php/
---

## **Aspose.Cells - Konvertering av kalkylblad till bild**
För att konvertera arbetsblad till bild med Aspose.Cells for Java i PHP, helt enkelt anropa konverteringsmodulen.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ned **Konvertera kalkylblad till bild (Aspose.Cells)** från någon av nedanstående sociala kodningssajter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
