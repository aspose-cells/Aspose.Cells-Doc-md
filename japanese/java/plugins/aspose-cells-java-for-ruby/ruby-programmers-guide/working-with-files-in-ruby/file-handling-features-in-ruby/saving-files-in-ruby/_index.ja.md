---
title: Rubyでファイルを保存する
type: docs
weight: 20
url: /ja/java/saving-files-in-ruby/
---

## **Aspose.Cells - ファイルの保存**
### **開発者がファイルをストレージに保存する必要がある場合、**Aspose.Cells Java for Ruby**を使用して**Workbook**オブジェクトの**save**メソッドを呼び出す際に、ファイル名(完全なストレージパスを含む)と希望のファイル形式(**FileFormatType**列挙型を使用)を単純に指定することができます。**
**Aspose.Cells Java for Ruby**を使用してファイルを指定の場所に保存する場合、**Workbook**オブジェクトの**save**メソッドを呼び出す際に、ファイル名（完全な保存パスとともに）と所望のファイル形式（**FileFormatType**列挙型を使用）を指定するだけです。

**Ruby Code**

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
