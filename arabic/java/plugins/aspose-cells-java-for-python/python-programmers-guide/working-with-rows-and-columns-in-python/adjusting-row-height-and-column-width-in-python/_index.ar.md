---
title: ضبط ارتفاع الصف وعرض العمود في Python
type: docs
weight: 10
url: /ar/java/adjusting-row-height-and-column-width-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, row height python, column width python, Excel pytho
description: استخدم Python Excel API لإنشاء ملفات Excel في Python. اضبط ارتفاع الصف وعرض العمود في XLSX أو XLS في تطبيقاتك Python بدون MS Office.
---
## **جداول بيانات Excel في Python - ضبط ارتفاع الصف وعرض العمود**
### **ضبط ارتفاع الصف**
مع Aspose.Cells ، يمكن ضبط ارتفاع صف واحد في Python باستدعاء طريقة setRowHeight لمجموعة Cells. تأخذ طريقة setRowHeight المعلمات التالية:

- **فهرس الصف**، فهرس الصف الذي تقوم بتغيير ارتفاعه.
- **ارتفاع الصف**، ارتفاع الصف المراد تطبيقه على الصف.

**Python كود**

{{< highlight "python" >}}

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
قم بتعيين عرض العمود عن طريق استدعاء طريقة setColumnWidth للمجموعة Cells. تأخذ طريقة setColumnWidth المعلمات التالية:

- **فهرس العمود**، هو فهرس العمود الذي تقوم بتغيير عرضه.
- **عرض العمود**، عرض العمود المطلوب.

**Python كود**

{{< highlight "python" >}}

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
## **قم بتنزيل كود التشغيل**
تحميل**ضبط ارتفاع الصف وعرض العمود (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
