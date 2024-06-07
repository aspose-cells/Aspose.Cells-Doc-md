---
title: 在Php中复制和移动工作表
type: docs
weight: 10
url: /zh/java/copying-and-moving-worksheets-in-php/
---

## **Aspose.Cells - 复制和移动工作表**
### **在工作簿内复制工作表**
使用**Aspose.Cells for Java in PHP**，通过调用**copyworksheets**模块的**copy_worksheet**方法来复制工作表。下面是代码示例。

**PHP代码**

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **在工作簿内移动工作表**
使用**Aspose.Cells for Java in PHP**，通过调用**copyworksheets**模块的**move_worksheet**方法来移动工作表。下面是代码示例。

**PHP代码**

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **下载运行代码**
从以下任一社交编码站点下载 **Copying and Moving Worksheets (Aspose.Cells)**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
