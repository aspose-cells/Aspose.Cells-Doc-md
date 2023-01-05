---
title: 在 PHP 中自动调整行和列
type: docs
weight: 20
url: /zh/java/autofit-rows-and-columns-in-php/
---
## **Aspose.Cells - 自动调整行和列**
### **自动调整行**
自动调整行的宽度和高度的最直接的方法是调用 Worksheet 类的 autoFitRow 方法。 autoFitRow 方法将（要调整大小的行的）行索引作为参数。

**PHP代码**

{{< highlight "php" >}}

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
### **自动调整列**
自动调整列的宽度和高度的最简单方法是调用 Worksheet 类的 autoFitColumn 方法。 autoFitColumn 方法将（即将调整大小的列的）列索引作为参数。

**PHP代码**

{{< highlight "php" >}}

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
下载**自动调整行和列 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
