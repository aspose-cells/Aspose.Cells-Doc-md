---
title: Dividere i riquadri in Python
type: docs
weight: 70
url: /it/java/split-panes-in-python/
---

## **Aspose.Cells - Dividi riquadri**
Per dividere i riquadri utilizzando **Aspose.Cells Java per Python**, semplicemente invoca il modulo **SplitPanes**.

**Codice Python**

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
## **Scarica il codice in esecuzione**
Scarica **Dividi riquadri (Aspose.Cells)** da uno dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
