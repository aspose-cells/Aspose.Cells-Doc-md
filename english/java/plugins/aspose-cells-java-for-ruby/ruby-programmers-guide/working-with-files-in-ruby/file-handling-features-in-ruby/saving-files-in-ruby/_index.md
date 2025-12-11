---
title: Saving Files in Ruby
type: docs
weight: 20
url: /java/saving-files-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Saving Files**
### **Saving file to some location**
If developers need to save their files using **Aspose.Cells Java for Ruby** to some storage location, then they can simply specify the file name (with its complete storage path) and the desired file format (using the **FileFormatType** enumeration) while calling the **save** method of the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) object.

**Ruby Code**

{{< highlight ruby >}}
data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

file_format_type = Rjb::import('com.aspose.cells.FileFormatType')

# Save in default (Excel2003) format
workbook.save(data_dir + "Book1.xls")

# Save in Excel2003 format
workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_97_TO_2003)

# Save in Excel2007 xlsx format
workbook.save(data_dir + "Book1.xls", file_format_type.XLSX)

# Save in SpreadsheetML format
workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_2003_XML)
{{< /highlight >}}
