---
title: Mostrar u Ocultar Rejillas en Python
type: docs
weight: 10
url: /es/java/display-or-hide-gridlines-in-python/
description: Aprenda a Mostrar u Ocultar Rejillas a través de la API de Aspose.Cells para Python Via Java.
keywords: Cómo Mostrar u Ocultar Rejillas en Python Via Java, Mostrar u Ocultar Rejillas usando Python Via Java, Mostrar u Ocultar Rejillas en Python. 
---

## **Aspose.Cells - Cómo Mostrar u Ocultar Rejillas**
### **Cómo Ocultar Rejillas**
Para ocultar una hoja de cálculo usando **Aspose.Cells Java para Ruby**, llama al módulo **displayhidegridlines**.

**Código Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

#Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **Cómo Mostrar Rejillas**
Para hacer visibles las líneas de cuadrícula, utiliza el método **setGridlinesVisible(true)** de la clase Worksheet.

**Código Python**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargue **DisplayHideGridlines (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
