---
title: Adjusting Row Height and Column Width in PHP
type: docs
weight: 10
url: /java/adjusting-row-height-and-column-width-in-php/
---

## **Aspose.Cells - Adjusting Row Height and Column Width**
### **Setting the Row Height**
It is possible to set the height of a single row by calling the Cells collection's setRowHeight method. The setRowHeight method takes the folloing parameters:

- **Row index**, the index of the row that you're changing the height of.
- **Row height**, the row height to apply on the row.

**PHP Code**

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
### **Setting the Column Width**
Set the width of a column by calling the Cells collection's setColumnWidth method. The setColumnWidth method takes the following parameters:

- **Column index**, the index of the column that you're changing the width of.
- **Column width**, the desired column width.

**PHP Code**

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
## **Download Running Code**
Download **Adjusting Row Height and Column Width (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
