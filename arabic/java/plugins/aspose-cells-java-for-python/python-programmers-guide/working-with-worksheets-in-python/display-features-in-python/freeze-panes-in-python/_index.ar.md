---
title: تجميد الألواح في Python
type: docs
weight: 40
url: /ar/java/freeze-panes-in-python/
---

## **Aspose.Cells - تجميد الألواح**
لتجميد الألواح في مستند الجدول الزمني باستخدام **Aspose.Cells Java for Python**, قم ببساطة باستدعاء وحدة **FreezePanes**.

**كود Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

#Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **مرحبًا بالعالم (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
