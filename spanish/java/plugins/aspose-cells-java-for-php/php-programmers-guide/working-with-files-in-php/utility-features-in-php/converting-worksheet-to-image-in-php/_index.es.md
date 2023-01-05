---
title: Convertir hoja de trabajo a imagen en PHP
type: docs
weight: 50
url: /es/java/converting-worksheet-to-image-in-php/
---
## **Aspose.Cells - Conversión de hoja de trabajo en imagen**
Para convertir una hoja de trabajo en una imagen usando Aspose.Cells for Java en PHP, simplemente invoque el módulo Converter.

**Código PHP**

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
## **Descargar código de ejecución**
Descargar**Conversión de hoja de trabajo en imagen (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
