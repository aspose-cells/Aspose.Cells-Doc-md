---
title: Spara filer i Ruby
type: docs
weight: 20
url: /sv/java/saving-files-in-ruby/
---

## **Aspose.Cells - Spara filer**
### **Spara filen på en viss plats**
Om utvecklare behöver spara sina filer med hjälp av **Aspose.Cells Java för Ruby** på en viss lagringsplats kan de helt enkelt ange filnamnet (med dess fullständiga lagringsväg) och önskat filformat (använda **FileFormatType** uppräkningen) vid anrop av **save** metoden för **Workbook** objektet.

**Ruby-kod**

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
