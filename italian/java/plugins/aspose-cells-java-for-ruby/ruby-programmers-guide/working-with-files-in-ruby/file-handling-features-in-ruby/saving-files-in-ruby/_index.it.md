---
title: Salvataggio file in Ruby
type: docs
weight: 20
url: /it/java/saving-files-in-ruby/
---

## **Aspose.Cells - Salvataggio dei file**
### **Salvataggio file in una determinata posizione**
Se gli sviluppatori devono salvare i propri file utilizzando **Aspose.Cells Java for Ruby** in una posizione di archiviazione, allora possono semplicemente specificare il nome del file (con il relativo percorso di archiviazione completo) e il formato desiderato del file (utilizzando l'enumerazione **FileFormatType**) durante la chiamata del metodo **save** dell'oggetto **Workbook**.

**Codice Ruby**

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
