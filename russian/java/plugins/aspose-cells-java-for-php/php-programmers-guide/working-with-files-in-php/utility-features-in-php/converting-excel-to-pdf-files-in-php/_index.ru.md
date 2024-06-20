---
title: Преобразование Excel в PDF файлы в PHP
type: docs
weight: 30
url: /ru/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - Преобразование Excel в PDF-файлы**
Для преобразования Excel в PDF-файл с использованием Aspose.Cells for Java в PHP, просто вызовите метод excel_to_pdf() модуля Converter.

**PHP-код**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Преобразование Excel в PDF-файлы (Aspose.Cells)** с любого из перечисленных ниже социальных сайтов для программистов:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
