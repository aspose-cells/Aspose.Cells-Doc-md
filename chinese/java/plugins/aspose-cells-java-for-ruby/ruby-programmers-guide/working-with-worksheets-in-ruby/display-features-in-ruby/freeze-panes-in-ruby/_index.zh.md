---
title: 在 Ruby 中冻结窗格
type: docs
weight: 50
url: /zh/java/freeze-panes-in-ruby/
---

## **Aspose.Cells - 冻结窗格**
要在电子表格文档中使用**Aspose.Cells Java for Ruby**冻结窗格，请简单调用**FreezePanes**模块。

**Ruby代码**

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
## **下载运行代码**
从下面列出的任何社交编码站点下载**冻结窗格（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/freezepanes.rb)
