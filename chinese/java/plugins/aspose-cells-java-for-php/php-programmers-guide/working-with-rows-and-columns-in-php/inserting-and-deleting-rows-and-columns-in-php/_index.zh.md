---
title: 在PHP中插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns-in-php/
description: 通过Aspose.Cells for PHP通过Java API学习如何插入和删除行和列。
keywords: 如何在PHP中插入和删除行和列，使用PHP插入行和列，PHP删除行和列，使用PHP插入行或列，通过PHP删除行或列。
---

## **Aspose.Cells - 管理行/列**
### **插入行**
通过调用单元格集合的insertRows方法在任何位置插入一行。insertRows方法的第一个参数是要插入新行的行索引，第二个参数是要插入的行数。

**PHP代码**

{{< highlight php >}}

 public static function insert_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a row into the worksheet at 3rd position

    $worksheet->getCells()->insertRows(2,1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Row.xls");

    print "Insert Row Successfully." . PHP_EOL;

}  

{{< /highlight >}}
### **插入多行**
要在工作表中插入多行，请调用单元格集合的insertRows方法。InsertRows方法接受两个参数:

- 行索引，新行将插入的起始行的索引。
- 行数，需要插入的总行数。

**PHP代码**

{{< highlight php >}}

 public static function insert_multiple_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a row into the worksheet at 3rd position

    $worksheet->getCells()->insertRows(2,10);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Multiple Rows.xls");

    print "Insert Multiple Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **删除一行**
要删除任何位置的行，请调用单元格集合的deleteRows方法。DeleteRows方法接受两个参数:

- 行索引，要删除的行的索引。
- 行数，需要删除的总行数。

**PHP代码**

{{< highlight php >}}

 public static function delete_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting 3rd row from the worksheet

    $worksheet->getCells()->deleteRows(2,1,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Row.xls");

    print "Delete Row Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **删除多行**
要从工作表中删除多行，请调用单元格集合的deleteRows方法。DeleteRows方法接受两个参数:

- 行索引，要删除的行的索引。
- 行数，需要删除的总行数。

**PHP代码**

{{< highlight php >}}

 public static function delete_multiple_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting 10 rows from the worksheet starting from 3rd row

    $worksheet->getCells()->deleteRows(2,10,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Multiple Rows.xls");

    print "Delete Multiple Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **插入列**
开发人员还可以通过调用单元格集合的insertColumns方法在工作表中的任何位置插入列。insertColumns方法接受两个参数:

- 列索引，要插入列的列索引
- 列数，需要插入的总列数

**PHP代码**

{{< highlight php >}}

 public static function insert_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a column into the worksheet at 2nd position

    $worksheet->getCells()->insertColumns(1,1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Column.xls");

    print "Insert Column Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **删除列**
要从工作表中的任何位置删除列，请调用单元格集合的deleteColumns方法。deleteColumns方法接受以下参数:

- 列索引，要删除列的列索引。
- 列数，需要删除的总列数。
- 移动单元格，一个布尔参数，用于指示删除后是否向左移动单元格。

**PHP代码**

{{< highlight php >}}

 public static function delete_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting a column from the worksheet at 2nd position

    $worksheet->getCells()->deleteColumns(1,1,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Column.xls");

    print "Delete Column Successfully." . PHP_EOL;

}  

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编程网站下载**管理行/列（Aspose.Cells）**:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
