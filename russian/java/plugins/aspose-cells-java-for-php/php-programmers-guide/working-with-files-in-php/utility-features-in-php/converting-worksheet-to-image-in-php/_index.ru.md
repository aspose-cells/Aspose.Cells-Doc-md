---
title: Преобразование листа в изображение в PHP
type: docs
weight: 50
url: /ru/java/converting-worksheet-to-image-in-php/
---

## **Aspose.Cells - Преобразование Листа в изображение**
Для преобразования листа в изображение с использованием Aspose.Cells for Java в PHP просто вызовите модуль Converter.

**PHP-код**

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
## **Скачать работающий код**
Загрузите **Преобразование Листа в изображение (Aspose.Cells)** с любого из указанных ниже сайтов для социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
