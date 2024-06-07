---
title: Ruby中的Hello World
type: docs
weight: 10
url: /zh/java/hello-world-in-ruby/
---

## **Aspose.Cells - Hello World**
要在Ruby中使用Aspose.Cells for Java写入电子表格文档，只需调用HelloWorld模块。

**Ruby代码**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object that represents a Microsoft Excel file.

workbook = Rjb::import('com.aspose.cells.Workbook').new

\# Note when you create a new workbook, a default worksheet,

\# "Sheet1", is by default added to the workbook.

\# Accessing the first worksheet in the book ("Sheet1").

sheet = workbook.getWorksheets().get(0)

\# Access cell "A1" in the sheet.

cell = sheet.getCells().get("A1")

\# Input the "Hello World!" text into the "A1" cell

cell.setValue("Hello World!")

\# Saving the modified Excel file in default (that is Excel 2003) format

file_format_type = Rjb::import('com.aspose.cells.FileFormatType')

workbook.save(data_dir + "HelloWorld.xls", file_format_type.EXCEL_97_TO_2003)

puts "Document has been saved, please check the output file."

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**Hello World(Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/helloworld.rb)
