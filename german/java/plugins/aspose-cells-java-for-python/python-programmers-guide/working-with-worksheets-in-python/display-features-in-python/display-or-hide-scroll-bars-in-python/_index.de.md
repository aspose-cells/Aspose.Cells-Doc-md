---
title: Bildlaufleisten in Python anzeigen oder ausblenden
type: docs
weight: 20
url: /de/java/display-or-hide-scroll-bars-in-python/
---
## **Aspose.Cells – Bildlaufleisten anzeigen oder ausblenden**
### **Zeilen-/Spaltenüberschriften ausblenden**
 Zeilen-/Spaltenüberschriften ausblenden mit**Aspose.Cells Java for Python** , Anruf**DisplayHideRowColumnHeader** Modul.

**Python Code**

{{< highlight "python" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **Zeilen-/Spaltenüberschriften sichtbar machen**
Machen Sie Zeilen- und Spaltenüberschriften sichtbar, indem Sie die setRowColumnHeadersVisible(true)-Methode der Worksheet-Klasse verwenden.

**Python Code**

{{< highlight "python" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Hello World (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
