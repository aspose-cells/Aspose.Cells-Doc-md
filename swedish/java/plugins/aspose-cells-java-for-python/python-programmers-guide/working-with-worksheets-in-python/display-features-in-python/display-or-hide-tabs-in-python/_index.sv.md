---
title: Visa eller dölj flikar i Python
type: docs
weight: 30
url: /sv/java/display-or-hide-tabs-in-python/
---
## **Aspose.Cells - Visa göm flikar**
### **Döljer flikar**
 För att dölja flikar med**Aspose.Cells Java för Ruby** , ringa upp**visagömflikar** modul.

**Python-kod**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Göra flikar synliga**
Gör flikar synliga med arbetsboksklassens setSheetTabBarHidden(false) metod.

**Python-kod**

{{< highlight "python" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Hello World (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
