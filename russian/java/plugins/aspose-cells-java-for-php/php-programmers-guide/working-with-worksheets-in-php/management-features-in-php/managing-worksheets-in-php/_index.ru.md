---
title: Управление рабочими листами в Php
type: docs
weight: 10
url: /ru/java/managing-worksheets-in-php/
---
## **Aspose.Cells - Управление рабочими листами**
### **Добавление рабочих листов в новый файл Excel**
Чтобы добавить рабочий лист в новый файл Excel, используя**Aspose.Cells Java для PHP** , просто позвоните**add_worksheet** метод**Управление рабочими листами** модуль.

**PHP-код**

{{< highlight "php" >}}

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
### **Удаление рабочих листов с использованием имени листа**
 Чтобы удалить рабочий лист по имени листа, используя**Aspose.Cells Java для PHP** , просто позвоните**remove_worksheet_by_name** метод**Управление рабочими листами** модуль.

**PHP-код**

{{< highlight "php" >}}

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
### **Удаление рабочих листов с помощью индекса листов**
 Чтобы удалить рабочий лист по индексу листа, используя**Aspose.Cells Java для PHP** , просто позвоните**remove_worksheet_by_index** метод**Управление рабочими листами** модуль.

**PHP-код**

{{< highlight "php" >}}

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
## **Скачать рабочий код**
Скачать**Управление рабочими листами (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
