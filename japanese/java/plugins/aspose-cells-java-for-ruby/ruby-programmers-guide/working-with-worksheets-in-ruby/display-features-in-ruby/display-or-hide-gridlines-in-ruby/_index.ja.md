---
title: Rubyでグリッド線を表示または非表示にする
type: docs
weight: 10
url: /ja/java/display-or-hide-gridlines-in-ruby/
---

## **Aspose.Cells - グリッド線の表示または非表示**
### **グリッド線を非表示にする**
**Aspose.Cells Java for Ruby**を使用してワークシートを非表示にするには、**displayhidegridlines**モジュールを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the gridlines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Gridlines are now hidden, please check the output file."

{{< /highlight >}}
### **グリッド線を表示する**
グリッド線を表示するには、WorksheetクラスのsetGridlinesVisible(true)メソッドを使用します。

**Ruby Code**

{{< highlight ruby >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **ランニングコードのダウンロード**
**Aspose.Cells**のDisplay or Hide Gridlinesを以下に示すソーシャルコーディングサイトからダウンロードする:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
