---
title: عرض رؤوس أعمدة الصفوف أو إخفاؤها في Ruby
type: docs
weight: 20
url: /ar/java/display-or-hide-row-column-headers-in-ruby/
---
## **Aspose.Cells - عرض أو إخفاء رؤوس أعمدة الصف**
### **إخفاء رؤوس الصفوف / الأعمدة**
 لإخفاء رؤوس الصفوف / الأعمدة باستخدام**Aspose.Cells Java لروبي** ، مكالمة**DisplayHideRowColumnHeaders** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

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
### **جعل رؤوس الصفوف / الأعمدة مرئية**
اجعل رؤوس الصفوف والأعمدة مرئية باستخدام أسلوب setRowColumnHeadersVisible (true) لفئة ورقة العمل.

**كود روبي**

{{< highlight "ruby" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**عرض رؤوس أعمدة الصفوف أو إخفاؤها (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
