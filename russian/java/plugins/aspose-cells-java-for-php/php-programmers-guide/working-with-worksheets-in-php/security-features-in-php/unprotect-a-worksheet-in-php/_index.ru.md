---
title: Снять защиту листа в Php
type: docs
weight: 20
url: /ru/java/unprotect-a-worksheet-in-php/
---

## **Aspose.Cells - Снять защиту листа**
Для снятия защиты листа с помощью **Aspose.Cells Java для PHP** вызовите метод **unprotect_worksheet** модуля **protection**.

**PHP-код**

{{< highlight php >}}

 $filesFormatType = new FileFormatType();

//Instantiating a Workbook object

$workbook = new Workbook($dataDir . "book1.xls");

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//Unprotecting the worksheet with a password

$worksheet->unprotect("aspose");

// Save the excel file.

$workbook->save($dataDir . "output.xls", $filesFormatType->EXCEL_97_TO_2003); 

{{< /highlight >}}
## **Скачать работающий код**
Загрузите **Снятие защиты с листа (Aspose.Cells)** с любого из указанных ниже социальных сайтов для разработки:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
