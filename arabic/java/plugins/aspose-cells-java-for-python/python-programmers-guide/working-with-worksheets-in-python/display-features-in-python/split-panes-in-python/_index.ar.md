---
title: تقسيم الألواح في Python
type: docs
weight: 70
url: /ar/java/split-panes-in-python/
---

## **Aspose.Cells - تقسيم الألواح**
لتقسيم النوافذ باستخدام **Aspose.Cells Java for Python**, قم ببساطة باستدعاء وحدة **SplitPanes**.

**كود Python**

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
## **تحميل رمز التشغيل**
تنزيل **تقسيم النوافذ (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
