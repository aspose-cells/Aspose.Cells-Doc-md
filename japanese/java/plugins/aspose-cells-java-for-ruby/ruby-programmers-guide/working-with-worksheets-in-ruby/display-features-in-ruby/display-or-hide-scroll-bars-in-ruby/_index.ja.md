---
title: Ruby でスクロール バーを表示または非表示にする
type: docs
weight: 30
url: /ja/java/display-or-hide-scroll-bars-in-ruby/
---
## **Aspose.Cells - スクロール バーの表示または非表示**
### **スクロール バーを非表示にする**
を使用してスクロール バーを非表示にするには**Aspose.Cells Ruby の場合は Java**、 電話**スクロールバーを非表示にする**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

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
### **スクロール バーを表示する**
Workbook クラスの setVerticalScrollBarHidden() または setHorizontalScrollBarHidden() メソッドを true に設定して、スクロール バーを表示します。

**ルビーコード**

{{< highlight "ruby" >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**スクロールバーを表示または非表示にする (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
