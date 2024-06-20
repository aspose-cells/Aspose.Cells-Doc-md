---
title: إدارة ورق العمل في Ruby
type: docs
weight: 10
url: /ar/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - إدارة ورق العمل**
### **إضافة ورقات العمل إلى ملف Excel جديد**
لإضافة ورقة عمل إلى ملف Excel جديد باستخدام برنامج **Aspose.Cells Java for Ruby**, قم ببساطة بإستدعاء الطريقة **add_worksheet** من وحدة **MangingWorksheets**.

**كود Ruby**

{{< highlight ruby >}}

 def add_worksheet()

    # Instantiating a Workbook object

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book.out.xls")

    puts "Sheet added successfully."

end 

{{< /highlight >}}
### **إضافة ورقات عمل إلى جدول التصميم**
إن عملية إضافة أوراق العمل إلى جدول بيانات المصمم متطابقة تمامًا مع الطريقة المذكورة أعلاه باستثناء أن ملف Excel تم إنشاؤه بالفعل ونحتاج إلى فتح ذلك الملف أولاً قبل إضافة ورقة عمل إليه.

**كود Ruby**

{{< highlight ruby >}}

 def add_worksheet_to_designer_spreadsheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book1.out.xls")

end  

{{< /highlight >}}
### **الوصول إلى الأوراق العمل باستخدام اسم الورقة**
للوصول إلى ورقة العمل بواسطة اسم الورقة باستخدام **Aspose.Cells Java for Ruby**, قم ببساطة بإستدعاء الطريقة **get_worksheet** من وحدة **MangingWorksheets**.

**كود Ruby**

{{< highlight ruby >}}

 def get_worksheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Accessing a worksheet using its sheet name

    worksheet = workbook.getWorksheets().get("Sheet1")

    puts worksheet.to_string

end

{{< /highlight >}}
### **إزالة الأوراق العمل باستخدام اسم الورقة**
لإزالة ورقة العمل بواسطة اسم الورقة باستخدام **Aspose.Cells Java for Ruby**, قم ببساطة بإستدعاء الثريقة **remove_worksheet_by_name** من وحدة **MangingWorksheets**.

**كود Ruby**

{{< highlight ruby >}}

 def remove_worksheet_by_name()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt("Sheet1")



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end


{{< /highlight >}}
### **إزالة الأوراق العمل باستخدام فهرس الورقة**
لإزالة ورقة العمل حسب فهرس الورقة باستخدام **Aspose.Cells Java for Ruby**، قم ببساطة بالاستدعاء **remove_worksheet_by_index** لوحدة **MangingWorksheets**.

**كود Ruby**

{{< highlight ruby >}}

 def remove_worksheet_by_index()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt(0)



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end 

{{< /highlight >}}
## **تحميل رمز التشغيل**
قم بتنزيل  **إدارة الورقة (Aspose.Cells)**  من أي من مواقع التعاون البرمجي الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
