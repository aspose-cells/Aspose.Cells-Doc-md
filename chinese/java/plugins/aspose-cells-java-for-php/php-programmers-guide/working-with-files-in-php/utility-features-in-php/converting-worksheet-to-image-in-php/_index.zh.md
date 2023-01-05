---
title: 在 PHP 中将工作表转换为图像
type: docs
weight: 50
url: /zh/java/converting-worksheet-to-image-in-php/
---
## **Aspose.Cells - 将工作表转换为图像**
要在 PHP 中使用 Aspose.Cells for Java 将工作表转换为图像，只需调用 Converter 模块。

**PHP代码**

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
## **下载运行代码**
下载**将工作表转换为图像 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
