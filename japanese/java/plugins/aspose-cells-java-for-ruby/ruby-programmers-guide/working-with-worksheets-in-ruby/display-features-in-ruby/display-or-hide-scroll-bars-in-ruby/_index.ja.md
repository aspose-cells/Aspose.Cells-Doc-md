---
title: Rubyでスクロールバーを表示または非表示にする
type: docs
weight: 30
url: /ja/java/display-or-hide-scroll-bars-in-ruby/
---

## **Aspose.Cells - スクロールバーの表示または非表示**
### **スクロールバーを非表示にする**
Aspose.Cells Java for Rubyを使用してスクロールバーを非表示にするには、displayhidescrollbarsモジュールを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false)

\# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Scroll Bars are now hidden, please check the output file."

{{< /highlight >}}
### **スクロールバーを表示する**
縦スクロールバーを非表示にするには、WorkbookクラスのsetVerticalScrollBarHidden()メソッドをtrueに設定します。

**Ruby Code**

{{< highlight ruby >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **ランニングコードのダウンロード**
**Aspose.Cells**のDisplay or Hide Scroll Barsを以下に示すソーシャルコーディングサイトからダウンロードする:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
