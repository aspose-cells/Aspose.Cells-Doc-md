---
title: إخفاء وإظهار الصفوف والأعمدة في جايثون
type: docs
weight: 50
url: /ar/java/hiding-and-showing-rows-and-columns-in-jython/
---
## **Aspose.Cells - إخفاء وإظهار الصفوف والأعمدة**
 لإلحاق المستندات باستخدام**Aspose.Cells Java لـ Jython**. هنا يمكنك أن ترى رمز المثال.

**كود جايثون**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

class RowsAndColumns:

    def __init__(self):



        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



        # Hiding Rows and Columns

        self.hide_rows_columns()

        # Showing Rows and Columns

        self.unhide_rows_columns()



    def hide_rows_columns(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        cells = worksheet.getCells()

        # Hiding the 3rd row of the worksheet

        cells.hideRow(2)

        # Hiding the 2nd column of the worksheet

        cells.hideColumn(1)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Hide Rows And Columns.xls")

        print "Hide Rows And Columns Successfully." 



    def unhide_rows_columns(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        cells = worksheet.getCells()

        # Unhiding the 3rd row and setting its height to 13.5

        cells.unhideRow(2,13.5)

        # Unhiding the 2nd column and setting its width to 8.5

        cells.unhideColumn(1,8.5)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Unhide Rows And Columns.xls")

        print "Unhide Rows And Columns Successfully." 

if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**إرفاق المستندات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
