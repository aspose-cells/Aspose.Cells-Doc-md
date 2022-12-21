---
title: Ruby で Excel ファイルを HTML に変換する
type: docs
weight: 20
url: /ja/java/converting-excel-files-to-html-in-ruby/
---
## **Aspose.Cells - Excel ファイルを HTML に変換する**
Ruby で Aspose.Cells for Java を使用して Excel を HTML に変換するには、単純にワークシートを呼び出します。_に_Converter モジュールの html() メソッド。

**ルビーコード**

{{< highlight "ruby" >}}

 def worksheet_to_html(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."

end 

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Excel ファイルを HTML に変換する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
