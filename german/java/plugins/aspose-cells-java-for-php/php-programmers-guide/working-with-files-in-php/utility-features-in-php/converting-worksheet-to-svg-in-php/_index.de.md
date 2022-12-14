---
title: Konvertieren von Arbeitsblättern in SVG in PHP
type: docs
weight: 60
url: /de/java/converting-worksheet-to-svg-in-php/
---
## **Aspose.Cells – Arbeitsblatt in SVG konvertieren**
Um Worksheet mit Aspose.Cells for Java in PHP in SVG zu konvertieren, rufen Sie einfach worksheet auf_zu_svg()-Methode des Converter-Moduls.

**PHP-Code**

{{< highlight "php" >}}

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
## **Laufcode herunterladen**
Download**Arbeitsblatt in SVG konvertieren (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
