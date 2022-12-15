---
title: إدخال وحذف الصفوف والأعمدة في Python
type: docs
weight: 60
url: /ar/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, XLT python, XLTX python, insert row python, insert column python, Excel pytho
description: استخدم Python Excel API لإنشاء جداول بيانات Excel في Python. قم بإدراج أو حذف صفوف من XLSX أو XLS في تطبيقاتك Python بدون MS Office.
---
## **قم بإنشاء جداول بيانات Excel في Python - إدارة الصفوف / الأعمدة**
### **إدخال صف**
أدخل صفًا في أي مكان باستدعاء طريقة insertRows للمجموعة Cells. تأخذ طريقة insertRows فهرس الصف حيث سيتم إدراج الصف الجديد كوسيطة أولى ، وعدد الصفوف التي سيتم إدراجها كوسيطة ثانية. فيما يلي الخطوات:

- قم بتحميل مصنف XLS أو XLSX
- قم بالوصول إلى ورقة العمل
- أدخل الصف
- حفظ كمصنف XLS أو XLSX

**Python كود**

{{< highlight "python" >}}

 def insert_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 

{{< /highlight >}}
### **إدراج صفوف متعددة**
لإدراج عدة صفوف في ورقة العمل ، قم باستدعاء الأسلوب insertRows للمجموعة Cells. تأخذ طريقة InsertRows معلمتين:

- فهرس الصف ، فهرس الصف حيث سيتم إدراج الصفوف الجديدة.
- عدد الصفوف ، إجمالي عدد الصفوف التي يجب إدراجها.

**Python كود**

{{< highlight "python" >}}

 def insert_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,10)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 


{{< /highlight >}}
### **حذف صف**
لحذف صف في أي مكان ، قم باستدعاء طريقة deleteRows للمجموعة Cells. تأخذ طريقة DeleteRows معلمتين:

- فهرس الصف ، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف ، إجمالي عدد الصفوف التي يجب حذفها.

**Python كود**

{{< highlight "python" >}}

 def delete_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 3rd row from the worksheet

worksheet.getCells().deleteRows(2,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 

{{< /highlight >}}
### **حذف عدة صفوف**
لحذف عدة صفوف من ورقة العمل ، قم باستدعاء الأسلوب deleteRows للمجموعة Cells. تأخذ طريقة DeleteRows معلمتين:

- فهرس الصف ، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف ، إجمالي عدد الصفوف التي يجب حذفها.

**Python كود**

{{< highlight "python" >}}

 def delete_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 10 rows from the worksheet starting from 3rd row

worksheet.getCells().deleteRows(2,10,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 


{{< /highlight >}}
### **إدخال عمود**
يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء طريقة insertColumns للمجموعة Cells. تأخذ طريقة insertColumns معلمتين:

- فهرس العمود ، فهرس العمود حيث سيتم إدراج العمود
- عدد الأعمدة ، إجمالي عدد الأعمدة التي يجب إدراجها

**Python كود**

{{< highlight "python" >}}

 def insert_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a column into the worksheet at 2nd position

worksheet.getCells().insertColumns(1,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 


{{< /highlight >}}
### **حذف عمود**
لحذف عمود من ورقة العمل في أي مكان ، قم باستدعاء طريقة deleteColumns للمجموعة Cells. تأخذ طريقة deleteColumns المعلمات التالية:

- فهرس العمود ، فهرس العمود الذي سيتم حذف العمود منه.
- عدد الأعمدة ، إجمالي عدد الأعمدة التي يجب حذفها.
- تحول الخلايا ، المعلمة المنطقية للإشارة إلى ما إذا كان سيتم نقل الخلايا المتبقية بعد الحذف.

**Python كود**

{{< highlight "python" >}}

 def delete_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting a column from the worksheet at 2nd position

worksheet.getCells().deleteColumns(1,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 


{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**إدارة الصفوف / الأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
