---
title: Conversión a XPS en Jython
type: docs
weight: 30
url: /es/java/converting-to-xps-in-jython/
---
## **Aspose.Cells - Conversión a XPS**
 Para anexar documentos usando**Aspose.Cells Java para Jython**. Aquí puedes ver el código de ejemplo.

**Código Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import ImageFormat;

from com.aspose.cells import ImageOrPrintOptions;

from com.aspose.cells import SheetRender;

from com.aspose.cells import SaveFormat;



class ConvertingToXPS:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingToXPS/'



        saveFormat = SaveFormat

        workbook = Workbook(dataDir + "Book1.xls")

        #Get the first worksheet.

        sheet = workbook.getWorksheets().get(0)

        #Apply different Image and Print options

        options = ImageOrPrintOptions()

        #Set the Format

        options.setSaveFormat(saveFormat.XPS)

        # Render the sheet with respect to specified printing options

        sr = SheetRender(sheet, options)

        sr.toImage(0, dataDir + "out_printingxps.xps")

        #Save the complete Workbook in XPS format

        workbook.save(dataDir + "out_whole_printingxps", saveFormat.XPS)

        # Print message

        print "Excel to XPS conversion performed successfully."



if __name__ == '__main__':        

    ConvertingToXPS()

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Adjuntar Documentos (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingToXPS.py)
