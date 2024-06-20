---
title: Aspose.Cells による出力PDFでUnicode補助文字をレンダリングする
type: docs
weight: 690
url: /ja/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

通常のUnicode文字は2バイトであり、Unicode補助文字は4バイトです。Aspose.Cells はこれらの4バイトのUnicode文字のレンダリングをサポートしています。

Unicode文字標準では、補助文字はU+10000からU+10FFFFまでのコードポイントが割り当てられています。つまり、これらはU+FFFFよりも大きいUnicode文字です。

- UTF-8では、これらの文字はそれぞれ4バイトです。
- UTF-16では、これらの文字は2つのサロゲート（16ビットユニット）が必要です。

{{% /alert %}} 
## **Aspose.Cellsによる出力PDFでUnicode補助文字をレンダリングする**
以下のスクリーンショットは、Aspose.Cells が [ソースエクセルファイル](5473390.xlsx) を [出力PDF](5473391.pdf) にレンダリングした方法を示しています。Microsoft Excelと同様に、3つのUnicode補助文字が正確にレンダリングされていることがわかります。

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

次のサンプルコードを使用して、[ソースエクセルファイル](5473390.xlsx) を [出力PDF](5473391.pdf) に変換できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
