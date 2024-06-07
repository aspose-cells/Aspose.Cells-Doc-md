---
title: 在PHP中隐藏和显示行和列
type: docs
weight: 50
url: /zh/java/hiding-and-showing-rows-and-columns-in-php/
description: 通过Aspose.Cells for PHP通过Java API学习如何隐藏和显示行和列。
keywords: 如何在PHP中隐藏和显示行和列，使用PHP隐藏行或列，PHP显示行或列。 
---

## **Aspose.Cells for PHP - 控制行和列的可见性**
### **如何在PHP中隐藏行和列**
开发人员可以通过调用Cells集合的HideRow和HideColumn方法来隐藏行或列。这两个方法分别接受行索引或列索引作为参数，以隐藏特定的行或列。

**PHP代码**

{{< highlight php >}}

 public static function hide_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Hiding the 3rd row of the worksheet

    $cells->hideRow(2);

    # Hiding the 2nd column of the worksheet

    $cells->hideColumn(1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Hide Rows And Columns.xls");

    print "Hide Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **如何使用PHP显示行和列**
开发人员可以通过调用Cells集合的UnhideRow和UnhideColumn方法来取消隐藏任何隐藏的行或列。这两个方法分别接受两个参数:

- **行或列索引** - 用于显示特定行或列的行或列索引。
- **行高或列宽度** - 在显示后分配给行或列的行高或列宽度。

**PHP代码**

{{< highlight php >}}

 public static function unhide_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Unhiding the 3rd row and setting its height to 13.5

    $cells->unhideRow(2,13.5);

    # Unhiding the 2nd column and setting its width to 8.5

    $cells->unhideColumn(1,8.5);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Unhide Rows And Columns.xls");

    print "Unhide Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**控制行和列的可见性（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
