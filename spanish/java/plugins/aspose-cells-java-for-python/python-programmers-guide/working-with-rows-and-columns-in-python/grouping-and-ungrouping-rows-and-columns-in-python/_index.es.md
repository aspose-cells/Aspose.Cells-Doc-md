---
title: Agrupar y Desagrupar Filas y Columnas en Python
type: docs
weight: 40
url: /es/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Aprenda cómo agrupar y desagrupar filas y columnas a través de Aspose.Cells para Python Via Java API.
keywords: Cómo Agrupar y Desagrupar Filas y Columnas en Python Via Java, Agrupar Filas y Columnas usando Python Via Java, Desagrupar Filas y Columnas en Python Via Java. 
---

## **Gestión de Agrupación y Desagrupación de Filas y Columnas en Aspose.Cells for Python via Java**
### **Cómo Agrupar Filas y Columnas en Python**
Es posible agrupar filas o columnas llamando a los métodos groupRows y groupColumns de la colección Cells. Ambos métodos toman los siguientes parámetros:

- Índice de la primera fila/columna, la primera fila o columna del grupo.
- Índice de la última fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si ocultar o no filas/columnas después de agrupar.

**Código Python**

{{< highlight python >}}

 def group_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Grouping first six rows (from 0 to 5) and making them hidden by passing true

cells.groupRows(0,5,True)

\# Grouping first three columns (from 0 to 2) and making them hidden by passing true

cells.groupColumns(0,2,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Group Rows And Columns.xls")

print "Group Rows And Columns Successfully." 

{{< /highlight >}}
### **Cómo Desagrupar Filas y Columnas usando Python**
Desagrupar filas o columnas agrupadas llamando a los métodos UngroupRows y UngroupColumns de la colección Cells. Ambos métodos toman los mismos parámetros:

- Índice de la primera fila o columna, la primera fila/columna a desagrupar.
- Índice de la última fila o columna, la última fila/columna a desagrupar.

**Código Python**

{{< highlight python >}}

 def ungroup_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Group Rows And Columns.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Ungrouping first six rows (from 0 to 5)

cells.ungroupRows(0,5)

\# Ungrouping first three columns (from 0 to 2)

cells.ungroupColumns(0,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Ungroup Rows And Columns.xls")

print "Ungroup Rows And Columns Successfully." 

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Agrupar y Desagrupar Filas y Columnas (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
