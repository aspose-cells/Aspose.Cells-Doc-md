---
title: Visa eller dölj rutnät i Python
type: docs
weight: 10
url: /sv/java/display-or-hide-gridlines-in-python/
description: Lär dig hur du visar eller döljer rutnät genom Aspose.Cells for Python via Java API.
keywords: Hur man visar eller döljer rutnät i Python via Java, Visa eller dölj rutnät med Python via Java, Python Visa eller dölj rutnät. 
---

## **Aspose.Cells - Hur man visar eller döljer rutnät**
### **Hur man döljer rutnät**
För att dölja kalkylblad med **Aspose.Cells Java för Ruby**, anropa **displayhidegridlines** modulen.

**Python-kod**

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
### **Hur man visar rutnät**
För att göra rutnätet synligt, använd klassen Worksheet metod setGridlinesVisible(true).

**Python-kod**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **DisplayHideGridlines (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
