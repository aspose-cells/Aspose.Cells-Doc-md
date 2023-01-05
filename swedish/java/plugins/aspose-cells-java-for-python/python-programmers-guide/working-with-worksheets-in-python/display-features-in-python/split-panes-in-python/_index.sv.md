---
title: Delade rutor i Python
type: docs
weight: 70
url: /sv/java/split-panes-in-python/
---
## **Aspose.Cells - Delade rutor**
 För att dela fönster med**Aspose.Cells Java for Python** , helt enkelt åberopa**SplitPanes** modul.

**Python Kod**

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
## **Ladda ner Running Code**
 Ladda ner**Delade rutor (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
