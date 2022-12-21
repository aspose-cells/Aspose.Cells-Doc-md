---
title: ボーダー スタイルが Web ブラウザーでサポートされていない場合に、同様のボーダー スタイルをエクスポートする
type: docs
weight: 70
url: /ja/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **考えられる使用シナリオ**

Microsoft Excel は、Web ブラウザでサポートされていないある種の破線枠をサポートしています。このような Excel ファイルを Aspose.Cells を使用して HTML に変換すると、そのような境界線が削除されます。ただし、Aspose.Cells も同様の境界線の表示をサポートできます。[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)財産。その値を次のように設定してください**真実**サポートされていない境界線も HTML ファイルにエクスポートされます。

## **ボーダー スタイルが Web ブラウザーでサポートされていない場合に、同様のボーダー スタイルをエクスポートする**

次のサンプル コードは、[サンプル Excel ファイル](64716832.xlsx)次のスクリーンショットに示すように、サポートされていない境界線が含まれています。スクリーンショットは、[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)内部のプロパティ[出力HTML](64716831.zip).

![todo:画像_代替_文章](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
