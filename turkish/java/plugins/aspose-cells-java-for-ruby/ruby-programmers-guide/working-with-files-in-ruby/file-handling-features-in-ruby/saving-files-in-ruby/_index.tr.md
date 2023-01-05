---
title: Ruby'de Dosyaları Kaydetmek
type: docs
weight: 20
url: /tr/java/saving-files-in-ruby/
---
## **Aspose.Cells - Dosyaları Kaydetme**
### **Dosyayı bir konuma kaydetme**
 Geliştiricilerin dosyalarını kullanarak kaydetmeleri gerekiyorsa**Yakut için Aspose.Cells Java** bir depolama konumuna daha sonra dosya adını (tam depolama yolu ile birlikte) ve istenen dosya formatını (kullanarak) belirtebilirler.**Dosya Biçimi Türü**numaralandırma) çağrılırken**kayıt etmek**yöntemi**Çalışma kitabı**nesne.

**Yakut Kodu**

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
