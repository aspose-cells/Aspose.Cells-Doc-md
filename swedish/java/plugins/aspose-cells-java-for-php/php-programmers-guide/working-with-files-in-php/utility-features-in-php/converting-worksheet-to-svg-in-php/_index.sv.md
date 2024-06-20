---
title: Konvertera arbetsblad till SVG i PHP
type: docs
weight: 60
url: /sv/java/converting-worksheet-to-svg-in-php/
---

## **Aspose.Cells - Konvertering av kalkylblad till SVG**
För att konvertera arbetsblad till SVG med Aspose.Cells for Java i PHP, helt enkelt anropa worksheet_to_svg() metoden i konverteringsmodulen.

**PHP-kod**

{{< highlight php >}}

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

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ned **Konvertera kalkylblad till SVG (Aspose.Cells)** från någon av nedanstående sociala kodningssajter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
