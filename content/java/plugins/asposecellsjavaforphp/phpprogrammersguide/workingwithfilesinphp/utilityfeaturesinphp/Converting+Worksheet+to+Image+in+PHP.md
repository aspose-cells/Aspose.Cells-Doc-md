+++
title = "Converting Worksheet to Image in PHP" 
description = "" 
weight = 24837 
+++

Aspose.Cells for Java : Converting Worksheet to Image in PHP  

# Aspose.Cells for Java : Converting Worksheet to Image in PHP


## Aspose.Cells - Converting Worksheet to Image

To convert Worksheet to Image using Aspose.Cells for Java in PHP, simply invoke Converter module.

**PHP Code**

{{< code lang="cs" >}}
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
{{< /code >}}

## Download Running Code

Download **Converting Worksheet to Image (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)

