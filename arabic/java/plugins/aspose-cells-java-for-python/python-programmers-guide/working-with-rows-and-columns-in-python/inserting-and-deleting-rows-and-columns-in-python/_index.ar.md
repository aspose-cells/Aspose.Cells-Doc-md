---
title: إدراج وحذف الصفوف والأعمدة في Python
type: docs
weight: 60
url: /ar/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: "إنشاء XLSX في بايثون، إنشاء XLS في بايثون، XLS python، XLSX python، XLT python، XLTX python، إدراج صف بايثون، إدراج عمود بايثون، إكسل بايثون"
description: استخدام واجهة برمجة تطبيقات إكسل في بايثون لإنشاء جداول بيانات إكسل في بايثون. إدراج أو حذف الصفوف من XLSX أو XLS في تطبيقاتك بايثون بدون MS Office.
---

## **إنشاء جداول بيانات إكسل في بايثون - إدارة الصفوف/الأعمدة**
### **إدراج صف**
إدراج صف في أي موقع عن طريق استدعاء طريقة insertRows في مجموعة الخلايا. تأخذ الطريقة insertRows الفهرس للصف الذي سيتم إدراج الصف الجديد فيه كالمعامل الأول، وعدد الصفوف التي يجب إدراجها كالمعامل الثاني. فيما يلي الخطوات:

- تحميل XLS أو مصحح XLSX
- الوصول إلى ورقة العمل
- إدراج الصف
- حفظ مصحح XLS أو XLSX

**كود Python**

{{< highlight python >}}

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
لإدراج صفوف متعددة في الورقة العمل، اُناد الطريقة insertRows من مجموعة Cells. تأخذ طريقة InsertRows معها معلمتين:

- فهرس الصف، الفهرس للصف من حيث إن الصفوف الجديدة ستدرج.
- عدد الصفوف، العدد الإجمالي للصفوف التي يجب إدراجها.

**كود Python**

{{< highlight python >}}

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
لحذف صف في أي مكان، اُناد الطريقة deleteRows من مجموعة Cells. تأخذ طريقة DeleteRows معها معلمتيتن:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، العدد الإجمالي للصفوف التي يجب حذفها.

**كود Python**

{{< highlight python >}}

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
### **حذف صفوف متعددة**
لحذف صفوف متعددة من ورقة العمل، اُناد الطريقة deleteRows من مجموعة Cells. تأخذ طريقة DeleteRows معها معلمتين:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، العدد الإجمالي للصفوف التي يجب حذفها.

**كود Python**

{{< highlight python >}}

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
### **إدراج عمود**
يُمكن للمطوِّرون أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق اُناد الطريقة insertColumns من مجموعة Cells. تأخذ طريقة insertColumns معها معلمتين:

- فهرس العمود، فهرس العمود الذي سيتم إدراج العمود منه
- عدد الأعمدة، العدد الإجمالي للأعمدة التي يجب إدراجها

**كود Python**

{{< highlight python >}}

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
لاحذف عمود من ورقة العمل في أي موقع، قم بإستدعاء طريقة الحذف الأعمدة من مجموعة الخلايا. تأخذ طريقة حذف الأعمدة المتغيرات التالية:

- فهرس العمود، وهو فهرس العمود الذي سيتم حذفه.
- عدد الأعمدة، العدد الإجمالي للأعمدة التي ينبغي حذفها.
- تحريك الخلايا، المعلمة البولية للإشارة إذا كان يجب تحريك الخلايا لليسار بعد الحذف.

**كود Python**

{{< highlight python >}}

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
## **تحميل رمز التشغيل**
تنزيل **إدارة الصفوف/الأعمدة (Aspose.Cells)** من أي من المواقع التالية للبرمجة الاجتماعية:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
