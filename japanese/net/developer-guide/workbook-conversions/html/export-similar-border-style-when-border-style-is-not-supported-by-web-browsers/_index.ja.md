---
title: Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする
type: docs
weight: 70
url: /ja/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **可能な使用シナリオ**

Microsoft ExcelはWebブラウザでサポートされていない一部の破線ボーダーをサポートしています。Aspose.Cellsを使用してこのようなExcelファイルをHTMLに変換すると、そのようなボーダーは削除されます。ただし、Aspose.Cellsは[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)プロパティもサポートし、その値を**true**に設定すると、サポートされていないボーダーもHTMLファイルにエクスポートされます。

## **Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする**

次のサンプルコードは、[サンプルExcelファイル](64716806.xlsx)を読み込み、{0}プロパティを{1}に設定した後、[output HTML](64716804.zip)に保存します。スクリーンショットは、**default output**から**{2}**が出力されたHTMLへの影響を示しています。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
{{< app/cells/assistant language="csharp" >}}
