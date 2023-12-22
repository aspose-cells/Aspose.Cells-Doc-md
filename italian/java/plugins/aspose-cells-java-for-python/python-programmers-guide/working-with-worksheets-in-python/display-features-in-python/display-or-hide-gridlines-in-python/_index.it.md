---
title: Visualizza o nascondi la griglia in Python
type: docs
weight: 10
url: /it/java/display-or-hide-gridlines-in-python/
description: Scopri come visualizzare o nascondere le griglie tramite Aspose.Cells for Python tramite Java API.
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines. 
---
##  **Aspose.Cells - Come visualizzare o nascondere le griglie**
###  **Come nascondere le griglie**
 Per nascondere il foglio di lavoro utilizzando**Aspose.Cells Java per Ruby**, chiama **displayhidegridlines** modulo.

**Python Cod**

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
###  **Come visualizzare le griglie**
Per rendere visibili le linee della griglia, utilizzare il metodo setGridlinesVisible(true) della classe Worksheet.

**Python Cod**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
##  **Scarica il codice in esecuzione**
 Scaricamento**VisualizzaNascondiGriglia (Aspose.Cells)** da uno qualsiasi dei siti di social coding indicati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
