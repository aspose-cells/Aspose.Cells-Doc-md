---
title : "Inserting and Deleting Rows and Columns in Ruby" 
description : "" 
weight : 20736 
toc : false
type: docs
url: /java/plugins/ruby/guide/rowsandcolumns/inserting+and+deleting+rows+and+columns+in+ruby/
---

# Aspose.Cells for Java : Inserting and Deleting Rows and Columns in Ruby


## Aspose.Cells - Managing Rows/Columns

##### Inserting a Row

Insert a row into at any location by calling the`insertRows`method of the`Cells`collection. The`insertRows`method takes the index of the row where the new row will be inserted as the first argument, and the number of rows to be inserted as the second argument.

**Ruby Code**

{{< code lang="cs" >}}
def insert_row()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position
    worksheet.getCells().insertRows(2,1)

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(data_dir + "Insert Row.xls")

    puts "Insert Row Successfully."
end   
{{< /code >}}

##### Inserting Multiple Rows

To insert multiple rows into the worksheet, call the`insertRows`method of the`Cells`collection. The`InsertRows`method takes two parameters:

*   Row index, the index of the row from where the new rows will be inserted.
*   Number of rows, total number of rows that need to be inserted.

**Ruby Code**

{{< code lang="cs" >}}
def insert_multiple_rows()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position
    worksheet.getCells().insertRows(2,10)

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(data_dir + "Insert Multiple Rows.xls")

    puts "Insert Multiple Rows Successfully."
end
{{< /code >}}

##### Deleting a Row

To delete a row at any location, call the`deleteRows`method of the`Cells`collection. The`DeleteRows`method takes two parameters:

*   Row index, the index of the row from where the rows will be deleted.
*   Number of rows, total number of rows that need to be deleted.

**Ruby Code**

{{< code lang="cs" >}}
def delete_row()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.getWorksheets().get(0)

    # Deleting 3rd row from the worksheet
    worksheet.getCells().deleteRows(2,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(data_dir + "Delete Row.xls")

    puts "Delete Row Successfully."
end
{{< /code >}}

##### Deleting Multiple Rows

To delete multiple rows from a worksheet, call the`deleteRows`method of the`Cells`collection. The`DeleteRows`method takes two parameters:

*   Row index, the index of the row from where the rows will be deleted.
*   Number of rows, total number of rows that need to be deleted.

**Ruby Code**

{{< code lang="cs" >}}
def delete_multiple_rows()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.getWorksheets().get(0)

    # Deleting 10 rows from the worksheet starting from 3rd row
    worksheet.getCells().deleteRows(2,10,true)

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(data_dir + "Delete Multiple Rows.xls")

    puts "Delete Multiple Rows Successfully."
end 
{{< /code >}}

##### Inserting a Column

Developers can also insert a column into the worksheet at any location by calling the`insertColumns`method of the`Cells`collection.`insertColumns`method takes two parameters:

*   Column index, the index of the column from where the column will be inserted
*   Number of columns, total number of columns that need to be inserted

**Ruby Code**

{{< code lang="cs" >}}
def insert_column()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.getWorksheets().get(0)

    # Inserting a column into the worksheet at 2nd position
    worksheet.getCells().insertColumns(1,1)

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(data_dir + "Insert Column.xls")

    puts "Insert Column Successfully."
end  
{{< /code >}}

##### Deleting a Column

To delete a column from the worksheet at any location, call the`deleteColumns`method of the`Cells`collection. The`deleteColumns`method takes the following parameters:

*   Column index, the index of the column from where the column will be deleted.
*   Number of columns, total number of columns that need to be deleted.
*   Shift cells, Boolean parameter to indicate whether to shift the cells left after deletion.

**Ruby Code**

{{< code lang="cs" >}}
def delete_column()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.getWorksheets().get(0)

    # Deleting a column from the worksheet at 2nd position
    worksheet.getCells().deleteColumns(1,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(data_dir + "Delete Column.xls")

    puts "Delete Column Successfully."
end   
{{< /code >}}

## Download Running Code

Download **Managing Rows/Columns (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)

