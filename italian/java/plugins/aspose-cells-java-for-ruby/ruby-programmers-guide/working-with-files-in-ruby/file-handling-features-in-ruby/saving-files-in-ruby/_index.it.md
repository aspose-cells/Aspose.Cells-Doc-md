---
title: Salvataggio di file in Ruby
type: docs
weight: 20
url: /it/java/saving-files-in-ruby/
---
## **Aspose.Cells - Salvataggio File**
### **Salvataggio del file in una posizione**
 Se gli sviluppatori devono salvare i propri file utilizzando**Aspose.Cells Java per Ruby** in una posizione di archiviazione, possono semplicemente specificare il nome del file (con il relativo percorso di archiviazione completo) e il formato del file desiderato (utilizzando l'estensione**FileFormatType**enumerazione) mentre si chiama il**Salva**metodo di**Cartella di lavoro**oggetto.

**Codice Rubino**

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
