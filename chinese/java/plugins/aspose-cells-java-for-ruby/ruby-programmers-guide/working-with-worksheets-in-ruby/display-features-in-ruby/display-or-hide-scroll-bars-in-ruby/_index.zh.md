---
title: 在Ruby中显示或隐藏滚动条
type: docs
weight: 30
url: /zh/java/display-or-hide-scroll-bars-in-ruby/
---

## **Aspose.Cells - 显示或隐藏滚动条**
### **隐藏滚动条**
要使用**Aspose.Cells Java for Ruby**隐藏滚动条，请调用**displayhidescrollbars**模块。

**Ruby 代码**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false)

\# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Scroll Bars are now hidden, please check the output file."

{{< /highlight >}}
### **显示滚动条**
通过将Workbook类的setVerticalScrollBarHidden()或setHorizontalScrollBarHidden()方法设置为true，使滚动条可见。

**Ruby 代码**

{{< highlight ruby >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**Display or Hide Scroll Bars (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
