---
title: 在Ruby中拆分窗格
type: docs
weight: 80
url: /zh/java/split-panes-in-ruby/
---

## **Aspose.Cells - 拆分窗格**
使用**Aspose.Cells Java for Ruby**简单调用**SplitPanes**模块即可拆分窗格。

**Ruby 代码**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20")

\# Split the worksheet window

workbook.getWorksheets().get(0).split()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "SplitPanes output.xls")

puts "Panes split successfully."

{{< /highlight >}}
## **下载运行代码**
从以下社交编码网站中下载**拆分窗格（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/splitpanes.rb)
