﻿---
title: تحويل ورقة العمل إلى صورة في PHP
type: docs
weight: 50
url: /ar/java/converting-worksheet-to-image-in-php/
---
## **Aspose.Cells - تحويل ورقة العمل إلى صورة**
لتحويل ورقة العمل إلى صورة باستخدام Aspose.Cells for Java في PHP ، ما عليك سوى استدعاء وحدة المحول.

**كود PHP**

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
## **قم بتنزيل كود التشغيل**
تحميل**تحويل ورقة العمل إلى صورة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)