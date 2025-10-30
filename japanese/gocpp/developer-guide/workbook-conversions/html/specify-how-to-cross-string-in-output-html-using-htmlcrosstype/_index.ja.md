---
title: C++経由のGolangを使用して、出力HTML内での文字の交差方法をHtmlCrossTypeで指定します。
linktitle: 出力HTMLでのHtmlCrossTypeの指定
type: docs
weight: 140
url: /ja/go-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aspose.Cells for C++のHtmlCrossTypeを使用して、HTML出力の文字列オーバーフローを制御する方法を学びます。
---

## **可能な使用シナリオ**

セルにテキストまたは文字列が含まれ、その長さがセルの幅を超える場合、次の列のセルがnullまたは空の場合、その文字列ははみ出します。ExcelファイルをHTMLに保存する際、[**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/)列挙体を使用してこのオーバーフローを制御できます。以下の値があります：

- **HtmlCrossType.Default**: MS Excelと同様に表示されます。次のセルによって異なります。次のセルがnullの場合、文字列は交わるか切り捨てられます。

- **HtmlCrossType.MSExport**: 文字列はMS ExcelでHTMLをエクスポートしたように表示されます。

- **HtmlCrossType.Cross**: HTMLクロス文字列が表示され、大きなHTMLファイルの作成に対するパフォーマンスがデフォルトまたはFitToCellに値を設定するよりも10倍以上向上します。

- **HtmlCrossType.FitToCell**: 文字列をセル内の幅に合わせて表示します。

## **出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定**

以下のサンプルコードは、[サンプルExcelファイル](51740732.xlsx)を読み込み、異なる [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) を指定してHTML形式に保存します。このコードで生成された[出力HTML](51740734.zip)をダウンロードしてください。サンプルExcelファイルには、赤色の枠線で囲まれた画像が含まれています。このスクリーンショットは、[**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) の値が出力HTMLに与える影響を示しています。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputHtmlUsingHtmlcrosstype.go" >}}
