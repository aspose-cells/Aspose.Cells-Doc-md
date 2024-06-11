---
title: 在Ruby中显示或隐藏网格线
type: docs
weight: 10
url: /zh/java/display-or-hide-gridlines-in-ruby/
---

## **Aspose.Cells - 显示或隐藏网格线**
### **隐藏网格线**
要使用**Aspose.Cells Java for Ruby**隐藏工作表，请调用**displayhidegridlines**模块。

**Ruby 代码**

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
### **使网格线可见**
要显示网格线，使用工作表类的setGridlinesVisible(true)方法。

**Ruby 代码**

{{< highlight ruby >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**Display or Hide Gridlines (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
