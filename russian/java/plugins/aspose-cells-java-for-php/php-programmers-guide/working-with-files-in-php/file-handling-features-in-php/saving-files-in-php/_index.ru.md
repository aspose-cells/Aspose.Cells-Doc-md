---
title: Сохранение файлов в PHP
type: docs
weight: 20
url: /ru/java/saving-files-in-php/
---

## **Aspose.Cells - Сохранение Файлов**
### **Сохранение файла в выбранное место**
Если разработчикам нужно сохранить свои файлы, используя **Aspose.Cells Java для PHP**, в некоторое хранилище, они могут просто указать имя файла (с его полным путем хранения) и желаемый формат файла (используя перечисление **FileFormatType**) при вызове метода **save** объекта **Workbook**.

**PHP-код**

{{< highlight php >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **Скачать работающий код**
Скачать ** Сохранение файлов (Aspose.Cells) ** из любого из перечисленных ниже сайтов социального кодинга:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
