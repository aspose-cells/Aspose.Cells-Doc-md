---
title: إدارة أوراق العمل في روبي
type: docs
weight: 10
url: /ar/java/managing-worksheets-in-ruby/
---
## **Aspose.Cells - إدارة أوراق العمل**
### **إضافة أوراق عمل إلى ملف Excel جديد**
 لإضافة ورقة عمل إلى ملف Excel جديد باستخدام**Aspose.Cells Java لروبي** ، ببساطة اتصل**add_worksheet** طريقة**أوراق العمل** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

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
### **إضافة أوراق عمل إلى جدول بيانات المصمم**
تتشابه عملية إضافة أوراق العمل إلى جدول بيانات المصمم تمامًا مع الطريقة المذكورة أعلاه باستثناء أن ملف Excel قد تم إنشاؤه بالفعل ونحن بحاجة إلى فتح ملف Excel هذا أولاً قبل إضافة ورقة العمل إليه.

**كود روبي**

{{< highlight "ruby" >}}

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
### **الوصول إلى أوراق العمل باستخدام اسم الورقة**
 للوصول إلى ورقة العمل باستخدام اسم الورقة**Aspose.Cells Java لروبي** ، ببساطة اتصل**get_worksheet** طريقة**أوراق العمل** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

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
### **إزالة أوراق العمل باستخدام اسم الورقة**
 لإزالة ورقة العمل حسب اسم الورقة باستخدام**Aspose.Cells Java لروبي** ، ببساطة اتصل**remove_worksheet_by_name** طريقة**أوراق العمل** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

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
### **إزالة أوراق العمل باستخدام فهرس الورقة**
 لإزالة ورقة العمل عن طريق فهرس الورقة باستخدام**Aspose.Cells Java لروبي** ، ببساطة اتصل**remove_worksheet_by_index** طريقة**أوراق العمل** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

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
## **قم بتنزيل كود التشغيل**
تحميل**إدارة أوراق العمل (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
