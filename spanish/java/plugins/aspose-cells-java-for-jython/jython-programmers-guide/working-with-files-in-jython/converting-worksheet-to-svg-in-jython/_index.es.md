---
title: Convertir hoja de trabajo a SVG en Jython
type: docs
weight: 40
url: /es/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - Conversión de hoja de trabajo a SVG**
 Para anexar documentos usando**Aspose.Cells Java para Jython**. Aquí puedes ver el código de ejemplo.

**Código Jython**

{{< highlight "java" >}}

 desde la configuración de importación de aspose-cells

desde com.aspose.cells libro de trabajo de importación

de com.aspose.cells importar ImageFormat

desde com.aspose.cells importar ImageOrPrintOptions

desde com.aspose.cells importar SheetRender

desde com.aspose.cells importar SaveFormat



clase ConvertingWorksheetToSVG:

 definitivamente__en eso__(uno mismo):

 dataDir = Configuración.dataDir + 'Trabajar con archivos/Convertir hoja de trabajo a SVG/'



 saveFormat = Guardar formato

 libro de trabajo = Libro de trabajo (dataDir + "Book1.xls")

 #Convierta cada hoja de trabajo en formato svg en una sola página.

 imgOptions = ImageOrPrintOptions()

 imgOptions.setSaveFormat(saveFormat.SVG)

 imgOptions.setOnePagePerSheet(Verdadero)

 #Convertir cada hoja de trabajo en formato svg

 sheetCount = libro de trabajo.getWorksheets().getCount()

 #para(i=0; yo<sheetCount; i++)

        for i in range(sheetCount):



            sheet = workbook.getWorksheets().get(i)

            sr = SheetRender(sheet, imgOptions)

            pageCount = sr.getPageCount()

            #for (k = 0 k < pageCount k++)

            for k in range(pageCount):



                #Output the worksheet into Svg image format

                sr.toImage(k, dataDir + sheet.getName() + ".out.svg")





        # Print message

        print "Excel to SVG conversion completed successfully."



if __name__ == '__main__':        

    ConvertingWorksheetToSVG()

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Adjuntar Documentos (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
