---
title: Ruby での改ページのプレビュー
type: docs
weight: 70
url: /ja/java/page-break-preview-in-ruby/
---
## **Aspose.Cells - 改ページのプレビュー**
を使用してワークシートを改ページプレビューに設定するには**Aspose.Cells Ruby の場合は Java**、単に呼び出す**改ページプレビュー**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(true)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Set page break preview, please check the output file."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**改ページプレビュー (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreakpreview.rb)
