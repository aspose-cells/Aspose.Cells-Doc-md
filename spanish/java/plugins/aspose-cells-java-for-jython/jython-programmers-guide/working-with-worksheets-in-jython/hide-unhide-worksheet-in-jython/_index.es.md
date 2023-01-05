---
title: Ocultar Mostrar hoja de trabajo en Jython
type: docs
weight: 70
url: /es/java/hide-unhide-worksheet-in-jython/
---
## **Aspose.Cells - Ocultar Mostrar hoja de trabajo**
 Para anexar documentos usando**Aspose.Cells Java para Jython**. Aquí puedes ver el código de ejemplo.

**Código Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class HideUnhideWorksheet:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/HideUnhideWorksheet/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Hiding the first worksheet of the Excel file

        worksheet.setVisible(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Worksheet 1 is now hidden, please check the output document."

if __name__ == '__main__':        

    HideUnhideWorksheet()

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Adjuntar Documentos (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/HideUnhideWorksheet.py)
