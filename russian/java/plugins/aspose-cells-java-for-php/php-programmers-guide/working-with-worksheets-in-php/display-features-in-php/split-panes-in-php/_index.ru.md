---
title: Разбить панели в Php
type: docs
weight: 70
url: /ru/java/split-panes-in-php/
---

## **Aspose.Cells - Разделить панели**
Для разделения панелей с помощью **Aspose.Cells Java для PHP** просто вызовите модуль **SplitPanes**.

**PHP-код**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

//Instantiate a new workbook

//Open a template file

$book = new Workbook($dataDir . "book.xls");

//Set the active cell

$book->getWorksheets()->get(0)->setActiveCell("A20");

//Split the worksheet window

$book->getWorksheets()->get(0)->split();

//Save the excel file

$book->save($dataDir . "book.out.xls", $saveFormat->EXCEL_97_TO_2003);

{{< /highlight >}}
## **Скачать работающий код**
Скачайте **Разделить панели (Aspose.Cells)** с любого из нижеуказанных сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
