---
title: Ruby de Dosyaları Kaydetme
type: docs
weight: 20
url: /tr/java/saving-files-in-ruby/
---

## **Aspose.Cells - Dosyaları Kaydetme**
### **Dosyayı belirli bir konuma kaydetme**
Geliştiriciler, **Aspose.Cells** Java için Ruby kullanarak dosyalarını belirli bir depolama konumuna kaydetmeleri gerekiyorsa, belirli bir depolama yolunu (tam depolama yoluna sahip) ve arzu edilen dosya biçimini ( **FileFormatType** numaralandırmasını kullanarak) belirtirken **Workbook** nesnesinin **save** metodunu çağırabilirler.

**Ruby Kodu**

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
