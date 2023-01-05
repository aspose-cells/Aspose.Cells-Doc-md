---
title: Ruby でワークシートを非表示または再表示する
type: docs
weight: 60
url: /ja/java/hide-or-unhide-a-worksheet-in-ruby/
---
## **Aspose.Cells - ワークシートを非表示または再表示する**
### **ワークシートを非表示にする**
Ruby で Aspose.Cells Java を使用してワークシートを非表示にするには、次のように呼び出します。**hideunhideワークシート**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Hiding the first worksheet of the Excel file

worksheet.setVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **ワークシートの表示**
開発者は、*setVisible(* *真実* *)*の方法**ワークシート**クラス。

**ルビーコード**

{{< highlight "ruby" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートを非表示または再表示する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
