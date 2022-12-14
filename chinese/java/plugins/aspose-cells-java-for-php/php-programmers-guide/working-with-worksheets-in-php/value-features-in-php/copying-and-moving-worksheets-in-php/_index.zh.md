---
title: 在 Php 中复制和移动工作表
type: docs
weight: 10
url: /zh/java/copying-and-moving-worksheets-in-php/
---
## **Aspose.Cells - 复制和移动工作表**
### **在工作簿中复制工作表**
使用复制工作表**PHP 中的 Aspose.Cells for Java**， 称呼**复制工作表**的方法**抄作业**模块。您可以在下面看到代码示例。

**PHP代码**

{{< highlight "php" >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **在工作簿中移动工作表**
使用移动工作表**PHP 中的 Aspose.Cells for Java**， 称呼**移动工作表**的方法**抄作业**模块。您可以在下面看到代码示例。

**PHP代码**

{{< highlight "php" >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **下载运行代码**
下载**复制和移动工作表 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
