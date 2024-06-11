---
title: 在PHP中保存文件
type: docs
weight: 20
url: /zh/java/saving-files-in-php/
---

## **Aspose.Cells - 保存文件**
### **将文件保存到某个位置**
如果开发人员需要使用 **Aspose.Cells Java for PHP** 将文件保存到某个存储位置，他们可以在调用 **Workbook** 对象的 **save** 方法时简单地指定文件名（包括完整的存储路径）和所需的文件格式（使用**FileFormatType**枚举）。 

**PHP 代码**

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
## **下载运行代码**
从以下任一社交编码网站下载**保存文件（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
