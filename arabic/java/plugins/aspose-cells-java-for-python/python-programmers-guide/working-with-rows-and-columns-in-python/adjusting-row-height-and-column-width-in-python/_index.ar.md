---
title: ضبط ارتفاع الصف وعرض العمود في Python
type: docs
weight: 10
url: /ar/java/adjusting-row-height-and-column-width-in-python/
keywords: "إنشاء XLSX في Python ، إنشاء XLS في Python ، XLS python ، XLSX python ، ارتفاع الصف python ، عرض العمود python ، Excel python"
description: استخدام واجهة برمجة التطبيقات لإكسل في Python لإنشاء ملفات Excel في Python. ضبط ارتفاع الصف وعرض العمود في XLSX أو XLS في تطبيقاتك Python دون MS Office.
---

## **جداول Excel في Python - ضبط ارتفاع الصف وعرض العمود**
### **ضبط ارتفاع الصف**
مع Aspose.Cells، يُمكن ضبط ارتفاع صف واحد في Python عن طريق استدعاء طريقة مجموعة Cells الـ setRowHeight. تأخذ طريقة setRowHeight المعلمات التالية:

- **مؤشر الصف**, مؤشر الصف الذي كنت تغير ارتفاعه.
- **ارتفاع الصف**, ارتفاع الصف المطبق على الصف.

**كود Python**

{{< highlight python >}}

 def set_row_height(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the height of the second row to 13

cells.setRowHeight(1, 13)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Row Height.xls")

print "Set Row Height Successfully." 

{{< /highlight >}}
### **ضبط عرض العمود**
قم بتعيين عرض عمود عن طريق استدعاء طريقة setColumnWidth لمجموعة Cells. تأخذ طريقة setColumnWidth  المعلمات التالية:

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.
- **عرض العمود**, العرض المطلوب للعمود.

**كود Python**

{{< highlight python >}}

 def set_column_width(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Column Width.xls")

print "Set Column Width Successfully." 

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **ضبط ارتفاع الصف وعرض العمود (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
