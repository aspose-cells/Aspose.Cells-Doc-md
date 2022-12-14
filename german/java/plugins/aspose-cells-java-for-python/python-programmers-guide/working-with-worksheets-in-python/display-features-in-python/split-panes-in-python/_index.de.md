---
title: Geteilte Scheiben in Python
type: docs
weight: 70
url: /de/java/split-panes-in-python/
---
## **Aspose.Cells - Geteilte Scheiben**
 So teilen Sie Fenster mit**Aspose.Cells Java für Python** , einfach aufrufen**SplitPanes** Modul.

**Python Code**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20");

# Split the worksheet window

workbook.getWorksheets().get(0).split();

# Save the excel file

workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

# Print Message

print "Panes split successfully."

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Geteilte Scheiben (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
