---
title: 在 Ruby 中保存文件
type: docs
weight: 20
url: /zh/java/saving-files-in-ruby/
---
## **Aspose.Cells - 保存文件**
### **将文件保存到某个位置**
如果开发人员需要使用**Aspose.Cells Java 红宝石**到某个存储位置，然后他们可以简单地指定文件名（及其完整的存储路径）和所需的文件格式（使用**文件格式类型**枚举），同时调用**救球**的方法**工作簿**目的。

**红宝石代码**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

file_format_type = Rjb::import('com.aspose.cells.FileFormatType')

\# Save in default (Excel2003) format

workbook.save(data_dir + "Book1.xls")

# Save in Excel2003 format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_97_TO_2003)

\# Save in Excel2007 xlsx format

workbook.save(data_dir + "Book1.xls", file_format_type.XLSX)

\# Save in SpreadsheetML format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_2003_XML)

{{< /highlight >}}
