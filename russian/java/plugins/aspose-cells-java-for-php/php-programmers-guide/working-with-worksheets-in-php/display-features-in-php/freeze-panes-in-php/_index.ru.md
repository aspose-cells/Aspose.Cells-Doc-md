---
title: Заморозить панели в Php
type: docs
weight: 40
url: /ru/java/freeze-panes-in-php/
---
## **Aspose.Cells - Замораживание панелей**
 Чтобы заморозить области в табличном документе с помощью**Aspose.Cells Java for PHP** , просто вызовите**Замерзшие оконные стекла** модуль.

**PHP-код**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Стоп-кадр (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
