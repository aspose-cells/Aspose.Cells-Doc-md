---
title: Panes in Python aufteilen
type: docs
weight: 70
url: /de/java/split-panes-in-python/
---

## **Aspose.Cells - Panes aufteilen**
Um Panes unter Verwendung von **Aspose.Cells Java für Python** aufzuteilen, rufen Sie einfach das Modul **SplitPanes** auf.

**Python-Code**

{{< highlight java >}}

 saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20");

#Split the worksheet window

workbook.getWorksheets().get(0).split();

#Save the excel file

workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

#Print Message

print "Panes split successfully."

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Panes aufteilen (Aspose.Cells)** von einer der unten genannten Coding-Plattformen herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
