---
title: Копирование и перемещение рабочих листов в Php
type: docs
weight: 10
url: /ru/java/copying-and-moving-worksheets-in-php/
---
## **Aspose.Cells - Копирование и перемещение рабочих листов**
### **Копировать рабочие листы в рабочую книгу**
 Чтобы скопировать лист с помощью**Aspose.Cells for Java в PHP** , вызов**копировать_рабочий лист** метод**копировальные листы** модуль. Ниже вы можете увидеть пример кода.

**PHP-код**

{{< highlight "php" >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Перемещение рабочих листов в рабочей книге**
 Чтобы переместить лист с помощью**Aspose.Cells for Java в PHP** , вызов**move_worksheet** метод**копировальные листы** модуль. Ниже вы можете увидеть пример кода.

**PHP-код**

{{< highlight "php" >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Копирование и перемещение рабочих листов (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
