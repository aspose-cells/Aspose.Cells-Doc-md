---
title: احتواء تلقائي للصفوف والأعمدة في Python
type: docs
weight: 20
url: /ar/java/autofit-rows-and-columns-in-python/
---
## **Aspose.Cells - احتواء تلقائي للصفوف والأعمدة**
### **صف احتواء تلقائي**
الطريقة الأكثر مباشرة لتغيير حجم عرض الصف وارتفاعه تلقائيًا هي استدعاء طريقة autoFitRow لفئة ورقة العمل. تأخذ طريقة autoFitRow فهرس صف (للصف المراد تغيير حجمه) كمعامل.

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
### **عمود الاحتواء التلقائي**
أسهل طريقة لتغيير حجم عرض العمود وارتفاعه تلقائيًا هي استدعاء طريقة autoFitColumn لفئة ورقة العمل. تأخذ طريقة autoFitColumn فهرس العمود (الخاص بالعمود على وشك تغيير حجمه) كمعامل.

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
## **تحميل كود الجري**
تحميل**احتواء تلقائي للصفوف والأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
