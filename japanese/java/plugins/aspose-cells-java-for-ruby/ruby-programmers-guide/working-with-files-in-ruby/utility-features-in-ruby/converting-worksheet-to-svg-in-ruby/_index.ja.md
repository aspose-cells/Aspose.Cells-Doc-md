---
title: RubyでワークシートをSVGに変換する
type: docs
weight: 70
url: /ja/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - ワークシートを SVG に変換中**
Ruby で Aspose.Cells for Java を使用してワークシートを SVG に変換するには、ワークシートを呼び出すだけです。_に_Converter モジュールの svg() メソッド。

**ルビーコード**

{{< highlight "ruby" >}}

デフォルトワークシート_に_svg(ワークブック)

# 各ワークシートを単一ページの svg 形式に変換します。

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new

save_format = Rjb::import('com.aspose.cells.SaveFormat')

画像_options.setSaveFormat(保存_format.SVG)

img_options.setOnePagePerSheet(true)



# 各ワークシートを svg 形式に変換

sheet_count = workbook.getWorksheets().getCount()

i=0

私がいる間< sheet_count

        sheet = workbook.getWorksheets().get(i)

        sr = Rjb::import('com.aspose.cells.SheetRender').new(sheet, img_options)

        k=0

        while sr.getPageCount()

            # Output the worksheet into Svg image format

            sr.toImage(k, @data_dir + sheet.getName() + "#{k}.svg")

        end

    end

    puts "SVG saved successfully."

end 

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートを SVG に変換中 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
