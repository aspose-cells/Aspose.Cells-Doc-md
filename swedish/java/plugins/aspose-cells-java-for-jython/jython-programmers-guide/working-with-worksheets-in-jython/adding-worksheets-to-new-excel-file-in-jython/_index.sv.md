---
title: Lägga till kalkylblad till ny Excel-fil i Jython
type: docs
weight: 10
url: /sv/java/adding-worksheets-to-new-excel-file-in-jython/
---
## **Aspose.Cells - Lägga till kalkylblad i nytt Excel**
 För att lägga till dokument med hjälp av**Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Code**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class AddingWorksheetstoNewExcelFile:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/AddingWorksheetstoNewExcelFile/'



        workbook = Workbook(dataDir + "Book1.xls")

        #Adding a new worksheet to the Workbook object

        worksheets = workbook.getWorksheets()

        sheetIndex = worksheets.add()

        worksheet = worksheets.get(sheetIndex)

        #Setting the name of the newly added worksheet

        worksheet.setName("My Worksheet")

        #Saving the Excel file

        workbook.save(dataDir + "book.out.xls")

        #Print Message

        print "Sheet added successfully."

if __name__ == '__main__':        

    AddingWorksheetstoNewExcelFile()

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Bifoga dokument (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/AddingWorksheetstoNewExcelFile.py)
