---
title: Mostrar u ocultar pestañas en Python
type: docs
weight: 30
url: /es/java/display-or-hide-tabs-in-python/
---
## **Aspose.Cells - Mostrar ocultar pestañas**
### **Ocultar pestañas**
 Para ocultar pestañas usando**Aspose.Cells Java para rubí** , llamar**Mostrar ocultar pestañas** módulo.

**Código Python**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Hacer pestañas visibles**
Haga que las pestañas sean visibles con el método setSheetTabBarHidden(false) de la clase Workbook.

**Código Python**

{{< highlight "python" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Hello World (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
