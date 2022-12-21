---
title: Rubyでワークシートを画像に変換する
type: docs
weight: 60
url: /ja/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells - ワークシートを画像に変換する**
Ruby で Aspose.Cells for Java を使用して Worksheet を Image に変換するには、単に Converter モジュールを呼び出します。

**ルビーコード**

{{< highlight "ruby" >}}

デフォルトワークシート_に_画像(ワークブック)

#ImageOptions のオブジェクトを作成する

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new



# 画像の種類を設定

image_format = Rjb::import('com.aspose.cells.ImageFormat')

画像_options.setImageFormat(画像_format.getPng())



# 最初のワークシートを取得します。

シート = workbook.getWorksheets().get(0)

# 対象シートの SheetRender オブジェクトを作成する

sr = Rjb::import('com.aspose.cells.SheetRender').new(シート, img_options)



j = 0

ながらj< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートを画像に変換 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
