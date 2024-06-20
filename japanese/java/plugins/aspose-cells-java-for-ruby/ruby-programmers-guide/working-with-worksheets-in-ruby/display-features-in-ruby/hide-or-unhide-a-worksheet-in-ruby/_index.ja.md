---
title: Rubyでワークシートを非表示または表示する
type: docs
weight: 60
url: /ja/java/hide-or-unhide-a-worksheet-in-ruby/
---

## **Aspose.Cells - ワークシートを非表示または表示する**
### **ワークシートを非表示にする**
Aspose.Cells Java for Rubyを使用してモジュール**hideunhideworksheet**を呼び出してワークシートを非表示にします。

**Ruby Code**

{{< highlight ruby >}}

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
### **ワークシートを表示する**
開発者は、WorksheetクラスのsetVisible(true)メソッドを設定することで、ワークシートを表示できます。

**Ruby Code**

{{< highlight ruby >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、Aspose.Cellsのワークシートの非表示または表示をダウンロードする

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
