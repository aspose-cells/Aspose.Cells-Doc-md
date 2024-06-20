---
title: Agregar hojas de cálculo a un nuevo archivo de Excel en Jython
type: docs
weight: 10
url: /es/java/adding-worksheets-to-new-excel-file-in-jython/
---

## **Aspose.Cells - Agregar hojas de cálculo a un nuevo Excel**
Para agregar documentos usando **Aspose.Cells Java for Jython**. Aquí puedes ver código de ejemplo.

**Código Jython**

{{< highlight java >}}

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
## **Descargar Código en Ejecución**
Descargar **Agregar documentos (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/AddingWorksheetstoNewExcelFile.py)
