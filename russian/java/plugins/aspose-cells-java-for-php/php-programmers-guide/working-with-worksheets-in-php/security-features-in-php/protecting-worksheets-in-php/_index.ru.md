---
title: Защита рабочих листов в Php
type: docs
weight: 10
url: /ru/java/protecting-worksheets-in-php/
---
## **Aspose.Cells - Защита рабочих листов**
 Чтобы защитить рабочий лист с помощью**Aspose.Cells Java for PHP** , вызов**Protect_worksheet** метод**защита** модуль.

**PHP-код**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$excel = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $excel->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//The following 3 methods are only for Excel 2000 and earlier formats

$protection->setAllowEditingContent(false);

$protection->setAllowEditingObject(false);

$protection->setAllowEditingScenario(false);

//Protects the first worksheet with a password "1234"

$protection->setPassword("1234");

//Saving the modified Excel file in default format

$excel->save($dataDir . "output.xls");  

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Защита рабочих листов (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/ProtectingWorksheet.php)
