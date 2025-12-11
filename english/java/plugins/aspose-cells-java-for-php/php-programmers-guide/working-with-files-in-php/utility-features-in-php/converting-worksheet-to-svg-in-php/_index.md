---
title: Converting Worksheet to SVG in PHP
type: docs
weight: 60
url: /java/converting-worksheet-to-svg-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Converting Worksheet to SVG**
To convert a worksheet to SVG using Aspose.Cells for Java in PHP, simply invoke the `worksheet_to_svg()` method of the Converter module.

**PHP Code**

{{< highlight php >}}
$saveFormat = new SaveFormat();

$path = $dataDir . "Template.xlsx";

// Create a workbook object from the template file
$workbook = new Workbook($path);

// Convert each worksheet into SVG format in a single page.
$imgOptions = new ImageOrPrintOptions();
$imgOptions->setSaveFormat($saveFormat->SVG);
$imgOptions->setOnePagePerSheet(true);

// Convert each worksheet into SVG format
$sheetCount = $workbook->getWorksheets()->getCount();

for ($i = 0; $i < $sheetCount; $i++) {
    $sheet = $workbook->getWorksheets()->get($i);
    $sr = new SheetRender($sheet, $imgOptions);
    $pageCount = $sr->getPageCount();

    for ($k = 0; $k < $pageCount; $k++) {
        // Output the worksheet into SVG image format
        $sr->toImage($k, $path . $sheet->getName() . $k . ".out.svg");
    }
}
{{< /highlight >}}

## **Download Running Code**
Download **Converting Worksheet to SVG (Aspose.Cells)** from any of the below‑mentioned social‑coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
