---
title: Convertir a Archivos MHTML en Jython
type: docs
weight: 20
url: /es/java/converting-to-mhtml-files-in-jython/
---

## **Aspose.Cells - Convertir a Archivos MHTML**
Para agregar documentos usando **Aspose.Cells Java for Jython**. Aquí puedes ver código de ejemplo.

**Código Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import HtmlSaveOptions

from com.aspose.cells import SaveFormat


class ConvertingToMhtmlFiles:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingToMhtmlFiles/'



        saveFormat = SaveFormat

        #Specify the file path

        filePath = dataDir + "Book1.xlsx"

        #Specify the HTML saving options

        sv = HtmlSaveOptions(saveFormat.M_HTML)

        #Instantiate a workbook and open the template XLSX file

        wb = Workbook(filePath)

        #Save the MHT file

        wb.save(filePath + ".out.mht", sv)

        # Print message

        print "Excel to MHTML conversion performed successfully."



if __name__ == '__main__':        

    ConvertingToMhtmlFiles()

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Agregar documentos (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingToMhtmlFiles.py)
