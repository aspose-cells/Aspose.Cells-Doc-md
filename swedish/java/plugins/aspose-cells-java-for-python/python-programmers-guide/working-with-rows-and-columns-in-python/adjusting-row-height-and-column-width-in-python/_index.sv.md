---
title: Justera radhöjd och kolumnbredd i Python
type: docs
weight: 10
url: /sv/java/adjusting-row-height-and-column-width-in-python/
keywords: "skapa XLSX i Python, skapa XLS i Python, XLS python, XLSX python, radhöjd python, kolumnbredd python, Excel python"
description: Använd Python Excel API för att skapa Excelfiler i Python. Justera radhöjd och kolumnbredd i XLSX eller XLS i dina Python applikationer utan MS Office.
---

## **Excelfil i Python - Justera radhöjd och kolumnbredd**
### **Ange radhöjden**
Med Aspose.Cells är det möjligt att ange höjden på en enskild rad i Python genom att anropa Cells-samlingen setRowHeight -metoden. setRowHeight-metoden tar följande parametrar:

- **Radindex**, index för den rad vars höjd du ändrar.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

**Python-kod**

{{< highlight python >}}

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
### **Ange kolumnbredden**
Ange bredden på en kolumn genom att anropa samlingen 'cells' 'setColumnWidth' -metoden.

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.
- **Kolumnbredd**, önskad kolumnbredd.

**Python-kod**

{{< highlight python >}}

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
## **Ladda ned körbar kod**
Ladda ner **Justera radhöjd och kolumnbredd (Aspose.Cells)** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
