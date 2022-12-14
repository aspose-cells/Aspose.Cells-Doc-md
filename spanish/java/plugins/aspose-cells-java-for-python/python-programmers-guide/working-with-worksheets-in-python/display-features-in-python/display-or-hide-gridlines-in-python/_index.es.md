---
title: Mostrar u ocultar líneas de cuadrícula en Python
type: docs
weight: 10
url: /es/java/display-or-hide-gridlines-in-python/
---
## **Aspose.Cells - Mostrar Ocultar líneas de cuadrícula**
### **Ocultar líneas de cuadrícula**
 Para ocultar la hoja de trabajo usando**Aspose.Cells Java para rubí** , llamar**mostrar ocultar líneas de cuadrícula** módulo.

**Código Python**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **Hacer visibles las líneas de cuadrícula**
Para hacer visibles las líneas de cuadrícula, utilice el método setGridlinesVisible(true) de la clase Worksheet.

**Código Python**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Mostrar Ocultar líneas de cuadrícula (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
