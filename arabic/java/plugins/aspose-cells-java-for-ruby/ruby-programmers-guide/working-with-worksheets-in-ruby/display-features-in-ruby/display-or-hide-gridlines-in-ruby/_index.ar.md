---
title: عرض أو إخفاء خطوط الشبكة في روبي
type: docs
weight: 10
url: /ar/java/display-or-hide-gridlines-in-ruby/
---

## **Aspose.Cells - عرض أو إخفاء خطوط الشبكة**
### **إخفاء خطوط الشبكة**
لإخفاء ورقة العمل باستخدام **Aspose.Cells Java for Ruby**, اتصل بوحدة **displayhidegridlines**.

**كود Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the gridlines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Gridlines are now hidden, please check the output file."

{{< /highlight >}}
### **جعل خطوط الشبكة مرئية**
لجعل خطوط الشبكة مرئية، استخدم الوسيطة setGridlinesVisible(true) في فئة Worksheet.

**كود Ruby**

{{< highlight ruby >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **عرض أو إخفاء خطوط الشبكة (Aspose.Cells)** من أي من المواقع المشفرة المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
