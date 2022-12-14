---
title: Visa eller dölj rutnät i Python
type: docs
weight: 10
url: /sv/java/display-or-hide-gridlines-in-python/
---
## **Aspose.Cells - Visa Dölj rutnät**
### **Dölja rutnät**
 För att dölja kalkylblad med**Aspose.Cells Java för Ruby** , ringa upp**visahidegridlines** modul.

**Python-kod**

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
### **Gör rutnät synliga**
För att göra rutnätslinjer synliga, använd arbetsbladsklassens setGridlinesVisible(true) metod.

**Python-kod**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**DisplayHide Gridlines (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
