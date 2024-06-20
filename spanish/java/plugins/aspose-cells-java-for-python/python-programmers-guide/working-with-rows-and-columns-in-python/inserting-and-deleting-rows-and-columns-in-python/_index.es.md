---
title: Insertar y Borrar Filas y Columnas en Python
type: docs
weight: 60
url: /es/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: "crear XLSX en Python, crear XLS en Python, XLS python, XLSX python, XLT python, XLTX python, insertar fila python, insertar columna python, Excel python"
description: Usar Python Excel API para crear hojas de cálculo de Excel en Python. Insertar o borrar filas de XLSX o XLS en tus aplicaciones de Python sin MS Office.
---

## **Crear Hojas de Cálculo de Excel en Python - Manejando Filas/Columnas**
### **Insertar una Fila**
Insertar una fila en cualquier ubicación llamando al método insertRows de la colección Cells. El método insertRows toma el índice de la fila donde se insertará la nueva fila como primer argumento y el número de filas a insertar como segundo argumento. A continuación se detallan los pasos:

- Cargar libro de trabajo XLS o XLSX
- Acceder a la hoja de cálculo
- Insertar la fila
- Guardar como libro de trabajo XLS o XLSX

**Código Python**

{{< highlight python >}}

 def insert_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 

{{< /highlight >}}
### **Insertar Múltiples Filas**
Para insertar múltiples filas en la hoja de cálculo, llame al método insertRows de la colección Cells. El método insertRows toma dos parámetros:

- Índice de la fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, número total de filas que deben ser insertadas.

**Código Python**

{{< highlight python >}}

 def insert_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,10)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 


{{< /highlight >}}
### **Eliminar una Fila**
Para eliminar una fila en cualquier ubicación, llame al método deleteRows de la colección Cells. El método deleteRows toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, número total de filas que deben ser eliminadas.

**Código Python**

{{< highlight python >}}

 def delete_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 3rd row from the worksheet

worksheet.getCells().deleteRows(2,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 

{{< /highlight >}}
### **Eliminar Múltiples Filas**
Para eliminar múltiples filas de una hoja de cálculo, llame al método deleteRows de la colección Cells. El método deleteRows toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, número total de filas que deben ser eliminadas.

**Código Python**

{{< highlight python >}}

 def delete_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 10 rows from the worksheet starting from 3rd row

worksheet.getCells().deleteRows(2,10,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 


{{< /highlight >}}
### **Insertar una columna**
Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método insertColumns de la colección Cells. El método insertColumns toma dos parámetros:

- Índice de la columna, el índice de la columna desde donde se insertará la columna
- Número de columnas, el número total de columnas que se deben insertar

**Código Python**

{{< highlight python >}}

 def insert_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a column into the worksheet at 2nd position

worksheet.getCells().insertColumns(1,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 


{{< /highlight >}}
### **Eliminar una columna**
Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al método deleteColumns de la colección Cells. El método deleteColumns toma los siguientes parámetros:

- Índice de columna, el índice de la columna desde donde se va a eliminar la columna.
- Número de columnas, el número total de columnas que se deben eliminar.
- Desplazar celdas, parámetro booleano para indicar si se deben desplazar las celdas a la izquierda después de la eliminación.

**Código Python**

{{< highlight python >}}

 def delete_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting a column from the worksheet at 2nd position

worksheet.getCells().deleteColumns(1,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 


{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Gestión de Filas/Columnas (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
