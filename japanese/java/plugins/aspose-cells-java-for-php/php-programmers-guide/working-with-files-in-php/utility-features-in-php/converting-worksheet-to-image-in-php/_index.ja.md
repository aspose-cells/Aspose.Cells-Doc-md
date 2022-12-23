---
title: PHP でワークシートを画像に変換する
type: docs
weight: 50
url: /ja/java/converting-worksheet-to-image-in-php/
---
## **Aspose.Cells - ワークシートを画像に変換する**
PHP で Aspose.Cells for Java を使用して Worksheet を Image に変換するには、単に Converter モジュールを呼び出します。

**PHP コード**

{{< highlight "php" >}}

 $imageFormat = new ImageFormat();

//Instantiate a new workbook with path to an Excel file

$book = new Workbook($dataDir . "MyTestBook1.xls");

//Create an object for ImageOptions

$imgOptions = new ImageOrPrintOptions();

//Set the image type

$imgOptions->setImageFormat($imageFormat->getPng());

//Get the first worksheet.

$sheet = $book->getWorksheets()->get(0);

//Create a SheetRender object for the target sheet

$sr = new SheetRender($sheet, $imgOptions);

for ($j = 0; $j < $sr->getPageCount(); $j++)

{

    //Generate an image for the worksheet

    $sr->toImage($j, $dataDir . "mysheetimg" . $j . ".png");

}

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートを画像に変換 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
