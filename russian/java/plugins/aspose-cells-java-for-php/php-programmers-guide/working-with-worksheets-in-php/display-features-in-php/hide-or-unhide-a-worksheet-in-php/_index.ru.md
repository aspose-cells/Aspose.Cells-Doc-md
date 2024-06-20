---
title: Скрыть или отобразить лист в Php
type: docs
weight: 50
url: /ru/java/hide-or-unhide-a-worksheet-in-php/
---

## **Aspose.Cells - Скрыть или показать лист**
### **Скрыть лист**
Для скрытия листа с использованием Aspose.Cells Java для PHP вызовите модуль **hideunhideworksheet**.

**PHP-код**

{{< highlight php >}}

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
## **Скачать работающий код**
Скачайте **Показать или скрыть лист (Aspose.Cells)** с любого из нижеуказанных сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
