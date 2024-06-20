---
title: Разделение областей в Python
type: docs
weight: 70
url: /ru/java/split-panes-in-python/
---

## **Aspose.Cells - Разделить панели**
Для разделения областей с использованием **Aspose.Cells Java для Python** просто вызовите модуль **SplitPanes**.

**Код Python**

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
## **Скачать работающий код**
Загрузите **Split Panes (Aspose.Cells)** с любого из упомянутых ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
