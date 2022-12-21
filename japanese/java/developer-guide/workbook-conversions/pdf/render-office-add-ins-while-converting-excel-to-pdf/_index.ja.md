---
title: Excel を PDF に変換しながら Office アドインをレンダリングする
type: docs
weight: 90
url: /ja/java/render-office-add-ins-while-converting-excel-to-pdf/
---
## **考えられる使用シナリオ**
以前は、Aspose.Cells は、Excel ファイルが PDF 形式で保存されている場合、Office アドインをレンダリングできませんでした。 Aspose.Cells で問題なく表示されるようになりました。出力 PDF で Office アドインをレンダリングするために特別なメソッドやプロパティを使用する必要はありません。 Excel ファイルを PDF 形式で保存するだけで、Office アドインがレンダリングされます。
## **Excel を PDF に変換しながら Office アドインをレンダリングする**
次のサンプル コードは、[サンプル Excel ファイル](60489783.xlsx)Office アドインが含まれています。をご覧ください[以前のバージョン、つまり 17.11 で生成された出力 PDF](60489781.pdf)そしてその[新しいバージョン、つまり 17.12 以降で生成された出力 PDF](60489782.pdf).以前のバージョンの出力 PDF は空白ですが、新しいバージョンの出力 PDF には Office アドインが表示されます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-RenderOfficeAdd_InsWhileConvertingExcelToPdf.java" >}}
