---
title: Arbeitsblatt in SVG in PHP konvertieren
type: docs
weight: 60
url: /de/java/converting-worksheet-to-svg-in-php/
---

## **Aspose.Cells - Konvertierung von Arbeitsblatt in SVG**
Um ein Arbeitsblatt unter Verwendung von Aspose.Cells for Java in PHP in SVG zu konvertieren, rufen Sie einfach die Methode worksheet_to_svg() des Converter-Moduls auf.

**PHP-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Konvertierung von Arbeitsblatt in SVG (Aspose.Cells)** von einer der unten aufgeführten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
