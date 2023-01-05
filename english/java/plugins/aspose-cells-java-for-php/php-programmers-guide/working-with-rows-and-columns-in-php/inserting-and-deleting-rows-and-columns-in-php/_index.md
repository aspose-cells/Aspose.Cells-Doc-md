---
title: Inserting and Deleting Rows and Columns in PHP
type: docs
weight: 60
url: /java/inserting-and-deleting-rows-and-columns-in-php/
---

## **Aspose.Cells - Managing Rows/Columns**
### **Inserting a Row**
Insert a row into at any location by calling the insertRows method of the Cells collection. The insertRows method takes the index of the row where the new row will be inserted as the first argument, and the number of rows to be inserted as the second argument.

**PHP Code**

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
### **Inserting Multiple Rows**
To insert multiple rows into the worksheet, call the insertRows method of the Cells collection. The InsertRows method takes two parameters:

- Row index, the index of the row from where the new rows will be inserted.
- Number of rows, total number of rows that need to be inserted.

**PHP Code**

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
### **Deleting a Row**
To delete a row at any location, call the deleteRows method of the Cells collection. The DeleteRows method takes two parameters:

- Row index, the index of the row from where the rows will be deleted.
- Number of rows, total number of rows that need to be deleted.

**PHP Code**

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
### **Deleting Multiple Rows**
To delete multiple rows from a worksheet, call the deleteRows method of the Cells collection. The DeleteRows method takes two parameters:

- Row index, the index of the row from where the rows will be deleted.
- Number of rows, total number of rows that need to be deleted.

**PHP Code**

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
### **Inserting a Column**
Developers can also insert a column into the worksheet at any location by calling the insertColumns method of the Cells collection. insertColumns method takes two parameters:

- Column index, the index of the column from where the column will be inserted
- Number of columns, total number of columns that need to be inserted

**PHP Code**

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
### **Deleting a Column**
To delete a column from the worksheet at any location, call the deleteColumns method of the Cells collection. The deleteColumns method takes the following parameters:

- Column index, the index of the column from where the column will be deleted.
- Number of columns, total number of columns that need to be deleted.
- Shift cells, Boolean parameter to indicate whether to shift the cells left after deletion.

**PHP Code**

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
## **Download Running Code**
Download **Managing Rows/Columns (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
