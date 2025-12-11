---
title: Adding Worksheets to New Excel File in Jython
type: docs
weight: 10
url: /java/adding-worksheets-to-new-excel-file-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells – Adding Worksheets to a New Excel File**
To add worksheets to a new Excel file using **Aspose.Cells for Java in Jython**, see the example code below.

**Jython Code**

{{< highlight java >}}
 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class AddingWorksheetstoNewExcelFile:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/AddingWorksheetstoNewExcelFile/'



        workbook = Workbook(dataDir + "Book1.xls")

        # Adding a new worksheet to the Workbook object

        worksheets = workbook.getWorksheets()

        sheetIndex = worksheets.add()

        worksheet = worksheets.get(sheetIndex)

        # Setting the name of the newly added worksheet

        worksheet.setName("My Worksheet")

        # Saving the Excel file

        workbook.save(dataDir + "book.out.xls")

        # Print message

        print "Sheet added successfully."

if __name__ == '__main__':        

    AddingWorksheetstoNewExcelFile()
{{< /highlight >}}

## **Download Running Code**
Download the code for **Adding Worksheets to a New Excel File (Aspose.Cells)** from any of the social coding sites listed below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/AddingWorksheetstoNewExcelFile.py)
