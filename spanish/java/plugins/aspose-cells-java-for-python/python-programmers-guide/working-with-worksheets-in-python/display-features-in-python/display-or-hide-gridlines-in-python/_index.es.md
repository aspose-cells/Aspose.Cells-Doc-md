---
title: Mostrar u ocultar líneas de división en Python
type: docs
weight: 10
url: /es/java/display-or-hide-gridlines-in-python/
description: Aprenda a mostrar u ocultar líneas de cuadrícula a través de Aspose.Cells for Python a través de Java API.
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines. 
---
##  **Aspose.Cells - Cómo mostrar u ocultar líneas de división**
###  **Cómo ocultar líneas de división**
 Para ocultar la hoja de trabajo usando**Aspose.Cells Java para Ruby**, llame a **displayhidegridlines** módulo.

**Python Código**

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
###  **Cómo mostrar líneas de cuadrícula**
Para hacer visibles las líneas de cuadrícula, utilice el método setGridlinesVisible(true) de la clase Worksheet.

**Python Código**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
##  **Descargar código de ejecución**
 Descargar**Mostrar líneas de cuadrícula ocultas (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
