---
title: PHP de Çalışma Sayfasını Görüntüye Dönüştürme
type: docs
weight: 50
url: /tr/java/converting-worksheet-to-image-in-php/
---

## **Aspose.Cells - Çalışma Sayfasını Görüntüye Dönüştürme**
Aspose.Cells for Java kullanarak PHP'de Çalışma Sayfasını Görüntüye dönüştürmek için, sadece Converter modülünü çağırın.

PHP Kodu

{{< highlight php >}}

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
## **Çalışan Kodu İndir**
aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Çalışma Sayfasını Görüntüye Dönüştürme (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
