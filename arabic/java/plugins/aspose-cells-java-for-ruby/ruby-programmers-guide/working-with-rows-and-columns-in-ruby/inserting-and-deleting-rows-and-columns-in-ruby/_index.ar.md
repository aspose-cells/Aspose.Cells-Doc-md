---
title: ادراج وحذف الصفوف والاعمده في روبي
type: docs
weight: 60
url: /ar/java/inserting-and-deleting-rows-and-columns-in-ruby/
---
## **Aspose.Cells - إدارة الصفوف / الأعمدة**
### **إدخال صف**
أدخل صفًا في أي مكان عن طريق استدعاء طريقة insertRows للمجموعة Cells. تأخذ طريقة insertRows فهرس الصف حيث سيتم إدراج الصف الجديد كوسيطة أولى ، وعدد الصفوف التي سيتم إدراجها كوسيطة ثانية.

**كود روبي**

{{< highlight "ruby" >}}

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
لإدراج عدة صفوف في ورقة العمل ، قم باستدعاء الأسلوب insertRows للمجموعة Cells. تأخذ طريقة InsertRows معلمتين:

- فهرس الصف ، فهرس الصف حيث سيتم إدراج الصفوف الجديدة.
- عدد الصفوف ، إجمالي عدد الصفوف التي يجب إدراجها.

**كود روبي**

{{< highlight "ruby" >}}

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
لحذف صف في أي مكان ، قم باستدعاء طريقة deleteRows للمجموعة Cells. تأخذ طريقة DeleteRows معلمتين:

- فهرس الصف ، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف ، إجمالي عدد الصفوف التي يجب حذفها.

**كود روبي**

{{< highlight "ruby" >}}

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
### **حذف عدة صفوف**
لحذف عدة صفوف من ورقة العمل ، قم باستدعاء الأسلوب deleteRows للمجموعة Cells. تأخذ طريقة DeleteRows معلمتين:

- فهرس الصف ، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف ، إجمالي عدد الصفوف التي يجب حذفها.

**كود روبي**

{{< highlight "ruby" >}}

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
### **إدخال عمود**
يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء طريقة insertColumns للمجموعة Cells. تأخذ طريقة insertColumns معلمتين:

- فهرس العمود ، فهرس العمود حيث سيتم إدراج العمود
- عدد الأعمدة ، إجمالي عدد الأعمدة التي يجب إدراجها

**كود روبي**

{{< highlight "ruby" >}}

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
لحذف عمود من ورقة العمل في أي مكان ، قم باستدعاء طريقة deleteColumns للمجموعة Cells. تأخذ طريقة deleteColumns المعلمات التالية:

- فهرس العمود ، فهرس العمود الذي سيتم حذف العمود منه.
- عدد الأعمدة ، إجمالي عدد الأعمدة التي يجب حذفها.
- تحول الخلايا ، المعلمة المنطقية للإشارة إلى ما إذا كان سيتم نقل الخلايا المتبقية بعد الحذف.

**كود روبي**

{{< highlight "ruby" >}}

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
## **تحميل كود الجري**
 تحميل**إدارة الصفوف / الأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
