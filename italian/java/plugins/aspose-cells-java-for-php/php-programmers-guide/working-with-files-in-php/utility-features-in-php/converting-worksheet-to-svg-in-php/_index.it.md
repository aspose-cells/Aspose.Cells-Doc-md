---
title: Conversione del foglio di lavoro in SVG in PHP
type: docs
weight: 60
url: /it/java/converting-worksheet-to-svg-in-php/
---

## **Aspose.Cells - Conversione di un foglio di lavoro in SVG**
Per convertire il foglio di lavoro in SVG usando Aspose.Cells for Java in PHP, basta invocare il metodo worksheet_to_svg() del modulo Converter.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Conversione di un foglio di lavoro in SVG (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale sotto elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
