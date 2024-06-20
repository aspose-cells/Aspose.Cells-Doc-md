---
title: يتماشى الصفوف والأعمدة تلقائيًا في Python
type: docs
weight: 20
url: /ar/java/autofit-rows-and-columns-in-python/
description: تعلم كيفية ضبط ارتفاع الصفوف وعرض الأعمدة من خلال Aspose.Cells لـ Python عبر واجهة برمجة التطبيقات Java.
keywords: كيفية ضبط ارتفاع الصفوف وعرض الأعمدة في Python عبر Java، ضبط البيانات لصفوف الارتفاع التلقائي في Python عبر Java، Python عبر Java ضبط بيانات الأعمدة لارتفاع التلقائي. 
---

## **كيفية ضبط ارتفاع الصفوف وعرض الأعمدة تلقائيًا**
### **كيفية ضبط ارتفاع الصف تلقائيًا**
أبسط نهج لتغيير حجم العرض والارتفاع للصف هو استدعاء طريقة autoFitRow من فئة Worksheet. تأخذ طريقة autoFitRow مؤشر الصف (الذي سيتم تغيير حجمه) كمعلمة.

**كود Python**

{{< highlight python >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

#worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
### **كيفية تعديل حجم العمود تلقائيًا**
أسهل طريقة لتغيير حجم العرض والارتفاع للعمود هي استدعاء طريقة autoFitColumn من فئة Worksheet. تأخذ طريقة autoFitColumn الفهرس العمود (الذي سيتم تغيير حجمه) كمعلمة.

**كود Python**

{{< highlight python >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

#worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل ** تكبير الصفوف والأعمدة (Aspose.Cells) ** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
