---
title: Ruby でのワークシートのコピーと移動
type: docs
weight: 10
url: /ja/java/copying-and-moving-worksheets-in-ruby/
---
## **Aspose.Cells - ワークシートのコピーと移動**
### **ワークブック内でワークシートをコピーする**
を使用してワークシートをコピーするには**Aspose.Cells ルビーで for Java**、 電話**copy_worksheet**方法**コピーワークシート**モジュール。以下にコード例を示します。

**ルビーコード**

{{< highlight "ruby" >}}

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
を使用してワークシートを移動するには**Aspose.Cells ルビーで for Java**、 電話**move_worksheet**方法**コピーワークシート**モジュール。以下にコード例を示します。

**ルビーコード**

{{< highlight "ruby" >}}

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
## **実行中のコードをダウンロード**
ダウンロード**ワークシートのコピーと移動 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
