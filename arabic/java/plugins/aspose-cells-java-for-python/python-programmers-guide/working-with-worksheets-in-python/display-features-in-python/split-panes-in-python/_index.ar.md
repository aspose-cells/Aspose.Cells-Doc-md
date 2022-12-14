---
title: تقسيم الأجزاء في Python
type: docs
weight: 70
url: /ar/java/split-panes-in-python/
---
## **Aspose.Cells - تقسيم الأجزاء**
 لتقسيم الأجزاء باستخدام**Aspose.Cells Java لـ Python** ، ببساطة استدعاء**SplitPanes** وحدة.

**Python كود**

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
## **قم بتنزيل كود التشغيل**
 تحميل**تقسيم الأجزاء (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
