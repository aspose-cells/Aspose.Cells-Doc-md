---
title: Rubyで行列ヘッダーを表示または非表示にする
type: docs
weight: 20
url: /ja/java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - 行列ヘッダーの表示または非表示**
### **行/列ヘッダーを非表示にする**
Aspose.Cells Java for Rubyを使用して行/列ヘッダーを非表示にするには、DisplayHideRowColumnHeadersモジュールを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the headers of rows and columns

worksheet.setRowColumnHeadersVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Headers of rows and columns are now hidden, please check the output file."

{{< /highlight >}}
### **行/列ヘッダーを表示する**
行列ヘッダーを表示するには、WorksheetクラスのsetRowColumnHeadersVisible(true)メソッドを使用します。

**Ruby Code**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **ランニングコードのダウンロード**
**Aspose.Cells**のDisplay or Hide Row Column Headersを以下に示すソーシャルコーディングサイトからダウンロードする:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
