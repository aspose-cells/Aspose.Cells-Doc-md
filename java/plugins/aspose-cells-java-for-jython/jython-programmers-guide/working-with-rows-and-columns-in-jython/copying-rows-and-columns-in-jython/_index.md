---
title: Copying Rows and Columns in Jython
type: docs
weight: 30
url: /java/copying-rows-and-columns-in-jython/
---

## **Aspose.Cells - Copying Rows and Columns**
To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

class RowsAndColumns:

    def __init__(self):



        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



        # Copying Rows

        self.copy_rows()

        # Copying Columns

        self.copy_columns()



    def copy_rows(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Copy the second row with data, formattings, images and drawing objects

        # to the 12th row in the worksheet.

        worksheet.getCells().copyRow(worksheet.getCells(),1,11)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Rows.xls")

        print "Copy Rows Successfully." 



    def copy_columns(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook()

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Put some data into header rows (A1:A4)

        i = 0

        while i < 5:

            worksheet.getCells().get(i, 0).setValue("Header Row #i")






        # Put some detail data (A5:A999)

        i = 5

        while i < 1000:

            worksheet.getCells().get(i, 0).setValue("Detail Row #i")



        # Create another Workbook.

        workbook1 = Workbook()

        # Get the first worksheet in the book.

        worksheet1 = workbook1.getWorksheets().get(0)

        # Copy the first column from the first worksheet of the first workbook into

        # the first worksheet of the second workbook.

        worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

        # Autofit the column.

        worksheet1.autoFitColumn(2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Columns.xls")

        print "Copy Columns Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **Download Running Code**
Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

- [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
