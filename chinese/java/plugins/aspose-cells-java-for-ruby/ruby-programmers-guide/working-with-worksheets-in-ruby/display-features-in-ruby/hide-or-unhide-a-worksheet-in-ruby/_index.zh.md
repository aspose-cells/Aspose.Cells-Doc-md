---
title: 在Ruby中隐藏或取消隐藏工作表
type: docs
weight: 60
url: /zh/java/hide-or-unhide-a-worksheet-in-ruby/
---

## **Aspose.Cells - 隐藏或取消隐藏工作表**
### **隐藏工作表**
通过Aspose.Cells Java for Ruby使用**hideunhideworksheet**模块来隐藏工作表。

**Ruby 代码**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Hiding the first worksheet of the Excel file

worksheet.setVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **显示工作表**
开发者可以通过设置**Worksheet**类的*setVisible(* *true* *)*方法来使工作表可见。

**Ruby 代码**

{{< highlight ruby >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **下载运行代码**
从以下社交编码网站中下载**隐藏或取消隐藏工作表（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
