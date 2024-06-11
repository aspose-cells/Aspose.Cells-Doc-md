---
title: 在 PHP 中调整行和列的大小
type: docs
weight: 20
url: /zh/java/autofit-rows-and-columns-in-php/
---

## **Aspose.Cells - 自动调整行和列**
### **自适应调整行高**
自动调整行宽和行高最直接的方法是调用Worksheet类的autoFitRow方法。autoFitRow方法将行索引（要调整大小的行）作为参数。

**PHP 代码**

{{< highlight php >}}

 public static function autofit_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 3rd row of the worksheet

    $worksheet->autoFitRow(2);

    # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

    # cells (from 1st to 9th column) within the row

    #$worksheet->autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Row.xls");

    print "Autofit Row Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **自适应调整列宽**
自动调整列宽和列高的最简单方法是调用Worksheet类的autoFitColumn方法。autoFitColumn方法以列索引（即将调整大小的列）作为参数。

**PHP 代码**

{{< highlight php >}}

 public static function autofit_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 4th column of the worksheet

    $worksheet->autoFitColumn(3);

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of

    # cells (from 1st to 9th row) within the column

    #$worksheet->autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Column.xls");

    print "Autofit Column Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **下载运行代码**
从以下提到的任一社交编程网站下载**Autofit Rows and Columns (Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
