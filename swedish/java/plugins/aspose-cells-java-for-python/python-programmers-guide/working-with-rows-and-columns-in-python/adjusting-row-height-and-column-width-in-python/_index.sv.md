---
title: Justering av radhöjd och kolumnbredd i Python
type: docs
weight: 10
url: /sv/java/adjusting-row-height-and-column-width-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, row height python, column width python, Excel pytho
description: Använd Python Excel API för att skapa Excel-filer i Python. Justera radhöjd och kolumnbredd i XLSX eller XLS i dina Python-program utan MS Office.
---
## **Excel-kalkylblad i Python - Justering av radhöjd och kolumnbredd**
### **Ställa in radhöjden**
Med Aspose.Cells är det möjligt att ställa in höjden på en enstaka rad i Python genom att anropa Cells-samlingens setRowHeight-metod. Metoden setRowHeight tar följande parametrar:

- **Radindex**, indexet för raden som du ändrar höjden på.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

**Python Kod**

{{< highlight "python" >}}

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
### **Ställa in kolumnbredden**
Ställ in bredden på en kolumn genom att anropa Cells-samlingens setColumnWidth-metod. Metoden setColumnWidth tar följande parametrar:

- **Kolumnindex**, indexet för kolumnen som du ändrar bredden på.
- **Kolumnbredd**, önskad kolumnbredd.

**Python Kod**

{{< highlight "python" >}}

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
## **Ladda ner Running Code**
Ladda ner**Justera radhöjd och kolumnbredd (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
