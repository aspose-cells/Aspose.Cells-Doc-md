---
title: Copiando Filas y Columnas en Ruby
type: docs
weight: 30
url: /es/java/copying-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Copiando Filas y Columnas**
### **Copiando Filas**
Aspose.Cells proporciona el método copyRow de la clase Cells. Este método copia todo tipo de datos, incluidas fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo de la fila de origen a la fila de destino.

El método copyRow toma los siguientes parámetros:

- el objeto Cells de origen,
- el índice de fila de origen, y
- el índice de fila de destino.

**Código Ruby**

{{< highlight ruby >}}

 def copy_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the worksheet.

    worksheet.getCells().copyRow(worksheet.getCells(),1,11)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Rows.xls")

    puts "Copy Rows Successfully."

end

{{< /highlight >}}
### **Copiar columnas**
Aspose.Cells proporciona el método copyColumn de la clase Cells, este método copia todo tipo de datos, incluyendo fórmulas - con referencias actualizadas - y valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo, desde la columna de origen a la columna de destino.

El método copyColumn toma los siguientes parámetros:

- el objeto Cells de origen,
- índice de columna de origen, y
- el índice de columna de destino.

**Código Ruby**

{{< highlight ruby >}}

 def copy_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Put some data into header rows (A1:A4)

    i = 0

    while i < 5

        worksheet.getCells().get(i, 0).setValue("Header Row #{i}")

        i +=1

    end

    # Put some detail data (A5:A999)

    i = 5

    while i < 1000

        worksheet.getCells().get(i, 0).setValue("Detail Row #{i}")

        i +=1

    end

    # Create another Workbook.

    workbook1 = Rjb::import('com.aspose.cells.Workbook').new

    # Get the first worksheet in the book.

    worksheet1 = workbook1.getWorksheets().get(0)

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

    # Autofit the column.

    worksheet1.autoFitColumn(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Columns.xls")

    puts "Copy Columns Successfully."

end

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Copiar Filas y Columnas (Aspose.Cells)** desde cualquiera de los siguientes sitios de codificación social:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
