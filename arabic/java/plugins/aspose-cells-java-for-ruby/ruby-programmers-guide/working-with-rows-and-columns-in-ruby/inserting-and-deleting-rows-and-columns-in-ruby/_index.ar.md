---
title: إدراج وحذف الصفوف والأعمدة في روبي
type: docs
weight: 60
url: /ar/java/inserting-and-deleting-rows-and-columns-in-ruby/
---

## **Aspose.Cells - إدارة الصفوف/الأعمدة**
### **إدراج صف**
أدرج صفًا في أي موقع عن طريق استدعاء طريقة insertRows لمجموعة Cells. تأخذ طريقة insertRows فهرس الصف حيث سيتم إدراج الصف الجديد كمعلمة أولى، وعدد الأسطر التي سيتم إدراجها كمعلمة ثانوية.

**كود Ruby**

{{< highlight ruby >}}

 def insert_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Row.xls")

    puts "Insert Row Successfully."

end   

{{< /highlight >}}
### **إدراج صفوف متعددة**
لإدراج صفوف متعددة في الورقة العمل، اُناد الطريقة insertRows من مجموعة Cells. تأخذ طريقة InsertRows معها معلمتين:

- فهرس الصف، الفهرس للصف من حيث إن الصفوف الجديدة ستدرج.
- عدد الصفوف، العدد الإجمالي للصفوف التي يجب إدراجها.

**كود Ruby**

{{< highlight ruby >}}

 def insert_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,10)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Multiple Rows.xls")

    puts "Insert Multiple Rows Successfully."

end

{{< /highlight >}}
### **حذف صف**
لحذف صف في أي مكان، اُناد الطريقة deleteRows من مجموعة Cells. تأخذ طريقة DeleteRows معها معلمتيتن:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، العدد الإجمالي للصفوف التي يجب حذفها.

**كود Ruby**

{{< highlight ruby >}}

 def delete_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 3rd row from the worksheet

    worksheet.getCells().deleteRows(2,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Row.xls")

    puts "Delete Row Successfully."

end

{{< /highlight >}}
### **حذف صفوف متعددة**
لحذف صفوف متعددة من ورقة العمل، اُناد الطريقة deleteRows من مجموعة Cells. تأخذ طريقة DeleteRows معها معلمتين:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، العدد الإجمالي للصفوف التي يجب حذفها.

**كود Ruby**

{{< highlight ruby >}}

 def delete_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 10 rows from the worksheet starting from 3rd row

    worksheet.getCells().deleteRows(2,10,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Multiple Rows.xls")

    puts "Delete Multiple Rows Successfully."

end 

{{< /highlight >}}
### **إدراج عمود**
يُمكن للمطوِّرون أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق اُناد الطريقة insertColumns من مجموعة Cells. تأخذ طريقة insertColumns معها معلمتين:

- فهرس العمود، فهرس العمود الذي سيتم إدراج العمود منه
- عدد الأعمدة، العدد الإجمالي للأعمدة التي يجب إدراجها

**كود Ruby**

{{< highlight ruby >}}

 def insert_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a column into the worksheet at 2nd position

    worksheet.getCells().insertColumns(1,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Column.xls")

    puts "Insert Column Successfully."

end  

{{< /highlight >}}
### **حذف عمود**
لاحذف عمود من ورقة العمل في أي موقع، قم بإستدعاء طريقة الحذف الأعمدة من مجموعة الخلايا. تأخذ طريقة حذف الأعمدة المتغيرات التالية:

- فهرس العمود، وهو فهرس العمود الذي سيتم حذفه.
- عدد الأعمدة، العدد الإجمالي للأعمدة التي ينبغي حذفها.
- تحريك الخلايا، المعلمة البولية للإشارة إذا كان يجب تحريك الخلايا لليسار بعد الحذف.

**كود Ruby**

{{< highlight ruby >}}

 def delete_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting a column from the worksheet at 2nd position

    worksheet.getCells().deleteColumns(1,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Column.xls")

    puts "Delete Column Successfully."

end   

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **إدارة الصفوف/الأعمدة (Aspose.Cells)** من أي من المواقع التالية للبرمجة الاجتماعية:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
