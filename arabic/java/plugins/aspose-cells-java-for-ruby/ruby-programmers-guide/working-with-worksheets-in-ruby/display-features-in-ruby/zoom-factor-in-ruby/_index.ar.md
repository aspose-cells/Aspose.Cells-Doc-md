---
title: عامل التكبير في روبي
type: docs
weight: 90
url: /ar/java/zoom-factor-in-ruby/
---

## **Aspose.Cells - عامل التكبير**
لضبط عامل التكبير باستخدام **Aspose.Cells Java for Ruby**, قم ببساطة بإستدعاء وحدة **ZoomFactor**.

**كود Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Setting the zoom factor of the worksheet to 75     

worksheet.setZoom(75)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Set zoom factor, please check the output file."

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل  **Zoom Factor (Aspose.Cells)** من أي من المواقع الإجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/zoomfactor.rb)
