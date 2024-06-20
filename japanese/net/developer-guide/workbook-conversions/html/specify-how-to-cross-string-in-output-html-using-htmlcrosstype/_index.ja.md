---
title: 出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定
type: docs
weight: 140
url: /ja/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **可能な使用シナリオ**

セルにテキストまたは文字列が含まれており、その幅がセルの幅を超えている場合、次の列のセルがnullまたは空の場合、文字列はオーバーフローします。ExcelファイルをHTMLに保存する際に、このオーバーフローを[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)列挙型を使用して制御することができます。

- **HtmlCrossType.Default**: MS Excelと同様に表示されます。次のセルによって異なります。次のセルがnullの場合、文字列は交わるか切り捨てられます。

- **HtmlCrossType.MSExport**: 文字列はMS ExcelでHTMLをエクスポートしたように表示されます。

- **HtmlCrossType.Cross**: HTMLクロス文字列が表示され、大きなHTMLファイルの作成に対するパフォーマンスがデフォルトまたはFitToCellに値を設定するよりも10倍以上向上します。

- **HtmlCrossType.FitToCell**: セルの幅内でのみ文字列を表示します。

## **出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定**

次のサンプルコードは、異なる [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) を指定して[出力HTML](51740734.zip)を生成したサンプルエクセルファイル](51740732.xlsx)を読み込んで保存します。サンプルエクセルファイルには、スクリーンショットに示されているように赤い枠線で囲まれた画像が含まれています。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
