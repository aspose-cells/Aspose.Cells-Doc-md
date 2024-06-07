---
title: 在PHP中调整行高和列宽
type: docs
weight: 10
url: /zh/java/adjusting-row-height-and-column-width-in-php/
---

## **Aspose.Cells - 调整行高和列宽**
### **设置行高**
通过调用Cells集合的setRowHeight方法来设置单行的高度。setRowHeight方法接受以下参数：

- **行索引**，要更改其高度的行的索引。
- **行高**，要应用于该行的行高。

**PHP代码**

{{< highlight php >}}

 public static function set_row_height($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();

    # Setting the height of the second row to 13

    $cells->setRowHeight(1, 13);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Set Row Height.xls");

    print "Set Row Height Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **设置列宽**
通过调用Cells集合的setColumnWidth方法来设置列的宽度。setColumnWidth方法接受以下参数：

- **列索引**，要更改其宽度的列的索引。
- **列宽**，所需的列宽。

**PHP代码**

{{< highlight php >}}

 public static function set_column_width($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();

    # Setting the width of the second column to 17.5

    $cells->setColumnWidth(1, 17.5);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Set Column Width.xls");

    print "Set Column Width Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **下载运行代码**
从以下提到的社交编码网站下载**调整行高和列宽(Aspose.Cells)**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
