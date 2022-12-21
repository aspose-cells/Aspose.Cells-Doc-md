---
title: Ruby でファイルを保存する
type: docs
weight: 20
url: /ja/java/saving-files-in-ruby/
---
## **Aspose.Cells - ファイルの保存**
### **ファイルをある場所に保存する**
開発者がファイルを保存する必要がある場合**Aspose.Cells Ruby の場合は Java**ある保存場所に移動すると、ファイル名 (完全な保存パスを含む) と目的のファイル形式 (**ファイル形式の種類**列挙) の呼び出し中**セーブ**方法**ワークブック**物体。

**ルビーコード**

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
