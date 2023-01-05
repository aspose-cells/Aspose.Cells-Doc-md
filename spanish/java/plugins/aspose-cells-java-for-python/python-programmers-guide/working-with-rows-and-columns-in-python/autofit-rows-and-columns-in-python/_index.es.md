---
title: Autoajustar filas y columnas en Python
type: docs
weight: 20
url: /es/java/autofit-rows-and-columns-in-python/
---
## **Aspose.Cells - Autoajustar filas y columnas**
### **Autoajustar fila**
El enfoque más sencillo para cambiar automáticamente el tamaño del ancho y el alto de una fila es llamar al método autoFitRow de la clase Worksheet. El método autoFitRow toma un índice de fila (de la fila a redimensionar) como parámetro.

**Código Python**

{{< highlight "python" >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

# worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
### **Columna de ajuste automático**
La forma más fácil de cambiar automáticamente el tamaño del ancho y el alto de una columna es llamar al método autoFitColumn de la clase Worksheet. El método autoFitColumn toma el índice de la columna (de la columna que se va a cambiar de tamaño) como parámetro.

**Código Python**

{{< highlight "python" >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

# worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Autoajustar filas y columnas (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
