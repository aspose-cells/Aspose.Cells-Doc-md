---
title: Rubyでタブを表示または非表示にする
type: docs
weight: 40
url: /ja/java/display-or-hide-tabs-in-ruby/
---

## **Aspose.Cells - タブの表示または非表示**
### **タブを非表示にする**
Aspose.Cells Java for Rubyを使用してタブを非表示にするには、displayhidetabsモジュールを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **タブを表示する**
WorkbookクラスのsetSheetTabBarHidden(false)メソッドを使用して、タブを表示する

**Ruby Code**

{{< highlight ruby >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、Aspose.CellsのHide or Display or Hide Tabsをダウンロードする: 

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
