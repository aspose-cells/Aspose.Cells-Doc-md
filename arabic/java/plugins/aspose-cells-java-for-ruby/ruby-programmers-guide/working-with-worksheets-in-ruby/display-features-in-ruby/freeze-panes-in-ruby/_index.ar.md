---
title: تجميد الألواح في Ruby
type: docs
weight: 50
url: /ar/java/freeze-panes-in-ruby/
---

## **Aspose.Cells - تجميد الألواح**
لتجميد الألواح في مستند الجدول النصي باستخدام **Aspose.Cells Java for Ruby**، قم ببساطة باستدعاء الوحدة **FreezePanes**.

**كود Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Apply freeze panes settings, please check the output file."

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **تجميد الألواح (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/freezepanes.rb)
