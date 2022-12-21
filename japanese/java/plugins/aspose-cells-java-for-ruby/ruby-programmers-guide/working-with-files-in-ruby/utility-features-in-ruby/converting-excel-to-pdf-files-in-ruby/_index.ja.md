---
title: Ruby で Excel を PDF ファイルに変換する
type: docs
weight: 30
url: /ja/java/converting-excel-to-pdf-files-in-ruby/
---
## **Aspose.Cells - Excel から PDF ファイルへの変換**
Ruby で Aspose.Cells for Java を使用して Excel を Pdf ファイルに変換するには、Excel を呼び出すだけです。_に_Converter モジュールの pdf() メソッド。

**ルビーコード**

{{< highlight "ruby" >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Excel を PDF ファイルに変換する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
