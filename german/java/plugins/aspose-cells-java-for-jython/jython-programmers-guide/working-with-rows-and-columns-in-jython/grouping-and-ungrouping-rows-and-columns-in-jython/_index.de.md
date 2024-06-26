---
title: Gruppierung und Aufhebung der Gruppierung von Zeilen und Spalten in Jython
type: docs
weight: 40
url: /de/java/grouping-and-ungrouping-rows-and-columns-in-jython/
---

## **Aspose.Cells - Gruppierung und Aufhebung der Gruppierung von Zeilen und Spalten**
Zum Anfügen von Dokumenten mit **Aspose.Cells Java für Jython**. Hier sehen Sie Beispielscode.

**Jython-Code**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

class RowsAndColumns:

    def __init__(self):



        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



        # Grouping Rows & Columns

        self.group_rows_columns()

        # Ungrouping Rows & Columns

        self.ungroup_rows_columns()





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
## **Laufenden Code herunterladen**
Laden Sie **Dokumente anfügen (Aspose.Cells)** von einer der unten genannten Plattformen für soziale Codierung herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
