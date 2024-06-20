---
title: Anzeigen oder Ausblenden von Scrollleisten in Python
type: docs
weight: 20
url: /de/java/display-or-hide-scroll-bars-in-python/
---

## **Aspose.Cells - Scrollleisten anzeigen oder ausblenden**
### **Zeilen-/Spaltenheader ausblenden**
Um Zeilen-/Spaltenheader mit **Aspose.Cells Java für Python** auszublenden, rufen Sie das Modul **DisplayHideRowColumnHeaders** auf.

**Python-Code**

{{< highlight python >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

#Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **Anzeigen von Zeilen-/Spaltenüberschriften**
Zeigen Sie Zeilen- und Spaltenüberschriften an, indem Sie die Methode setRowColumnHeadersVisible(true) der Klasse Arbeitsblatt verwenden.

**Python-Code**

{{< highlight python >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Hello World (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
