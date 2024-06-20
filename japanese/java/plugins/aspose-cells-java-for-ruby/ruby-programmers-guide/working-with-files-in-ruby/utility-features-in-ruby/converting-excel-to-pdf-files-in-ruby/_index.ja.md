---
title: Ruby で Excel を PDF ファイルに変換する
type: docs
weight: 30
url: /ja/java/converting-excel-to-pdf-files-in-ruby/
---

## **Aspose.Cells - Excel を PDF ファイルに変換する**
Ruby で Aspose.Cells for Java を使用して Excel を PDF ファイルに変換するには、Converter モジュールの excel_to_pdf() メソッドを単純に呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に挙げるいずれかのソーシャルコーディングサイトから、**Converting Excel to PDF Files (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
