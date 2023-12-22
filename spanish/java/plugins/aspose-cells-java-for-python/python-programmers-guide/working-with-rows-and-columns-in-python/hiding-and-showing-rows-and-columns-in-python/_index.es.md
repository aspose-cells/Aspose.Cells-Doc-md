---
title: Ocultar y mostrar filas y columnas en Python
type: docs
weight: 50
url: /es/java/hiding-and-showing-rows-and-columns-in-python/
description: Aprenda a ocultar y mostrar filas y columnas a través de Aspose.Cells for Python a través de Java API.
keywords: How to Hide and Show Rows and Columns in Python Via Java, Hide Rows and Columns using Python Via Java, Python Via Java Show Rows and Columns. 
---
##  **Aspose.Cells - Controlar la visibilidad de filas y columnas**
###  **Cómo ocultar filas y columnas**
Los desarrolladores pueden ocultar una fila o columna llamando a los métodos HideRow y HideColumn de la colección Cells respectivamente. Ambos métodos toman el índice de fila/columna como parámetro para ocultar la fila o columna específica.

**Código Rubí**

{{< highlight "ruby" >}}

 def hide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Hiding the 3rd row of the worksheet

cells.hideRow(2)

\# Hiding the 2nd column of the worksheet

cells.hideColumn(1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Hide Rows And Columns.xls")

print "Hide Rows And Columns Successfully." 

{{< /highlight >}}
###  **Cómo mostrar filas y columnas**
Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos UnhideRow y UnhideColumn de la colección Cells respectivamente. Ambos métodos toman dos parámetros:

- **Índice de columna Rowor**el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Alto de fila o ancho de columna**- la altura de la fila o el ancho de la columna asignado a la fila o columna después de que se muestra.

**Código Rubí**

{{< highlight "ruby" >}}

 def unhide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Unhiding the 3rd row and setting its height to 13.5

cells.unhideRow(2,13.5)

\# Unhiding the 2nd column and setting its width to 8.5

cells.unhideColumn(1,8.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Unhide Rows And Columns.xls")

print "Unhide Rows And Columns Successfully." 

{{< /highlight >}}
##  **Descargar código de ejecución**
 Descargar**Controlar la visibilidad de filas y columnas (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
