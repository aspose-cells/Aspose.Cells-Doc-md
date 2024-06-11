---
title: 在Ruby中显示或隐藏标签页
type: docs
weight: 40
url: /zh/java/display-or-hide-tabs-in-ruby/
---

## **Aspose.Cells - 显示或隐藏标签页**
### **隐藏选项卡**
要使用**Aspose.Cells Java for Ruby**隐藏标签页，请调用**displayhidetabs**模块。

**Ruby 代码**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **使选项卡可见**
通过将Workbook类的setSheetTabBarHidden(false)方法使标签页可见。

**Ruby 代码**

{{< highlight ruby >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**隐藏或显示标签页 (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
