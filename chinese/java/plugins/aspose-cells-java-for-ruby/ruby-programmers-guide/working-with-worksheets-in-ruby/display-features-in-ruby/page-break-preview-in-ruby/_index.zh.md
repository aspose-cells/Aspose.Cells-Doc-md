---
title: 在Ruby中的分页预览
type: docs
weight: 70
url: /zh/java/page-break-preview-in-ruby/
---

## **Aspose.Cells - 页面分页预览**
使用**Aspose.Cells Java for Ruby**简单调用**PageBreakPreview**模块即可将工作表设置为分页预览。

**Ruby 代码**

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
## **下载运行代码**
从以下社交编码网站中下载**分页预览（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreakpreview.rb)
