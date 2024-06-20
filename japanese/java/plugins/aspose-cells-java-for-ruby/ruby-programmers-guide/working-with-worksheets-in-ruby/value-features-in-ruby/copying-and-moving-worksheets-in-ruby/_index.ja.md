---
title: Rubyでワークシートのコピーと移動する
type: docs
weight: 10
url: /ja/java/copying-and-moving-worksheets-in-ruby/
---

## **Aspose.Cells - ワークシートのコピーと移動**
### **ブック内でのワークシートのコピー**
**RubyでAspose.Cells for Javaを使用してワークシートをコピーする**場合は、**copyworksheets**モジュールの**copy_worksheet**メソッドを呼び出します。以下に、コード例が示されています。

**Ruby Code**

{{< highlight ruby >}}

 def copy_worksheet(workbook)

    # Create a Worksheets object with reference to the sheets of the Workbook.

    sheets = workbook.getWorksheets()

    # Copy data to a new sheet from an existing sheet within the Workbook.

    sheets.addCopy("Sheet1")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Copy Worksheet.xls")

    puts "Copy worksheet, please check the output file."

end 

{{< /highlight >}}
### **ワークブック内でワークシートを移動する**
**RubyでAspose.Cells for Javaを使用してワークシートを移動する**場合は、**copyworksheets**モジュールの**move_worksheet**メソッドを呼び出します。以下に、コード例が示されています。

**Ruby Code**

{{< highlight ruby >}}

 def move_worksheet(workbook)

    # Get the first worksheet in the book.

    sheet = workbook.getWorksheets().get(0)

    # Move the first sheet to the third position in the workbook.

    sheet.moveTo(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Move Worksheet.xls")

    puts "Move worksheet, please check the output file."

end 

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のどちらかのソーシャルコーディングサイトから、**Aspose.Cells**の**ワークシートのコピーと移動**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
