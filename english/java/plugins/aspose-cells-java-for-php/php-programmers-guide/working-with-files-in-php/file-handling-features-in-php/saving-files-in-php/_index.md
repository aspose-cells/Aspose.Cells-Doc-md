---
title: Saving Files in PHP
type: docs
weight: 20
url: /java/saving-files-in-php/
---

## **Aspose.Cells - Saving Files**
### **Saving file to some location**
If developers need to save their files using **Aspose.Cells Java for PHP** to some storage location then they can simply specify the file name (with its complete storage path) and desired file format (using the **FileFormatType** enumeration) while calling the **save** method of **Workbook** object.

**PHP Code**

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
## **Download Running Code**
Download **Saving Files (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
