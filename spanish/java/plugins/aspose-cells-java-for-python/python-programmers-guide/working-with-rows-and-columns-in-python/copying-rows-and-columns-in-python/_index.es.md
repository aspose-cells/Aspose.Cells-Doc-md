---
title: Copiar filas y columnas en Python
type: docs
weight: 30
url: /es/java/copying-rows-and-columns-in-python/
---

## **Aspose.Cells - Copiando Filas y Columnas**
### **Copiando Filas**
Aspose.Cells proporciona el método copyRow de la clase Cells. Este método copia todo tipo de datos, incluidas fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo de la fila de origen a la fila de destino.

El método copyRow toma los siguientes parámetros:

- el objeto Cells de origen,
- el índice de fila de origen, y
- el índice de fila de destino.

**Código Python**

{{< highlight java >}}

 def copy_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Copy the second row with data, formattings, images and drawing objects

\# to the 12th row in the worksheet.

worksheet.getCells().copyRow(worksheet.getCells(),1,11)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Rows.xls")

print "Copy Rows Successfully." 

{{< /highlight >}}
### **Copiar columnas**
Aspose.Cells proporciona el método copyColumn de la clase Cells, este método copia todo tipo de datos, incluyendo fórmulas - con referencias actualizadas - y valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo, desde la columna de origen a la columna de destino.

El método copyColumn toma los siguientes parámetros:

- el objeto Cells de origen,
- índice de columna de origen, y
- el índice de columna de destino.

**Código Python**

{{< highlight ruby >}}



def copy_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Put some data into header rows (A1:A4)

i = 0

while i < 5:

worksheet.getCells().get(i, 0).setValue("Header Row #i")





\# Put some detail data (A5:A999)

i = 5

while i < 1000:

worksheet.getCells().get(i, 0).setValue("Detail Row #i")


\# Create another Workbook.

workbook1 = Workbook()

\# Get the first worksheet in the book.

worksheet1 = workbook1.getWorksheets().get(0)

\# Copy the first column from the first worksheet of the first workbook into

\# the first worksheet of the second workbook.

worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

\# Autofit the column.

worksheet1.autoFitColumn(2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Columns.xls")

print "Copy Columns Successfully." 

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar Copiando Filas y Columnas (Aspose.Cells) desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
