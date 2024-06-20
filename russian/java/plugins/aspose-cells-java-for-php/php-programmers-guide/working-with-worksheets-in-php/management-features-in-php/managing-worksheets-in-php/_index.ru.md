---
title: Управление листами данных в Php
type: docs
weight: 10
url: /ru/java/managing-worksheets-in-php/
---

## **Aspose.Cells - Управление рабочими листами**
### **Добавление рабочих листов в новый файл Excel**
Чтобы добавить лист данных в новый файл Excel с помощью **Aspose.Cells Java для PHP**, просто вызовите метод **add_worksheet** модуля **MangingWorksheets**.

**PHP-код**

{{< highlight php >}}

 //Instantiating a Workbook object

$workbook = new Workbook();

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$sheetIndex = $worksheets->add();

$worksheet = $worksheets->get($sheetIndex);

//Setting the name of the newly added worksheet

$worksheet->setName("My Worksheet");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
### **Удаление листов с использованием имени листа**
Чтобы удалить лист данных по названию листа с помощью **Aspose.Cells Java для PHP**, просто вызовите метод **remove_worksheet_by_name** модуля **MangingWorksheets**.

**PHP-код**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet name

$workbook->getWorksheets()->removeAt("Sheet1");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
### **Удаление рабочих листов с использованием индекса листа.**
Чтобы удалить лист данных по индексу листа с помощью **Aspose.Cells Java для PHP**, просто вызовите метод **remove_worksheet_by_index** модуля **MangingWorksheets**.

**PHP-код**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream=new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet index

$workbook->getWorksheets()->removeAt(0);

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
## **Скачать работающий код**
Загрузите управление рабочими листами (Aspose.Cells) с любого из упомянутых ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
