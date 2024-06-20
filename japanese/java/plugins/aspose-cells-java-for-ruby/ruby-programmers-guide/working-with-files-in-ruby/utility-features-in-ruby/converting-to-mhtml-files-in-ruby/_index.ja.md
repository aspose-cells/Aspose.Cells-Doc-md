---
title: Ruby で MHTML ファイルに変換する
type: docs
weight: 50
url: /ja/java/converting-to-mhtml-files-in-ruby/
---

## **Aspose.Cells - MHTML ファイルに変換する**
Ruby で Aspose.Cells for Java を使用して Worksheet を MHTML ファイルに変換するには、Converter モジュールの worksheet_to_mhtml() メソッドを単純に呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に挙げるいずれかのソーシャルコーディングサイトから、**Converting to MHTML Files (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
