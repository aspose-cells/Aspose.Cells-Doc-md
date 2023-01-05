---
title: ボーダー スタイルが Web ブラウザーでサポートされていない場合に、同様のボーダー スタイルをエクスポートする
type: docs
weight: 70
url: /ja/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **考えられる使用シナリオ**

Microsoft Excel は、Web ブラウザでサポートされていないある種の破線枠をサポートしています。このような Excel ファイルを Aspose.Cells を使用して HTML に変換すると、そのような境界線が削除されます。ただし、Aspose.Cells は、そのような境界線の表示をサポートすることもできます[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)財産。その値を次のように設定してください**真実**サポートされていない境界線も HTML ファイルにエクスポートされます。

## **ボーダー スタイルが Web ブラウザーでサポートされていない場合に、同様のボーダー スタイルをエクスポートする**

次のサンプル コードは、[サンプル Excel ファイル](64716806.xlsx)次のスクリーンショットに示すように、サポートされていない境界線が含まれています。スクリーンショットは、[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)内部のプロパティ[出力 HTML](64716804.zip).

![todo:画像_代替_文章](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
