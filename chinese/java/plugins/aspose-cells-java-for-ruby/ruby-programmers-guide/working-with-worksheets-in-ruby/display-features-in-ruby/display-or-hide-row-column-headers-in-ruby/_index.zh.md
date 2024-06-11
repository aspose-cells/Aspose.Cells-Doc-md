---
title: 在Ruby中显示或隐藏行列标题
type: docs
weight: 20
url: /zh/java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - 显示或隐藏行列标题**
### **隐藏行/列标头**
要使用**Aspose.Cells Java for Ruby**隐藏行/列标题，请调用**DisplayHideRowColumnHeaders**模块。

**Ruby 代码**

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
### **使行/列标头可见**
通过使用工作表类的setRowColumnHeadersVisible(true)方法，使行和列标题可见。

**Ruby 代码**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**Display or Hide Row Column Headers (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
