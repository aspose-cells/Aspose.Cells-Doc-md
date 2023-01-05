---
title: Преобразование в файлы MHTML в PHP
type: docs
weight: 40
url: /ru/java/converting-to-mhtml-files-in-php/
---
## **Aspose.Cells - Преобразование в файлы MHTML**
Чтобы преобразовать рабочий лист в файл MHTML, используя Aspose.Cells for Java в PHP, просто вызовите рабочий лист_к_Метод mhtml() модуля Converter.

**PHP-код**

{{< highlight "php" >}}

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
## **Скачать рабочий код**
Скачать**Преобразование в файлы MHTML (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
