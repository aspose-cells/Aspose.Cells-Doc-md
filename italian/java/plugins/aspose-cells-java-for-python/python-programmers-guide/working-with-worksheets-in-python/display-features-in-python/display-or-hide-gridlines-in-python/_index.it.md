---
title: Mostra o Nascondi Celle di Griglia in Python
type: docs
weight: 10
url: /it/java/display-or-hide-gridlines-in-python/
description: Scopri come Mostrare o Nascondere le Celle di Griglia tramite Aspose.Cells per Python tramite API Java.
keywords: Come Mostrare o Nascondere le Celle di Griglia in Python tramite Java, Mostra o Nascondi le Celle di Griglia usando Python tramite Java, Python Mostra o Nascondi le Celle di Griglia. 
---

## **Aspose.Cells - Come Mostrare o Nascondere le Celle di Griglia**
### **Come Nascondere le Celle di Griglia**
Per nascondere il foglio di lavoro usando **Aspose.Cells Java per Ruby**, chiamare il modulo **displayhidegridlines**.

**Codice Python**

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
### **Come Mostrare le Celle di Griglia**
Per rendere visibili le linee della griglia, utilizzare il metodo `setGridlinesVisible(true)` della classe `Worksheet`.

**Codice Python**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Mostra Nascondi Celle di Griglia (Aspose.Cells)** da uno qualsiasi dei siti di coding social qui sotto menzionati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
