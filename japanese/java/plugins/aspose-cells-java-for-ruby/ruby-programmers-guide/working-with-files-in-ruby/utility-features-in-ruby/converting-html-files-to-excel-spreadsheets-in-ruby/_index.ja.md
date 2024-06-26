---
title: Ruby で HTML ファイルを Excel スプレッドシートに変換する
type: docs
weight: 40
url: /ja/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---

## **Aspose.Cells - HTML ファイルを Excel スプレッドシートに変換する**
Ruby で Aspose.Cells for Java を使用して HTML をスプレッドシートに変換するには、Converter モジュールの html_to_excel() メソッドを単純に呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def html_to_excel()

    load_format = Rjb::import('com.aspose.cells.LoadFormat')

    # Create an instance of HTMLLoadOptions and initiate it with appropriate LoadFormat

    options = Rjb::import('com.aspose.cells.HTMLLoadOptions').new(load_format.HTML)



    # Load the Html file through file path while passing the instance of HTMLLoadOptions class

    workbook = Rjb::import('com.aspose.cells.Workbook').new(@data_dir + "index.html", options)



    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    #Save the results to disc in Xlsx format

    workbook.save(@data_dir + "output.xlsx", save_format.XLSX)

    puts "XLSX saved successfully."

end

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に挙げるいずれかのソーシャルコーディングサイトから、**Converting HTML files to Excel Spreadsheets (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
