---
title: عرض أو إخفاء رؤوس الصف العمود في روبي
type: docs
weight: 20
url: /ar/java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - عرض أو إخفاء رؤوس الصف العمود**
### **إخفاء رؤوس الصف/العمود**
لإخفاء رؤوس الصف/العمود باستخدام **Aspose.Cells Java for Ruby**, اتصل بوحدة **DisplayHideRowColumnHeaders**.

**كود Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the headers of rows and columns

worksheet.setRowColumnHeadersVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Headers of rows and columns are now hidden, please check the output file."

{{< /highlight >}}
### **جعل رؤوس الصف/العمود مرئية**
جعل رؤوس الصف والعمود مرئية باستخدام الوسيطة setRowColumnHeadersVisible(true) في فئة Worksheet.

**كود Ruby**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **إظهار أو إخفاء رؤوس الصفوف والأعمدة (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
