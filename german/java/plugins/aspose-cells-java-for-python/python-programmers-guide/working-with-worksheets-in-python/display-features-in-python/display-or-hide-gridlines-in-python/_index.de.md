---
title: Anzeigen oder Ausblenden von Gitterlinien in Python
type: docs
weight: 10
url: /de/java/display-or-hide-gridlines-in-python/
description: Lernen Sie, wie Sie Gitterlinien über das Aspose.Cells for Python Via Java API anzeigen oder ausblenden.
keywords: Wie man Gitterlinien in Python Via Java anzeigen oder ausblenden, Gitterlinien in Python Via Java anzeigen oder ausblenden, Python anzeigen oder ausblenden von Gitterlinien. 
---

## **Aspose.Cells - Wie man Gitterlinien anzeigt oder ausblendet**
### **Wie man Gitterlinien ausblendet**
Um ein Arbeitsblatt mit **Aspose.Cells Java für Ruby** auszublenden, rufen Sie das Modul **displayhidegridlines** auf.

**Python-Code**

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
### **Wie man Gitterlinien anzeigt**
Um Gitterlinien sichtbar zu machen, verwenden Sie die Methode setGridlinesVisible(true) der Klasse Worksheet.

**Python-Code**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **DisplayHideGridlines (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
