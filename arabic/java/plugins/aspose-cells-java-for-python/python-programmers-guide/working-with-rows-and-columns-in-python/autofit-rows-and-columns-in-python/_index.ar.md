---
title: الصفوف والأعمدة التلقائية في Python
type: docs
weight: 20
url: /ar/java/autofit-rows-and-columns-in-python/
description: تعرف على كيفية الاحتواء التلقائي للصفوف والأعمدة من خلال Aspose.Cells for Python عبر Java API.
keywords: How to Autofit Rows and Columns in Python Via Java, Autofit Rows Data in workbook using Python Via Java, Python Via Java Autofit Columns Data. 
---
##  **كيفية الاحتواء التلقائي للصفوف والأعمدة**
###  **كيفية الاحتواء التلقائي للصف**
الطريقة الأكثر مباشرة للتحجيم التلقائي لعرض الصف وارتفاعه هي استدعاء أسلوب autoFitRow الخاص بفئة ورقة العمل. تأخذ الطريقة autoFitRow فهرس الصف (الصف الذي سيتم تغيير حجمه) كمعلمة.

**Python كود**

{{< highlight "python" >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

# worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
###  **كيفية الاحتواء التلقائي للعمود**
أسهل طريقة لتحديد حجم عرض العمود وارتفاعه تلقائيًا هي استدعاء أسلوب autoFitColumn الخاص بفئة ورقة العمل. تأخذ الطريقة autoFitColumn فهرس العمود (العمود الذي على وشك تغيير حجمه) كمعلمة.

**Python كود**

{{< highlight "python" >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

# worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
##  **تحميل كود التشغيل**
تحميل**الاحتواء التلقائي للصفوف والأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
