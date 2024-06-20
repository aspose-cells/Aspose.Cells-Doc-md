---
title: Копирование и перемещение листов в Php
type: docs
weight: 10
url: /ru/java/copying-and-moving-worksheets-in-php/
---

## **Aspose.Cells - Копирование и перемещение листов**
### **Копировать листы в рамках рабочей книги**
Чтобы скопировать лист с использованием **Aspose.Cells for Java в PHP**, вызовите метод **copy_worksheet** модуля **copyworksheets**. Ниже приведен пример кода.

**PHP-код**

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Перемещение листов в рамках книги**
Чтобы переместить лист с использованием **Aspose.Cells for Java в PHP**, вызовите метод **move_worksheet** модуля **copyworksheets**. Ниже приведен пример кода.

**PHP-код**

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Скачать работающий код**
Загрузите **Копирование и перемещение листов (Aspose.Cells)** с любого из указанных ниже социальных сайтов для разработки:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
