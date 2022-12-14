---
title: Скрыть или показать рабочий лист в Php
type: docs
weight: 50
url: /ru/java/hide-or-unhide-a-worksheet-in-php/
---
## **Aspose.Cells - Скрыть или показать рабочий лист**
### **Скрытие рабочего листа**
 Чтобы скрыть рабочий лист с помощью Aspose.Cells Java для PHP, вызовите**скрыть рабочий лист** модуль.

**PHP-код**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file

$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Скрыть или показать рабочий лист (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
