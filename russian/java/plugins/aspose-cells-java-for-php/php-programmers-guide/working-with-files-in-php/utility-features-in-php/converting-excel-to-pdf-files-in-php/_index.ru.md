---
title: Преобразование файлов Excel в PDF в PHP
type: docs
weight: 30
url: /ru/java/converting-excel-to-pdf-files-in-php/
---
## **Aspose.Cells - Преобразование файлов Excel в PDF**
Чтобы преобразовать файл Excel в файл Pdf, используя Aspose.Cells for Java в PHP, просто вызовите excel_к_pdf() модуля Converter.

**PHP-код**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Преобразование Excel в файлы PDF (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
