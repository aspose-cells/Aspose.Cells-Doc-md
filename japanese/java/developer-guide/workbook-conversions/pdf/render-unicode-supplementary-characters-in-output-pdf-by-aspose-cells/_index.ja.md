---
title: Aspose.Cells による出力 PDF の Unicode 補助文字のレンダリング
type: docs
weight: 690
url: /ja/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}} 

通常の Unicode 文字の長さは 2 バイトですが、Unicode 補助文字の長さは 4 バイトです。 Aspose.Cells は、これらの 4 バイト Unicode 文字のレンダリングをサポートするようになりました。

Unicode Character Standard では、補助文字は、U+10000 から U+10FFFF までのコード ポイントが割り当てられた文字です。つまり、これらは U+FFFF より大きい Unicode 文字です。

- UTF-8 では、これらの文字の長さはそれぞれ 4 バイトです。
- UTF-16 では、これらの文字には 2 つのサロゲート (16 ビット単位) が必要です。

{{% /alert %}} 
## **Aspose.Cells による出力 PDF の Unicode 補助文字のレンダリング**
次のスクリーンショットは、Aspose.Cells がどのようにレンダリングされたかを示しています。[ソースエクセルファイル](5473390.xlsx)に[PDF出力](5473391.pdf).ご覧のとおり、3 つの Unicode Supplementary 文字はすべて、Microsoft Excel とまったく同じようにレンダリングされています。

![todo:画像_代替_文章](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

このサンプル コードを使用して、[ソースエクセルファイル](5473390.xlsx)の中へ[PDF出力](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
