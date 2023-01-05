---
title: Ruby で MHTML ファイルに変換する
type: docs
weight: 50
url: /ja/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - MHTML ファイルへの変換**
Ruby で Aspose.Cells for Java を使用してワークシートを MHTML ファイルに変換するには、ワークシートを呼び出すだけです。_に_Converter モジュールの mhtml() メソッド。

**ルビーコード**

{{< highlight "ruby" >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**MHTML ファイルへの変換 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
