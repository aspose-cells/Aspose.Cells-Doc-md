---
title: 在 Ruby 中隐藏或取消隐藏工作表
type: docs
weight: 60
url: /zh/java/hide-or-unhide-a-worksheet-in-ruby/
---
## **Aspose.Cells - 隐藏或取消隐藏工作表**
### **隐藏工作表**
要使用 Aspose.Cells Java 为 Ruby 隐藏工作表，请调用**隐藏取消隐藏工作表**模块。

**红宝石代码**

{{< highlight "ruby" >}}

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
开发人员可以通过设置*设置可见（* *真的* *)*的方法**工作表**班级。

**红宝石代码**

{{< highlight "ruby" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **下载运行代码**
下载**隐藏或取消隐藏工作表 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
