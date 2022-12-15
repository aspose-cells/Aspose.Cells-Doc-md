---
title: Показать или скрыть вкладки в Php
type: docs
weight: 30
url: /ru/java/display-or-hide-tabs-in-php/
---
## **Aspose.Cells — Показать или скрыть вкладки**
### **Скрытие вкладок**
 Чтобы скрыть вкладки с помощью**Aspose.Cells Java for PHP** , вызов**показать скрыть вкладки** модуль.

**PHP-код**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Скрыть или отобразить или скрыть вкладки (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
