---
title: Rubyでワークシートを保護する
type: docs
weight: 10
url: /ja/java/protecting-worksheets-in-ruby/
---

## **Aspose.Cells - ワークシートの保護**
Aspose.Cells Java for Rubyを使用してワークシートを保護するには、**protection**モジュールの**protect_worksheet**メソッドを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def protect_worksheet()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)

    protection = worksheet.getProtection()

    # The following 3 methods are only for Excel 2000 and earlier formats

    protection.setAllowEditingContent(false)

    protection.setAllowEditingObject(false)

    protection.setAllowEditingScenario(false)

    # Protects the first worksheet with a password "1234"

    protection.setPassword("1234")



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Protect Worksheet.xls")

    puts "Protect a Worksheet, please check the output file."

end   

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のどちらかのソーシャルコーディングサイトから、**Aspose.Cells**の**ワークシートの保護**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)
