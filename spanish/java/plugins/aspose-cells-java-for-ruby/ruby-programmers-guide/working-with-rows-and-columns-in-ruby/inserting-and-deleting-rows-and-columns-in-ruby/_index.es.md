---
title: Insertar y Eliminar Filas y Columnas en Ruby
type: docs
weight: 60
url: /es/java/inserting-and-deleting-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Administración de Filas/Columnas**
### **Insertar una Fila**
Insertar una fila en cualquier ubicación llamando al método insertRows de la colección Cells. El método insertRows toma el índice de la fila donde se insertará la nueva fila como primer argumento, y el número de filas a insertar como segundo argumento.

**Código Ruby**

{{< highlight ruby >}}

 def insert_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Row.xls")

    puts "Insert Row Successfully."

end   

{{< /highlight >}}
### **Insertar Múltiples Filas**
Para insertar múltiples filas en la hoja de cálculo, llame al método insertRows de la colección Cells. El método insertRows toma dos parámetros:

- Índice de la fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, número total de filas que deben ser insertadas.

**Código Ruby**

{{< highlight ruby >}}

 def insert_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,10)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Multiple Rows.xls")

    puts "Insert Multiple Rows Successfully."

end

{{< /highlight >}}
### **Eliminar una Fila**
Para eliminar una fila en cualquier ubicación, llame al método deleteRows de la colección Cells. El método deleteRows toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, número total de filas que deben ser eliminadas.

**Código Ruby**

{{< highlight ruby >}}

 def delete_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 3rd row from the worksheet

    worksheet.getCells().deleteRows(2,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Row.xls")

    puts "Delete Row Successfully."

end

{{< /highlight >}}
### **Eliminar Múltiples Filas**
Para eliminar múltiples filas de una hoja de cálculo, llame al método deleteRows de la colección Cells. El método deleteRows toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, número total de filas que deben ser eliminadas.

**Código Ruby**

{{< highlight ruby >}}

 def delete_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 10 rows from the worksheet starting from 3rd row

    worksheet.getCells().deleteRows(2,10,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Multiple Rows.xls")

    puts "Delete Multiple Rows Successfully."

end 

{{< /highlight >}}
### **Insertar una columna**
Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método insertColumns de la colección Cells. El método insertColumns toma dos parámetros:

- Índice de la columna, el índice de la columna desde donde se insertará la columna
- Número de columnas, el número total de columnas que se deben insertar

**Código Ruby**

{{< highlight ruby >}}

 def insert_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a column into the worksheet at 2nd position

    worksheet.getCells().insertColumns(1,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Column.xls")

    puts "Insert Column Successfully."

end  

{{< /highlight >}}
### **Eliminar una columna**
Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al método deleteColumns de la colección Cells. El método deleteColumns toma los siguientes parámetros:

- Índice de columna, el índice de la columna desde donde se va a eliminar la columna.
- Número de columnas, el número total de columnas que se deben eliminar.
- Desplazar celdas, parámetro booleano para indicar si se deben desplazar las celdas a la izquierda después de la eliminación.

**Código Ruby**

{{< highlight ruby >}}

 def delete_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting a column from the worksheet at 2nd position

    worksheet.getCells().deleteColumns(1,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Column.xls")

    puts "Delete Column Successfully."

end   

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Gestión de Filas/Columnas (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
