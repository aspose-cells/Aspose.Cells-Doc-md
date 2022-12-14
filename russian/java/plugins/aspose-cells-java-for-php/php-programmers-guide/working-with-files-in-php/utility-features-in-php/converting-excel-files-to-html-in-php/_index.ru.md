---
title: Преобразование файлов Excel в HTML в PHP
type: docs
weight: 20
url: /ru/java/converting-excel-files-to-html-in-php/
---
## **Aspose.Cells - Преобразование файлов Excel в HTML**
Чтобы преобразовать Excel в HTML, используя Aspose.Cells for Java в PHP, просто вызовите рабочий лист_к_html() модуля Converter.

**PHP-код**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Преобразование файлов Excel в HTML (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
