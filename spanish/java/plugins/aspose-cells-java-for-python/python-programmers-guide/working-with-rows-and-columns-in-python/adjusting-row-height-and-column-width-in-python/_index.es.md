---
title: Ajuste de altura de fila y ancho de columna en Python
type: docs
weight: 10
url: /es/java/adjusting-row-height-and-column-width-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, row height python, column width python, Excel pytho
description: Use Python Excel API para crear archivos de Excel en Python. Ajuste la altura de fila y el ancho de columna en XLSX o XLS en sus aplicaciones Python sin MS Office.
---
## **Hojas de cálculo de Excel en Python - Ajuste de altura de fila y ancho de columna**
### **Configuración de la altura de la fila**
Con Aspose.Cells, es posible establecer la altura de una sola fila en Python llamando al método setRowHeight de la colección Cells. El método setRowHeight toma los siguientes parámetros:

- **Índice de fila**, el índice de la fila cuya altura está cambiando.
- **Altura de la fila**, el alto de fila que se aplicará en la fila.

**Código Python**

{{< highlight "python" >}}

 def set_row_height(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the height of the second row to 13

cells.setRowHeight(1, 13)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Row Height.xls")

print "Set Row Height Successfully." 

{{< /highlight >}}
### **Configuración del ancho de columna**
Establezca el ancho de una columna llamando al método setColumnWidth de la colección Cells. El método setColumnWidth toma los siguientes parámetros:

- **índice de columna**, el índice de la columna cuyo ancho está cambiando.
- **Ancho de columna**, el ancho de columna deseado.

**Código Python**

{{< highlight "python" >}}

 def set_column_width(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Column Width.xls")

print "Set Column Width Successfully." 

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Ajuste de altura de fila y ancho de columna (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
