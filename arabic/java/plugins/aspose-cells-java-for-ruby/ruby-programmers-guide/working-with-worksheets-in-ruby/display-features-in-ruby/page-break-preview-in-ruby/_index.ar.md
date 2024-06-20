---
title: معاينة كسر الصفحات في روبي
type: docs
weight: 70
url: /ar/java/page-break-preview-in-ruby/
---

## **Aspose.Cells - معاينة كسر الصفحات**
لتعيين ورقة عمل إلى معاينة كسر الصفحات باستخدام **Aspose.Cells Java for Ruby**، قم ببساطة بدعوة الوحدة **PageBreakPreview**.

**كود Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(true)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Set page break preview, please check the output file."

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **معاينة كسر الصفحات (Aspose.Cells)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreakpreview.rb)
