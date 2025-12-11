---
title: Worksheet to Image Conversion in PHP
type: docs
weight: 40
url: /net/worksheet-to-image-conversion-in-php/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Convert Worksheet to Image**
Convert a Microsoft Excel worksheet to an image file.

**PHP Code**

{{< highlight php >}}
$dataDir = '';

// Create Aspose.Cells helper object
$ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

// Opening through a path
// Creating a Workbook object and opening an Excel file using its file path
$workbook = $ptr->New("Aspose.Cells.Workbook", array($dataDir . '/MyTestBook1.xls'));

$worksheets = $ptr->Get($workbook, "Worksheets", array());

$sheet = $ptr->Get($worksheets, 'Item', array(0));

$imgOptions = $ptr->New("Aspose.Cells.Rendering.ImageOrPrintOptions", array());

$imageFormat = new \DOTNET('mscorlib', 'System.Drawing.Imaging.ImageFormat');

$ptr->Set($imgOptions, 'ImageFormat', $imageFormat->Jpeg, array());

$ptr->Set($imgOptions, 'OnePagePerSheet', true, array());

$sr = $ptr->New("Aspose.Cells.Rendering.SheetRender", array($sheet, $imgOptions));

$bitmap = new \DOTNET("mscorlib", "System.Drawing.Bitmap");

$bitmap->Save($dataDir . "./SheetImage.jpg");

print "Conversion to Image(s) completed!" . PHP_EOL;
{{< /highlight >}}

## **Download Sample Code**
Download **Worksheet to Image (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
