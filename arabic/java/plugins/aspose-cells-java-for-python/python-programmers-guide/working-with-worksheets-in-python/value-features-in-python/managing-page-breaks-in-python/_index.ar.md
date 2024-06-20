---
title: إدارة كسر الصفحة في Python
type: docs
weight: 20
url: /ar/java/managing-page-breaks-in-python/
---

## **Aspose.Cells - إدارة فواصل الصفحات**
### **إضافة فواصل الصفحات**
لإضافة فواصل الصفحات باستخدام **Aspose.Cells Java for Ruby**، اُنادي بطريقة **add_page_breaks** لوحدة **pagebreaks**. يمكنك أدناه رؤية مثال على الكود.

**كود Python**

{{< highlight python >}}

 def add_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.add("Y30")

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.add("Y30")

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Add Page Breaks.xls")

print "Add page breaks, please check the output file."


{{< /highlight >}}
### **مسح كافة فواصل الصفحات**
لمسح كل كسر الصفحة باستخدام **Aspose.Cells Java for Python**، اطلب من طريق استدعاء **clear_all_page_breaks** من وحدة **pagebreaks**. فيما يلي مثال على الكود.

**كود Python**

{{< highlight python >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **إزالة فاصل صفحة محدد**
لإزالة كسر الصفحة المحدد باستخدام **Aspose.Cells Java for Python**، اطلب من طريق استدعاء **remove_page_break** من وحدة **pagebreaks**. فيما يلي مثال على الكود.

**كود Python**

{{< highlight python >}}



def remove_page_break(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.removeAt(0)

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.removeAt(0)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Remove Page Break.xls")

print "Remove page break, please check the output file."


{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **إدارة كسر الصفحة (Aspose.Cells)** من أي من مواقع التعديل الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
