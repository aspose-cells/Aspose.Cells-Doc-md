---
title: 出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定
type: docs
weight: 140
url: /ja/python-net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **可能な使用シナリオ**

セルにテキストまたは文字列が含まれており、その幅がセルの幅を超えている場合、次の列のセルがnullまたは空の場合、文字列はオーバーフローします。ExcelファイルをHTMLに保存する際に、このオーバーフローを[**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype)列挙型を使用して制御することができます。

- **HtmlCrossType.DEFAULT** : MS Excelのように表示し、次のセルに依存します。次のセルがnullの場合、文字列はクロス表示されるか切り詰められます。

- **HtmlCrossType.MS_EXPORT** : MS ExcelがHTMLにエクスポートする際と同じように文字列を表示します。

- **HtmlCrossType.CROSS** : HTMLのクロス文字列を表示します。大規模なHTMLファイルの作成パフォーマンスは、DefaultまたはFitToCellに設定するよりも10倍以上高速です。

- **HtmlCrossType.CROSS_HIDE_RIGHT** : HTMLのクロス文字列を表示し、テキストの重複部分は右側の文字列を非表示にします。

- **HtmlCrossType.FIT_TO_CELL** : セルの幅内に文字列を表示します。

## **出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定**

次のサンプルコードは、異なる [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype) を指定して[出力HTML](51740734.zip)を生成したサンプルエクセルファイル](51740732.xlsx)を読み込んで保存します。サンプルエクセルファイルには、スクリーンショットに示されているように赤い枠線で囲まれた画像が含まれています。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SpecifyHtmlCrossTypeInOutputHTML.py" >}}
