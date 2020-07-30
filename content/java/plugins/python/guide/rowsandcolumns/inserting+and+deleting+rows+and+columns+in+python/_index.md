---
title : "Inserting and Deleting Rows and Columns in Python" 
description : "" 
weight : 20762 
toc : false
type: docs
url: /java/plugins/python/guide/rowsandcolumns/inserting+and+deleting+rows+and+columns+in+python/
---

# Aspose.Cells for Java : Inserting and Deleting Rows and Columns in Python


## Aspose.Cells - Managing Rows/Columns

##### Inserting a Row

Insert a row into at any location by calling the`insertRows`method of the`Cells`collection. The`insertRows`method takes the index of the row where the new row will be inserted as the first argument, and the number of rows to be inserted as the second argument.

**Python Code**

{{< code lang="cs" >}}
def insert_row(self):

# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file
worksheet = workbook.getWorksheets().get(0)

# Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2,1)

# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 
{{< /code >}}

##### Inserting Multiple Rows

To insert multiple rows into the worksheet, call the`insertRows`method of the`Cells`collection. The`InsertRows`method takes two parameters:

*   Row index, the index of the row from where the new rows will be inserted.
*   Number of rows, total number of rows that need to be inserted.

**Python Code**

{{< code lang="cs" >}}
def insert_multiple_rows(self):

# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + 'Book1.xls')

# Accessing the first worksheet in the Excel file
worksheet = workbook.getWorksheets().get(0)

# Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2,10)

# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 

{{< /code >}}

##### Deleting a Row

To delete a row at any location, call the`deleteRows`method of the`Cells`collection. The`DeleteRows`method takes two parameters:

*   Row index, the index of the row from where the rows will be deleted.
*   Number of rows, total number of rows that need to be deleted.

**Python Code**

{{< code lang="cs" >}}
def delete_row(self):

# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + 'Book1.xls')

# Accessing the first worksheet in the Excel file
worksheet = workbook.getWorksheets().get(0)

# Deleting 3rd row from the worksheet
worksheet.getCells().deleteRows(2,1,True)

# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 
{{< /code >}}

##### Deleting Multiple Rows

To delete multiple rows from a worksheet, call the`deleteRows`method of the`Cells`collection. The`DeleteRows`method takes two parameters:

*   Row index, the index of the row from where the rows will be deleted.
*   Number of rows, total number of rows that need to be deleted.

**Python Code**

{{< code lang="cs" >}}
def delete_multiple_rows(self):

# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + 'Book1.xls')

# Accessing the first worksheet in the Excel file
worksheet = workbook.getWorksheets().get(0)

# Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2,10,True)

# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 

{{< /code >}}

##### Inserting a Column

Developers can also insert a column into the worksheet at any location by calling the`insertColumns`method of the`Cells`collection.`insertColumns`method takes two parameters:

*   Column index, the index of the column from where the column will be inserted
*   Number of columns, total number of columns that need to be inserted

**Python Code**

{{< code lang="cs" >}}
def insert_column(self):

# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + 'Book1.xls')

# Accessing the first worksheet in the Excel file
worksheet = workbook.getWorksheets().get(0)

# Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumns(1,1)

# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 

{{< /code >}}

##### Deleting a Column

To delete a column from the worksheet at any location, call the`deleteColumns`method of the`Cells`collection. The`deleteColumns`method takes the following parameters:

*   Column index, the index of the column from where the column will be deleted.
*   Number of columns, total number of columns that need to be deleted.
*   Shift cells, Boolean parameter to indicate whether to shift the cells left after deletion.

**Python Code**

{{< code lang="cs" >}}
def delete_column(self):

# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + 'Book1.xls')

# Accessing the first worksheet in the Excel file
worksheet = workbook.getWorksheets().get(0)

# Deleting a column from the worksheet at 2nd position
worksheet.getCells().deleteColumns(1,1,True)

# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 

{{< /code >}}

## Download Running Code

Download **Managing Rows/Columns (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

