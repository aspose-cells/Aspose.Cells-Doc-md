---
title: Преобразование листа в SVG в PHP
type: docs
weight: 60
url: /ru/java/converting-worksheet-to-svg-in-php/
---

## **Aspose.Cells - Преобразование Листа в SVG**
Для преобразования листа в SVG с использованием Aspose.Cells for Java в PHP просто вызовите метод worksheet_to_svg() модуля Converter.

**PHP-код**

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
## **Скачать работающий код**
Загрузите **Преобразование Листа в SVG (Aspose.Cells)** с любого из указанных ниже сайтов для социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
