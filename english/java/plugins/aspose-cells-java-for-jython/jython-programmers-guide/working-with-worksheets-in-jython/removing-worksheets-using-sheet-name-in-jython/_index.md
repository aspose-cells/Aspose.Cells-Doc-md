---  
title: Removing Worksheets using Sheet Name in Jython  
type: docs  
weight: 120  
url: /java/removing-worksheets-using-sheet-name-in-jython/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Aspose.Cells – Removing Worksheets using Sheet Name**  

This example demonstrates how to remove a worksheet by its name using **Aspose.Cells for Java in Jython**. See the sample code below.  

**Jython Code**  

{{< highlight java >}}  
```python
from aspose-cells import Settings
from com.aspose.cells import Workbook
from java.io import FileInputStream


class RemovingWorksheetsUsingSheetName:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithWorksheets/RemovingWorksheetsusingSheetName/'

        # Creating a file stream containing the Excel file to be opened
        fstream = FileInputStream(dataDir + "Book1.xls")

        # Instantiating a Workbook object with the stream
        workbook = Workbook(fstream)

        # Removing a worksheet using its sheet name
        workbook.getWorksheets().removeAt("Sheet1")

        # Saving the Excel file
        workbook.save(dataDir + "book.out.xls")

        # Closing the file stream to free all resources
        fstream.close()

        # Print message
        print "Sheet removed successfully."
        

if __name__ == '__main__':
    RemovingWorksheetsUsingSheetName()
```  
{{< /highlight >}}  

## **Download Runnable Code**  

Download **Removing Worksheets (Aspose.Cells)** from any of the below mentioned source‑code repositories:  

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetName.py)  
