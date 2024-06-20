---
title: Преобразование в файлы MHTML в PHP
type: docs
weight: 40
url: /ru/java/converting-to-mhtml-files-in-php/
---

## **Aspose.Cells - Преобразование в файлы MHTML**
Для преобразования листа в файл MHTML с использованием Aspose.Cells for Java в PHP просто вызовите метод worksheet_to_mhtml() модуля Converter.

**PHP-код**

{{< highlight php >}}

 $sveFormat = new SaveFormat();

//Specify the file path

$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options

$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file

$wb = new Workbook($filePath);

//Save the MHT file

$wb->save($filePath . ".out.mht", $sv);

{{< /highlight >}}
## **Скачать работающий код**
Загрузите **Преобразование в файлы MHTML (Aspose.Cells)** с любого из указанных ниже сайтов для социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
