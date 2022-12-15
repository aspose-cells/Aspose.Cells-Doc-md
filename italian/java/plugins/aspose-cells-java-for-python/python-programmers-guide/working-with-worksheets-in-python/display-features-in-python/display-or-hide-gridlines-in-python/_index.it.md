---
title: Mostra o nascondi le linee della griglia in Python
type: docs
weight: 10
url: /it/java/display-or-hide-gridlines-in-python/
---
## **Aspose.Cells - Visualizza Nascondi griglia**
### **Nascondere le linee della griglia**
 Per nascondere il foglio di lavoro utilizzando**Aspose.Cells Java per Ruby** , chiamata**displayhidegridlines** modulo.

**Codice Pitone**

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
### **Rendere visibili le linee della griglia**
Per rendere visibili le linee della griglia, utilizzare il metodo setGridlinesVisible(true) della classe Worksheet.

**Codice Pitone**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scarica**VisualizzaNascondiLinee griglia (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
