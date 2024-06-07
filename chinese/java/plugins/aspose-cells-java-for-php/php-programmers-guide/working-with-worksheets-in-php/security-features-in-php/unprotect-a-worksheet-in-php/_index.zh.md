---
title: 在Php中取消保护工作表
type: docs
weight: 20
url: /zh/java/unprotect-a-worksheet-in-php/
---

## **Aspose.Cells - 取消保护工作表**
使用**Aspose.Cells Java for PHP**，通过调用**protection**模块的**unprotect_worksheet**方法来取消保护工作表。

**PHP代码**

{{< highlight php >}}

 $filesFormatType = new FileFormatType();

//Instantiating a Workbook object

$workbook = new Workbook($dataDir . "book1.xls");

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//Unprotecting the worksheet with a password

$worksheet->unprotect("aspose");

// Save the excel file.

$workbook->save($dataDir . "output.xls", $filesFormatType->EXCEL_97_TO_2003); 

{{< /highlight >}}
## **下载运行代码**
从以下任一社交编码站点下载 **Unprotect a Worksheet (Aspose.Cells)**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
