---
title: Ruby でタブを表示または非表示にする
type: docs
weight: 40
url: /ja/java/display-or-hide-tabs-in-ruby/
---
## **Aspose.Cells - タブの表示または非表示**
### **タブを非表示にする**
を使用してタブを非表示にするには**Aspose.Cells Ruby の場合は Java**、 電話**表示非表示タブ**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

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
Workbook クラスの setSheetTabBarHidden(false) メソッドでタブを表示します。

**ルビーコード**

{{< highlight "ruby" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**タブを非表示または表示または非表示にする (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
