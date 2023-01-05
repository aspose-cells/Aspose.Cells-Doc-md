---
title: Показать или скрыть линии сетки в Php
type: docs
weight: 10
url: /ru/java/display-or-hide-gridlines-in-php/
---
## **Aspose.Cells — Показать или скрыть линии сетки**
### **Скрытие линий сетки**
 Чтобы скрыть рабочий лист, используя**Aspose.Cells Java for PHP** , вызов**displayhidegridlines** модуль.

**PHP-код**

{{< highlight "php" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

//Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the grid lines of the first worksheet of the Excel file

$worksheet->setGridlinesVisible(false);

//Saving the modified Excel file in default (that is Excel 2000) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Показать или скрыть линии сетки (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
