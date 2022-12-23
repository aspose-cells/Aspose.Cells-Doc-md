---
title: RubyでHTMLファイルをExcelスプレッドシートに変換する
type: docs
weight: 40
url: /ja/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---
## **Aspose.Cells - HTML ファイルを Excel スプレッドシートに変換する**
Ruby で Aspose.Cells for Java を使用して HTML をスプレッドシートに変換するには、単純に html を呼び出します。_に_Converterモジュールのexcel()メソッド。

**ルビーコード**

{{< highlight "ruby" >}}

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
## **実行中のコードをダウンロード**
ダウンロード**HTML ファイルを Excel スプレッドシートに変換する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
