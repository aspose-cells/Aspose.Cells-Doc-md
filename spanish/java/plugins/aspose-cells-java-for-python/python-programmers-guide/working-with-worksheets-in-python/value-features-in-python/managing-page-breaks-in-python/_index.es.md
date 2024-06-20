---
title: Gestionar Saltos de Página en Python
type: docs
weight: 20
url: /es/java/managing-page-breaks-in-python/
---

## **Aspose.Cells - Gestionar Saltos de Página**
### **Añadir Saltos de Página**
Para añadir saltos de página usando **Aspose.Cells Java para Ruby**, llame al método **add_page_breaks** del módulo **pagebreaks**. A continuación, puede ver un ejemplo de código.

**Código Python**

{{< highlight python >}}

 def add_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.add("Y30")

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.add("Y30")

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Add Page Breaks.xls")

print "Add page breaks, please check the output file."


{{< /highlight >}}
### **Borrar Todos los Saltos de Página**
Para borrar todos los saltos de página usando **Aspose.Cells Java para Python**, llame al método **clear_all_page_breaks** del módulo **pagebreaks**. A continuación, puede ver un ejemplo de código.

**Código Python**

{{< highlight python >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **Eliminar Salto de Página Específico**
Para eliminar un salto de página específico usando **Aspose.Cells Java para Python**, llame al método **remove_page_break** del módulo **pagebreaks**. A continuación, puede ver un ejemplo de código.

**Código Python**

{{< highlight python >}}



def remove_page_break(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.removeAt(0)

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.removeAt(0)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Remove Page Break.xls")

print "Remove page break, please check the output file."


{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Gestionando saltos de página (Aspose.Cells)** desde cualquiera de los siguientes sitios de codificación social:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
