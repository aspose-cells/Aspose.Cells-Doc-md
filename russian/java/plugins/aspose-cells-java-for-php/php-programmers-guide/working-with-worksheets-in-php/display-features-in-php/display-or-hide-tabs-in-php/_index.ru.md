---
title: Показать или скрыть вкладки в Php
type: docs
weight: 30
url: /ru/java/display-or-hide-tabs-in-php/
---

## **Aspose.Cells - Отображение или скрытие вкладок**
### **Скрытие вкладок**
Чтобы скрыть вкладки с помощью **Aspose.Cells Java для PHP**, вызовите модуль **displayhidetabs**.

**PHP-код**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Скрыть или отобразить вкладки (Aspose.Cells)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
