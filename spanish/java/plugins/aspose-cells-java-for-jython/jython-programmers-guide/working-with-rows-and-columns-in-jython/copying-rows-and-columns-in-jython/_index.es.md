---
title: Copiar filas y columnas en Jython
type: docs
weight: 30
url: /es/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells - Copia de filas y columnas**
 Para anexar documentos usando**Aspose.Cells Java para Jython**. Aquí puedes ver el código de ejemplo.

**Código Jython**

{{< highlight "java" >}}

 desde la configuración de importación de aspose-cells

desde com.aspose.cells libro de trabajo de importación

clase filas y columnas:

 definitivamente__en eso__(uno mismo):



 dataDir = Configuración.dataDir + 'TrabajandoConFilasYColumnas/FilasYColumnas'



 # Copiando filas

 self.copiar_filas()

 # Copiando Columnas

 self.copiar_columnas()



 def copy_rows(dataDir):

 dataDir = Configuración.dataDir + 'TrabajandoConFilasYColumnas/FilasYColumnas/'

 # Creación de instancias de un objeto de libro de trabajo por ruta de archivo de Excel

 libro = Workbook(dataDir + 'Book1.xls')

 # Accediendo a la primera hoja de trabajo en el archivo de Excel

 hoja de trabajo = libro de trabajo.getWorksheets().get(0)

 # Copie la segunda fila con datos, formatos, imágenes y objetos de dibujo

 # hasta la fila 12 de la hoja de cálculo.

 hoja de trabajo.getCells().copyRow(hoja de trabajo.getCells(),1,11)

 # Guardar el archivo de Excel modificado en formato predeterminado (es decir, Excel 2003)

libro de trabajo. guardar (dataDir + "Copiar filas.xls")

 imprimir "Copiar filas con éxito".



 def copy_columns(dataDir):

 dataDir = Configuración.dataDir + 'TrabajandoConFilasYColumnas/FilasYColumnas/'

 # Creación de instancias de un objeto de libro de trabajo por ruta de archivo de Excel

 libro de trabajo = libro de trabajo()

 # Accediendo a la primera hoja de trabajo en el archivo de Excel

 hoja de trabajo = libro de trabajo.getWorksheets().get(0)

 # Ponga algunos datos en las filas del encabezado (A1:A4)

 yo = 0

 mientras yo< 5:

            worksheet.getCells().get(i, 0).setValue("Header Row #i")






        # Put some detail data (A5:A999)

        i = 5

        while i < 1000:

            worksheet.getCells().get(i, 0).setValue("Detail Row #i")



        # Create another Workbook.

        workbook1 = Workbook()

        # Get the first worksheet in the book.

        worksheet1 = workbook1.getWorksheets().get(0)

        # Copy the first column from the first worksheet of the first workbook into

        # the first worksheet of the second workbook.

        worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

        # Autofit the column.

        worksheet1.autoFitColumn(2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Columns.xls")

        print "Copy Columns Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Adjuntar Documentos (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
