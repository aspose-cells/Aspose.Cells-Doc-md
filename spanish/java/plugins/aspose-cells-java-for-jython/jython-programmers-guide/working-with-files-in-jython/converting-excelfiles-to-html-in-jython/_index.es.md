---
title: Convertir Archivos de Excel a Html en Jython
type: docs
weight: 10
url: /es/java/converting-excelfiles-to-html-in-jython/
---

## **Aspose.Cells - Convertir Archivos de Excel a Html**
Para agregar documentos usando **Aspose.Cells Java for Jython**. Aquí puedes ver código de ejemplo.

**Código Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class ConvertingExcelFilesToHtml:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingExcelFilesToHtml/'



        saveFormat = SaveFormat

        workbook = Workbook(dataDir + "Book1.xls")

        #Save the document in PDF format

        workbook.save(dataDir + "OutBook1.html", saveFormat.HTML)

        # Print message

        print "\n Excel to HTML conversion performed successfully."



if __name__ == '__main__':        

    ConvertingExcelFilesToHtml()

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Agregar documentos (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingExcelFilesToHtml.py)
