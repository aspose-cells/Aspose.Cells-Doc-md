---
title: Снять защиту листа в Php
type: docs
weight: 20
url: /ru/java/unprotect-a-worksheet-in-php/
---
## **Aspose.Cells - Снять защиту с рабочего листа**
 Чтобы защитить рабочий лист с помощью**Aspose.Cells Java для PHP** , вызов**unprotect_worksheet** метод**защита** модуль.

**PHP-код**

{{< highlight "php" >}}

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
## **Скачать рабочий код**
Скачать**Снять защиту с рабочего листа (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
