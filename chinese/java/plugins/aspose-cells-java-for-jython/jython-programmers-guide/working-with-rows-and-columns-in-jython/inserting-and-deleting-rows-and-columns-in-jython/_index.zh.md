---
title: 在Jython中插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns-in-jython/
---

## **Aspose.Cells - 插入和删除行和列**
使用**Aspose.Cells Java for Jython**进行附加文档。这里可以看到示例代码。

**Jython 代码**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

class RowsAndColumns:

    def __init__(self):



        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'





        # Inserting a Row

        self.insert_row()

        # Inserting Multiple Rows

        self.insert_multiple_rows()

        # Deleting a Row

        self.delete_row()

        # Deleting Multiple Rows

        self.delete_multiple_rows()

        # Inseting one or Multiple Columns

        self.insert_column()

        # Deleting a Column

        self.delete_column()

        # Grouping Rows & Columns

        self.group_rows_columns()

        # Ungrouping Rows & Columns

        self.ungroup_rows_columns()



    def insert_row(dataDir):



        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'



        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + "Book1.xls")

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Inserting a row into the worksheet at 3rd position

        worksheet.getCells().insertRows(2,1)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Insert Row.xls")

        print "Insert Row Successfully." 



    def insert_multiple_rows(dataDir):



        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'



        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Inserting a row into the worksheet at 3rd position

        worksheet.getCells().insertRows(2,10)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Insert Multiple Rows.xls")

        print "Insert Multiple Rows Successfully." 



    def delete_row(dataDir):



        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'



        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Deleting 3rd row from the worksheet

        worksheet.getCells().deleteRows(2,1,True)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Delete Row.xls")

        print "Delete Row Successfully." 



    def delete_multiple_rows(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Deleting 10 rows from the worksheet starting from 3rd row

        worksheet.getCells().deleteRows(2,10,True)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Delete Multiple Rows.xls")

        print "Delete Multiple Rows Successfully." 



    def insert_column(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Inserting a column into the worksheet at 2nd position

        worksheet.getCells().insertColumns(1,1)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Insert Column.xls")

        print "Insert Column Successfully." 



    def delete_column(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Deleting a column from the worksheet at 2nd position

        worksheet.getCells().deleteColumns(1,1,True)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Delete Column.xls")

        print "Delete Column Successfully." 



    def group_rows_columns(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        cells = worksheet.getCells()

        # Grouping first six rows (from 0 to 5) and making them hidden by passing true

        cells.groupRows(0,5,True)

        # Grouping first three columns (from 0 to 2) and making them hidden by passing true

        cells.groupColumns(0,2,True)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Group Rows And Columns.xls")

        print "Group Rows And Columns Successfully." 



    def ungroup_rows_columns(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Group Rows And Columns.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        cells = worksheet.getCells()

        # Ungrouping first six rows (from 0 to 5)

        cells.ungroupRows(0,5)

        # Ungrouping first three columns (from 0 to 2)

        cells.ungroupColumns(0,2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Ungroup Rows And Columns.xls")

        print "Ungroup Rows And Columns Successfully."        


if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**Append Documents (Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
