---
title: Mostra o Nascondi le schede in Python
type: docs
weight: 30
url: /it/java/display-or-hide-tabs-in-python/
---

## **Aspose.Cells - Mostra/Nascondi schede**
### **Nascondere le schede**
Per nascondere le schede usando **Aspose.Cells Java per Ruby**, chiama il modulo **displayhidetabs**.

**Codice Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Rendere visibili le schede con il metodo {1} della classe {0}.**
Rendi le schede visibili con il metodo setSheetTabBarHidden(false) della classe Workbook.

**Codice Python**

{{< highlight python >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Hello World (Aspose.Cells)** da uno dei siti di codifica sociali menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
