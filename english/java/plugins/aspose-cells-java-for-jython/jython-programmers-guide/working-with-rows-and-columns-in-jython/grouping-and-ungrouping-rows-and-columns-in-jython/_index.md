---  
title: Grouping and Ungrouping Rows and Columns in Jython  
type: docs  
weight: 40  
url: /java/grouping-and-ungrouping-rows-and-columns-in-jython/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Aspose.Cells - Grouping and Ungrouping Rows and Columns**  
To work with rows and columns using **Aspose.Cells Java for Jython**. Here you can see an example code.  

**Jython Code**  

{{< highlight java >}}  

```python
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
        # Instantiating a Workbook object by Excel file path
        workbook = Workbook(dataDir + 'Book1.xls')
        # Accessing the first worksheet in the Excel file
        worksheet = workbook.getWorksheets().get(0)
        cells = worksheet.getCells()
        # Grouping first six rows (from 0 to 5) and making them hidden by passing true
        cells.groupRows(0, 5, True)
        # Grouping first three columns (from 0 to 2) and making them hidden by passing true
        cells.groupColumns(0, 2, True)
        # Saving the modified Excel file in default (that is Excel 2003) format
        workbook.save(dataDir + "Group Rows And Columns.xls")
        print "Group Rows and Columns successfully."

    def ungroup_rows_columns(dataDir):
        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'
        # Instantiating a Workbook object by Excel file path
        workbook = Workbook(dataDir + 'Group Rows And Columns.xls')
        # Accessing the first worksheet in the Excel file
        worksheet = workbook.getWorksheets().get(0)
        cells = worksheet.getCells()
        # Ungrouping first six rows (from 0 to 5)
        cells.ungroupRows(0, 5)
        # Ungrouping first three columns (from 0 to 2)
        cells.ungroupColumns(0, 2)
        # Saving the modified Excel file in default (that is Excel 2003) format
        workbook.save(dataDir + "Ungroup Rows And Columns.xls")
        print "Ungroup Rows and Columns successfully."

if __name__ == '__main__':
    RowsAndColumns()
```  

{{< /highlight >}}  

## **Download Running Code**  
Download **Append Documents (Aspose.Cells)** from any of the following social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
