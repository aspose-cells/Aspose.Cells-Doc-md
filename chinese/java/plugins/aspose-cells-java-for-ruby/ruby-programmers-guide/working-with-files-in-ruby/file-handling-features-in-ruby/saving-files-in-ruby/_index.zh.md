---
title: 在Ruby中保存文件
type: docs
weight: 20
url: /zh/java/saving-files-in-ruby/
---

## **Aspose.Cells - 保存文件**
### **将文件保存到某个位置**
如果开发人员需要使用**Aspose.Cells Java for Ruby**将其文件保存到某个存储位置，那么他们可以在调用**Workbook**对象的**save**方法时指定文件名（包括完整的存储路径）和所需的文件格式（使用 **FileFormatType** 枚举）。

**Ruby 代码**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

file_format_type = Rjb::import('com.aspose.cells.FileFormatType')

\# Save in default (Excel2003) format

workbook.save(data_dir + "Book1.xls")

#Save in Excel2003 format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_97_TO_2003)

\# Save in Excel2007 xlsx format

workbook.save(data_dir + "Book1.xls", file_format_type.XLSX)

\# Save in SpreadsheetML format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_2003_XML)

{{< /highlight >}}
