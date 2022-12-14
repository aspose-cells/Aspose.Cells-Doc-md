---
title: تجميد الأجزاء في Python
type: docs
weight: 40
url: /ar/java/freeze-panes-in-python/
---
## **Aspose.Cells - تجميد الأجزاء**
 لتجميد الأجزاء في مستند جدول البيانات باستخدام**Aspose.Cells Java لـ Python** ، ببساطة استدعاء**أجزاء التجميد** وحدة.

**Python كود**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

# Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**Hello World (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
