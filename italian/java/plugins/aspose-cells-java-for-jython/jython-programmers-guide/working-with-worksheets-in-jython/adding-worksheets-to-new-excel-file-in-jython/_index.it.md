---
title: Aggiunta di fogli di lavoro al nuovo file Excel in Jython
type: docs
weight: 10
url: /it/java/adding-worksheets-to-new-excel-file-in-jython/
---
## **Aspose.Cells - Aggiunta di fogli di lavoro a New Excel**
 Per aggiungere documenti utilizzando**Aspose.Cells Java per Jython**. Qui puoi vedere il codice di esempio.

**Codice Jython**

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
## **Scarica il codice in esecuzione**
 Scaricamento**Aggiungi documenti (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/AddingWorksheetstoNewExcelFile.py)
