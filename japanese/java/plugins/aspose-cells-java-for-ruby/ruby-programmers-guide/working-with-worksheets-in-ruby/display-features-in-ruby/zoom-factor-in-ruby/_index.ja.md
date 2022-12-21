---
title: Ruby のズーム率
type: docs
weight: 90
url: /ja/java/zoom-factor-in-ruby/
---
## **Aspose.Cells - ズーム係数**
を使用してズーム係数を設定するには**Aspose.Cells Ruby の場合は Java**、単に呼び出す**ズーム係数**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Setting the zoom factor of the worksheet to 75     

worksheet.setZoom(75)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Set zoom factor, please check the output file."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ズーム倍率 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/zoomfactor.rb)
