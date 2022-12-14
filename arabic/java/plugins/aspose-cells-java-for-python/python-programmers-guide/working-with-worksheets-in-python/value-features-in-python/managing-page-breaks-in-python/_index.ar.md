---
title: إدارة فواصل الصفحات في Python
type: docs
weight: 20
url: /ar/java/managing-page-breaks-in-python/
---
## **Aspose.Cells - إدارة فواصل الصفحات**
### **مضيفا فواصل الصفحات**
 لإضافة فواصل الصفحات باستخدام**Aspose.Cells Java لروبي** ، مكالمة**add_page_breaks** طريقة**فواصل الصفحة** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**Python كود**

{{< highlight "python" >}}

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
 لمسح كافة فواصل الصفحات باستخدام**Aspose.Cells Java لـ Python** ، مكالمة**clear_all_page_breaks** طريقة**فواصل الصفحة** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**Python كود**

{{< highlight "python" >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **إزالة فاصل صفحة معين**
 لإزالة فاصل صفحة معين باستخدام**Aspose.Cells Java لـ Python** ، مكالمة**remove_page_break** طريقة**فواصل الصفحة** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**Python كود**

{{< highlight "python" >}}



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
## **قم بتنزيل كود التشغيل**
 تحميل**إدارة فواصل الصفحات (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
