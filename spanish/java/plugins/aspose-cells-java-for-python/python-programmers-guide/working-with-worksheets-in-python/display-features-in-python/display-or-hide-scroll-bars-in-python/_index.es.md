---
title: Mostrar u ocultar barras de desplazamiento en Python
type: docs
weight: 20
url: /es/java/display-or-hide-scroll-bars-in-python/
---
## **Aspose.Cells - Mostrar u ocultar barras de desplazamiento**
### **Ocultar encabezados de fila/columna**
Para ocultar encabezados de fila/columna usando**Aspose.Cells Java for Python** , llamar**MostrarOcultarFilaColumnaEncabezados** módulo.

**Código Python**

{{< highlight "python" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **Hacer visibles los encabezados de fila/columna**
Haga que los encabezados de fila y columna sean visibles mediante el método setRowColumnHeadersVisible(true) de la clase Worksheet.

**Código Python**

{{< highlight "python" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Hello World (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
