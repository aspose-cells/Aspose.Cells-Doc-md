---
title: تحويل ورقة العمل إلى SVG في PHP
type: docs
weight: 60
url: /ar/java/converting-worksheet-to-svg-in-php/
---

## **Aspose.Cells - تحويل ورقة العمل إلى SVG**
لتحويل ورقة العمل إلى SVG باستخدام رمز Aspose.Cells for Java في PHP، قم ببساطة باستدعاء طريقة worksheet_to_svg() من وحدة Converter.

**كود PHP**

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
## **تحميل رمز التشغيل**
تنزيل ** تحويل ورقة العمل إلى SVG (Aspose.Cells) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
