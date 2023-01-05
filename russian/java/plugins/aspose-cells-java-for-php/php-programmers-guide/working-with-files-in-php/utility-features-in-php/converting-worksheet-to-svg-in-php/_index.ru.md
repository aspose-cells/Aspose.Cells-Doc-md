---
title: Преобразование рабочего листа в SVG в PHP
type: docs
weight: 60
url: /ru/java/converting-worksheet-to-svg-in-php/
---
## **Aspose.Cells - Преобразование рабочего листа в SVG**
Чтобы преобразовать рабочий лист в SVG, используя Aspose.Cells for Java в PHP, просто вызовите рабочий лист_к_Метод svg() модуля Converter.

**PHP-код**

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
## **Скачать рабочий код**
Скачать**Преобразование рабочего листа в SVG (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
