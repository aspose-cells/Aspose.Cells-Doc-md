---
title: PHP de Çalışma Sayfasını SVG ye Dönüştürme
type: docs
weight: 60
url: /tr/java/converting-worksheet-to-svg-in-php/
---

## **Aspose.Cells - Çalışma Sayfasını SVG'ye Dönüştürme**
Aspose.Cells for Java kullanarak PHP'de Çalışma Sayfasını SVG'ye dönüştürmek için, sadece Converter modülünün worksheet_to_svg() yöntemini çağırın.

PHP Kodu

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
## **Çalışan Kodu İndir**
aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Çalışma Sayfasını SVG'ye Dönüştürme (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
