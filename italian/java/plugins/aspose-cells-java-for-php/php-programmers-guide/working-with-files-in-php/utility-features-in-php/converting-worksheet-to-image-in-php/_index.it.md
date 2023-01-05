---
title: Conversione del foglio di lavoro in immagine in PHP
type: docs
weight: 50
url: /it/java/converting-worksheet-to-image-in-php/
---
## **Aspose.Cells - Conversione del foglio di lavoro in immagine**
Per convertire il foglio di lavoro in immagine utilizzando Aspose.Cells for Java in PHP, è sufficiente richiamare il modulo Converter.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scaricamento**Conversione del foglio di lavoro in immagine (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
