---
title: Ajustar la altura de la fila y el ancho de la columna en Python
type: docs
weight: 10
url: /es/java/adjusting-row-height-and-column-width-in-python/
keywords: "crear XLSX en Python, crear XLS en Python, XLS python, XLSX python, altura de fila python, ancho de columna python, Excel python"
description: Utilice Python Excel API para crear archivos de Excel en Python. Ajuste la altura de fila y el ancho de columna en XLSX o XLS en sus aplicaciones Python sin MS Office.
---

## **Hojas de cálculo de Excel en Python - Ajustar la altura de la fila y el ancho de la columna**
### **Establecer la altura de la fila**
Con Aspose.Cells, es posible establecer la altura de una sola fila en Python llamando al método setRowHeight de la colección Cells. El método setRowHeight toma los siguientes parámetros:

- **Índice de fila**, el índice de la fila a la que le estás cambiando la altura.
- **Altura de fila**, la altura de fila para aplicar en la fila.

**Código Python**

{{< highlight python >}}

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
### **Configurar ancho de columna**
Establezca el ancho de una columna llamando al método setColumnWidth de la colección Cells. El método setColumnWidth toma los siguientes parámetros:

- **Índice de la columna**, el índice de la columna cuyo ancho se va a cambiar.
- **Ancho de la columna**, el ancho de columna deseado.

**Código Python**

{{< highlight python >}}

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
## **Descargar Código en Ejecución**
Descargar **Ajuste de altura de fila y ancho de columna (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
