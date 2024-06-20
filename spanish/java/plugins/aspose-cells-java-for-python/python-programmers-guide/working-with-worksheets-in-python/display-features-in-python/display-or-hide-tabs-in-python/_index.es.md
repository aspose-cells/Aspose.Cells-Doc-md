---
title: Mostrar u ocultar pestañas en Python
type: docs
weight: 30
url: /es/java/display-or-hide-tabs-in-python/
---

## **Aspose.Cells - Mostrar u ocultar pestañas**
### **Ocultar pestañas**
Para ocultar pestañas usando **Aspose.Cells Java para Ruby**, llama al módulo **displayhidetabs**.

**Código Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Hacer pestañas visibles**
Haz visibles las pestañas con el método setSheetTabBarHidden(false) de la clase Workbook.

**Código Python**

{{< highlight python >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Hola Mundo (Aspose.Cells)** desde cualquiera de los siguientes sitios de codificación social mencionados:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
