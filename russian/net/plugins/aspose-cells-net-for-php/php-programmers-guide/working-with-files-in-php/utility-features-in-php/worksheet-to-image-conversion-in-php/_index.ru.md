---
title: Преобразование рабочего листа в изображение в PHP
type: docs
weight: 40
url: /ru/net/worksheet-to-image-conversion-in-php/
---
## **Aspose.Cells - Преобразование рабочего листа в изображение**
Преобразование рабочего листа Excel Microsoft в файл изображения

**PHP-код**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/MyTestBook1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $sheet = $ptr->Get($worksheets,'Item',array(0));

        $imgOptions = $ptr->New("Aspose.Cells.Rendering.ImageOrPrintOptions",array());

        $imageFormat = new \DOTNET('mscorlib', 'System.Drawing.Imaging.ImageFormat');

        $ptr->Set($imgOptions,'ImageFormat',$imageFormat->Jpeg,array());

        $ptr->Set($imgOptions,'OnePagePerSheet',true,array());

        $sr = $ptr->New("Aspose.Cells.Rendering.SheetRender",array($sheet,$imgOptions));

        $bitmap = new \DOTNET("mscorlib", "System.Drawing.Bitmap");

        $bitmap->Save($dataDir . "./SheetImage.jpg");

        print "Conversion to Image(s) completed!" . PHP_EOL;

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Рабочий лист в изображение (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
