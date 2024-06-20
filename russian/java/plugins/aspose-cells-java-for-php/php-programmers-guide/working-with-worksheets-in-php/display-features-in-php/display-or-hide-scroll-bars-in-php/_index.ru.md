---
title: Показать или скрыть полосы прокрутки в Php
type: docs
weight: 20
url: /ru/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - Показать или скрыть полосы прокрутки**
### **Скрытие полос прокрутки**
Чтобы скрыть полосы прокрутки с помощью **Aspose.Cells Java для PHP**, вызовите модуль **displayhidescrollbars**.

**PHP-код**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Показать или скрыть полосы прокрутки (Aspose.Cells)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
