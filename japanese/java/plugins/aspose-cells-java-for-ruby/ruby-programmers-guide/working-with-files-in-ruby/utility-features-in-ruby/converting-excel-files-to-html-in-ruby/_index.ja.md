---
title: Ruby で Excel ファイルを HTML に変換する
type: docs
weight: 20
url: /ja/java/converting-excel-files-to-html-in-ruby/
---

## **Aspose.Cells - Excel ファイルを HTML に変換する**
Ruby で Aspose.Cells for Java を使用して Excel を HTML に変換するには、Converter モジュールの worksheet_to_html() メソッドを単純に呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def worksheet_to_html(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."

end 

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に挙げるいずれかのソーシャルコーディングサイトから、**Converting Excel Files to HTML (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
