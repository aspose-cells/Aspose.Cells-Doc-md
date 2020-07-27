+++
title = "Converting Worksheet to SVG in PHP" 
description = "" 
weight = 24838 
+++

Aspose.Cells for Java : Converting Worksheet to SVG in PHP  

# Aspose.Cells for Java : Converting Worksheet to SVG in PHP


## Aspose.Cells - Converting Worksheet to SVG

To convert Worksheet to SVG using Aspose.Cells for Java in PHP, simply invoke worksheet\_to\_svg() method of Converter module.

**PHP Code**

{{< code lang="cs" >}}
$saveFormat = new SaveFormat();

$path = $dataDir . "Template.xlsx";

//Create a workbook object from the template file
$workbook = new Workbook($path);

//Convert each worksheet into svg format in a single page.
$imgOptions = new ImageOrPrintOptions();
$imgOptions->setSaveFormat($saveFormat->SVG);
$imgOptions->setOnePagePerSheet(true);

//Convert each worksheet into svg format
$sheetCount = $workbook->getWorksheets()->getCount();

for($i=0; $i < $sheetCount; $i++)
{
    $sheet = $workbook->getWorksheets()->get($i);

    $sr = new SheetRender($sheet, $imgOptions);

    $pageCount = $sr->getPageCount();
    for ($k = 0; $k < $pageCount; $k++)
    {
        //Output the worksheet into Svg image format
        $sr->toImage($k, $path . $sheet->getName() . $k . ".out.svg");
    }
}
{{< /code >}}

## Download Running Code

Download **Converting Worksheet to SVG (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)

