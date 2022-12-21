---
title: PHP でワークシートを SVG に変換する
type: docs
weight: 60
url: /ja/java/converting-worksheet-to-svg-in-php/
---
## **Aspose.Cells - ワークシートを SVG に変換する**
PHP で Aspose.Cells for Java を使用してワークシートを SVG に変換するには、ワークシートを呼び出すだけです。_に_Converter モジュールの svg() メソッド。

**PHPコード**

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
## **実行中のコードをダウンロード**
ダウンロード**ワークシートを SVG に変換する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingWorksheetToSVG.php)
