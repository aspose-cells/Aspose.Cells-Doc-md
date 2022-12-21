---
title: Ruby でペインを分割する
type: docs
weight: 80
url: /ja/java/split-panes-in-ruby/
---
## **Aspose.Cells - ペインの分割**
を使用してペインを分割するには**Aspose.Cells Ruby の場合は Java**、単に呼び出す**SplitPanes**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20")

\# Split the worksheet window

workbook.getWorksheets().get(0).split()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "SplitPanes output.xls")

puts "Panes split successfully."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**分割ペイン (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/splitpanes.rb)
